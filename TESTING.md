# TESTING USER STORIES

Testing user stories goes here

---

# DJANGO TESTING

## Django Unit Testing

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure basic Django Allauth form is working as intended | Basic Django Allauth form is working as intended. Images confirming the outcome of this test. [Allauth test 1](wireframes/allauth_test2.png) - [Allauth test 2](wireframes/allauth_test.png) | PASS
Ensure Django authenticates emails | Django authenticates emails. Image confirming the outcome of this test. [Allauth test 3](wireframes/allauth_test3.png) | PASS
Ensure login system redirects back to the login redirect url in settings | Login system redirects back to the login redirect url in settings. The 'success' url was created to test this. [Allauth test 4](wireframes/allauth_test4.png) | PASS
Ensure the appropiate categories are loaded with the correct fixtures | The appropiate categories are loaded with the correct fixtures. [Load data categories](wireframes/loaddata_categories.png) | PASS
Ensure the appropiate products are loaded with the correct fixtures | The appropiate products are loaded with the correct fixtures. [Load data products](wireframes/loaddata_products.png) | PASS
Ensure in Django Admin 'Categorys' is changed to 'Categories' and the friendly name is diaplayed | in Django Admin 'Categorys' is changed to 'Categories' and the friendly name is diaplayed. [Friendly name](wireframes/friendly_name.png) | PASS
Ensure all car models are displaying on the page with the correct url | All car models are displaying on the page with the correct url. [All products test](wireframes/all_products.png) | PASS 


## Searching and Filtering

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure searching for a particular car name, gives the user the correct response. | Searching for a particular car name, gives the user the correct response. [Search result](wireframes/search_result1.png) | PASS
Ensure if a user searches for example 'blue', the search result not only returns the name but also the description. | If a user searches for example 'blue', the search result not only returns the name but also the description. [Search result](wireframes/search_result2.png) | PASS
Ensure that searches are user friendly by making queries case insensitive. | Searches are user friendly by making queries case insensitive. ```queries = Q(name__icontains=query) Q(description__icontains=query)``` | PASS
Ensure the appropiate filtering is applied when user is using the main navigational links. | The appropiate filtering is applied when user is using the main navigational links. [Filter result 1](wireframes/filter_sample1.png) - [Filter result 2](wireframes/filter_sample2.png) - [Filter result 3](wireframes/filter_sample3.png) - [Filter result 4](wireframes/filter_sample4.png) | PASS
Ensure cars are sorted By Price ascending | Cars are sorted by Price ascending ``` {% url 'products' %}?sort=price&direction=asc ``` | PASS
Ensure cars are sorted By Rating descending | Cars are sorted by Rating descending ``` {% url 'products' %}?sort=rating&direction=desc ``` | PASS
Ensure cars are sorted By Category descending | Cars are sorted by Category descending ``` {% url 'products' %}?sort=category&direction=asc ``` | PASS
Ensure a clickable link with the approiate car category is in each card on the products page | A clickable link with the approiate car category is in each card on the products page. [Sorting category](wireframes/sorting_cat1.png) | PASS
Ensure a clickable link with the approiate car category is displayed on the product details page | A clickable link with the approiate car category is displayed on the product details page. [Sorting category](wireframes/sorting_cat2.png) | PASS
Ensure when a badge is clicked the approiate category is displayed. | When a badge is clicked the approiate category is displayed. | PASS


---

# MANUAL TESTING

## Front End Testing

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure Bootstrap is connected and returning the correct url | Bootstrap is connected and returning the correct url. Image confirming the outcome of this test. [Bootstrap test](wireframes/bootstrap_test.png) | PASS
Ensure basic search functionality works as intended | When a search query is submitted, the result is returned to the address bar. Image confirming the outcome of this test. [Search test](wireframes/searchtest.png) | PASS
Ensure when the My Account is clicked a dropdown menu shows Register and Login | When the My Account is clicked a dropdown menu shows Register and Login. Image confirming the outcome of this test. [Menu test](wireframes/menutest.png) | PASS
Ensure footer social network links work and open up in a new browser tab | Footer social network links work and open up in a new browser tab | PASS
Enusure basic CSS styles are working with the Products page | Basic CSS styles are working with the Products page. [CSS test](wireframes/products_css.png) | PASS
Ensure when DISCOVER NOW button is clicked, user is directed to all products page. | When DISCOVER NOW button is clicked, user is directed to all products page. | PASS
Ensure when a car is click on all products page, user is taken to the product detail page. | When a car is click on all products page, user is taken to the product detail page. [Product detail](wireframes/product_details.png) | PASS
Ensure that when a user is in the product details page, should they click on the image, a larger image is opened up in a new browser tab. | When a user is in the product details page, should they click on the image, a larger image is opened up in a new browser tab. [Larger image](wireframes/larger_image.png) | PASS
Ensure when a user clicks on the All Cars link in the main nav bar, user is directed to the all products page. | When a user clicks on the All Cars link in the main nav bar, user is directed to the all products page. | PASS
Ensure when a user clicks on the car category link in the card of the products page they are then taken to the page that holds that category of cars. | When a user clicks on the car category link in the card of the products page they are then taken to the page that holds that category of cars. | PASS
Ensure when a user hovers over a badge, the colours invert. | When a user hovers over a badge, the colours invert. [badges hover](wireframes/badges_hover.png) | PASS
 

---

# DETAILED TESTING


TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------


# CHROME LIGHTHOUSE REPORT

---

# RESPONSIVENESS TESTING

## Navbar Responsiveness

Ensure Navbar displays as intended across devices and laptops.

- Navbar displays as intended on laptop and larger screens.

![Navbar larger screens](wireframes/navbar_larger.png)

- Navbar displays as intended on smaller screens.

![Navbar smaller screens](wireframes/navbar_smaller.png)

- Navbar displays as intended on mobile screens.

![Navbar mobile screens](wireframes/navbar_mobile.png)

## Footer Responsiveness

Ensure Footer displays as intended across devices and laptops.

- Footer displays as intended on laptop and larger screens.

![footer larger screens](wireframes/footer_lager.png)

- Footer displays as intended on smaller screens.

![footer smaller screens](wireframes/footer_smaller.png)

- Footer displays as intended on mobile screens.

![footer mobile screens](wireframes/footer_mobile.png)

## Car Products Page

Ensure Car Products page displays as intended across devices and laptops.

- Car Products page displays as intended on laptop and larger screens.

![products larger screens](wireframes/carproducts_large.png)

- Car Products page displays as intended on smaller screens.

![products smaller screens](wireframes/carproducts_smaller.png)

- Car Products page displays as intended on mobile screens.

![products mobile screens](wireframes/carproducts_mobile.png)

---

# BUGS AND ISSUES