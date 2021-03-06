from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm


def all_products(request):
    """ A view to show all cars, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any \
                                         search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual car details """

    product = get_object_or_404(Product, pk=product_id)

    num_comments = Comment.objects.filter(product=product).count()

    context = {
        'product': product,
        'num_comments': num_comments
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "You've successfully added a new car!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add a product. Please ensure \
                the form is filled out correctly.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully updated product!")
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update the product, please \
                ensure the form is filled out correctly.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect(reverse('products'))


def add_comment(request, product_id):
    """ Comment on a particular product """
    product = get_object_or_404(Product, pk=product_id)

    form = CommentForm(instance=product)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=product)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=product, comment_name=name,
                        comment_body=body)
            c.save()
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'products/add_comment.html', context)


def delete_comment(request, comment_id):
    """ Delete the comment """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment successfully deleted.')
    return redirect(reverse('products'))


def edit_comment(request, comment_id):
    """ Edit the comment """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_comment', args=[comment_id]))
        else:
            messages.error(request, 'Failed to edit the comment, please \
                ensure the form is filled out correctly.')
    else:
        form = CommentForm(instance=comment)

    template = 'products/add_comment.html'
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)
