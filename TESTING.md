# DJANGO TESTING

## Django Unit and Template Testing

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure basic Django Allauth form is working as intended | Basic Django Allauth form is working as intended. Images confirming the outcome of this test. [Allauth test 1](wireframes/allauth_test2.png) - [Allauth test 2](wireframes/allauth_test.png) | PASS
Ensure Django authenticates emails | Django authenticates emails. Image confirming the outcome of this test. [Allauth test 3](wireframes/allauth_test3.png) | PASS
Ensure login system redirects back to the login redirect url in settings | Login system redirects back to the login redirect url in settings. The 'success' url was created to test this. [Allauth test 4](wireframes/allauth_test4.png) | PASS
Ensure the appropiate categories are loaded with the correct fixtures | The appropiate categories are loaded with the correct fixtures. [Load data categories](wireframes/loaddata_categories.png) | PASS
Ensure the appropiate products are loaded with the correct fixtures | The appropiate products are loaded with the correct fixtures. [Load data products](wireframes/loaddata_products.png) | PASS
Ensure in Django Admin 'Categorys' is changed to 'Categories' and the friendly name is diaplayed | in Django Admin 'Categorys' is changed to 'Categories' and the friendly name is diaplayed. [Friendly name](wireframes/friendly_name.png) | PASS
Ensure all car models are displaying on the page with the correct url | All car models are displaying on the page with the correct url. [All products test](wireframes/all_products.png) | PASS
Ensure the cart page renders correctly. | The cart page renders correctly when the users clicks or taps on delivery truck. [Cart page render](wireframes/cart_page.png) | PASS
Ensure that if no items are in the cart, text is displayed telling the user. | If no items are in the cart, text is displayed telling the user. [Empty cart](wireframes/empty_cart.png) | PASS
Enusre the Free Mechanical Services threshold is consistently displayed on every page throughout the site. | The Free Mechanical Services threshold is consistently displayed on every page throughout the site. | PASS
Ensure items are added to the cart and are displaying in the terminal. | Items are added to the cart and are displaying in the terminal. [Add to cart test](wireframes/cart_test_1.png) | PASS
Ensure items are visible in the cart with the correct price attached. | Items are visible in the cart with the correct price attached. [Add to cart test](wireframes/cart_test.png) | PASS
Ensure items are added to the cart displaying, images and prices accordingly. | Items are added to the cart displaying, images and prices accordingly. [Cart items test](wireframes/cart_items.png) | PASS
Ensure items in the cart add up to the correct amount, are displayed to the user in the cart and in the menu. | Items in the cart add up to the correct amount, are displayed to the user in the cart and in the menu. [Cart items test](wireframes/cart_items.png) | PASS
Ensure users are able to delete cars from the cart. | Users are able to delete cars from the cart. When a user clicks on the Remove Car button, car is removed, the total is amended and the page reloads. | PASS
Ensure the appropiate toast message is displayed when a user adds a car to the cart. | The appropiate toast message is displayed when a user adds a car to the cart. [Toast message success 1](wireframes/car_added_success.png) | PASS
Ensure the appropiate toast message is displayed when a user removes a car from the cart. | The appropiate toast message is displayed when a user removes a car from the cart. [Toast message success 2](wireframes/car_removed_toast.png) | PASS
Ensure the product image is displayed within the toast notifications. | The product image is displayed within the toast notifications. [toast image](wireframes/toast_nods.png) | PASS
Ensure the total cost is displayed within the toast notifications. | The total cost is displayed within the toast notifications. [toast image](wireframes/toast_nods.png) | PASS
Ensure the CHECKOUT button takes the user to the checkout page. | The CHECKOUT button takes the user to the checkout page. | PASS
Ensure the appropiate fields are added to the admin checkout. | The appropiate fields are added to the admin checkout. [Admin checkout](wireframes/admin_checkout.png) | PASS
Ensure cripsy forms renders the correct fields. | Crispy forms renders the correct form fiels on the checkout page. Fields marked with an asterisk are required, preventing the form from being submitted unless these fields are filled out. | PASS
Ensure on the checkout page a preview of what the user is buying, an image of the product, its cost and quantity. | On the checkout page a preview of what the user is buying, an image of the product, its cost and quantity. | PASS
Ensure Django-Countries displays a dropdown list of countries. | Django-Countries displays a dropdown list of countries. | PASS
Ensure Full Name contains an * and is required. Unless this field is entered the form is not submitted. | Full Name contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure Email contains an * and is required. Unless this field is entered the form is not submitted. | Email contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure Street Address1 contains an * and is required. Unless this field is entered the form is not submitted. | Street Address1 contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure Phone Number contains an * and is required. Unless this field is entered the form is not submitted. | Phone Number contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure Town Or City contains an * and is required. Unless this field is entered the form is not submitted. | Town Or City contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure Country contains an * and is required. Unless this field is entered the form is not submitted. | Country contains an * and is required. Unless this field is entered the form is not submitted. | PASS
Ensure if a user enters invalid credentials, an error message is displayed telling them what went wrong. | If a user enters invalid credentials, an error message is displayed telling them what went wrong. [Sign In error](wireframes/sign_in_error.png) | PASS
Ensure when a user signs in with the right credentials, an alert message is displayed telling them so. | When a user signs in with the right credentials, an alert message is displayed telling them so. [Sign In success1](wireframes/sign_in_success.png) | PASS
Ensure when a user signs up a confirmation email is sent to the user with a confirm link. | When a user signs up a confirmation email is sent to the user with a confirm link. This is carried out in the terminal at this point. [Confirm email1](wireframes/verify_email.png) | PASS
When a user confirms their email address ensure a toast message is displayed to the user. | When a user confirms their email address a toast message is displayed to the user. [Confirm email2](wireframes/confirm_email.png) | PASS
Ensure when a user successfully signs in, a toast message is displayed telling them so. | When a user successfully signs in, a toast message is displayed telling them so. [Sign In success2](wireframes/signin_success.png) | PASS
Ensure the user's username is displayed when they go to their profile page. | The user's username is displayed when they go to their profile page. [User profile](wireframes/user_profile.png) | PASS
Ensure when a user updates their profile delivery info, a toast message is displayed telling that the change has been successfully made. | When a user updates their profile delivery info, a toast message is displayed telling that the change has been successfully made. [Update profile](wireframes/updated_profile.png) | PASS
Ensure when a user ticks the save order button, their order is saved to their profile. | When a user ticks the save order button, their order is saved to their profile. This tests also shows that all order details have been populated to the order history form. [Order history](wireframes/order_history.png) | PASS
Ensure when a user clicks on the order number in the order history, they are prompted with an alert that it is a past order. | When a user clicks on the order number in the order history, they are prompted with an alert that it is a past order. [Order number](wireframes/order_number.png) | PASS
Ensure the appropriate error message is displayed if the add products form is filled out incorrectly. | The appropriate error message is displayed if the add products form is filled out incorrectly. [Add products error](wireframes/addproducts_error.png) | PASS
Ensure the appropriate success message is displayed if the add products form is filled out correctly. | The appropriate success message is displayed if the add products form is filled out correctly. [Add products success](wireframes/addproducts_success.png) | PASS
Ensure that products are successfully added. If product has no image, the appropiat noimage.png is displayed. | Products are successfully added. If product has no image, the appropiate noimage.png is displayed. [Add products](wireframes/addproducts.png) | PASS
Ensure new product images are uploaded successfully. | New product images are uploaded successfully. [Product image](wireframes/product_image.png) - [Product image2](wireframes/product_image2.png) | PASS
Ensure the appropiate message is displayed when a product has been updated successfully. | The appropiate message is displayed when a product has been updated successfully. When product has been updated, the admin is redirected to the specific product detail page. [Edit success](wireframes/edit_success.png) | PASS
Ensure when a new product is added they are redirected to that specific product detail page with the correct id displayed in the browser. | When a new product is added they are redirected to that specific product detail page with the correct id displayed in the browser. [Add products2](wireframes/addproduct_id.png) | PASS
Ensure the appropiate messages is displayed when a product has been deleted. | The appropiate messages is displayed when a product has been deleted. [Delete product](wireframes/delete_product.png) | PASS
Ensure when logged in as the Superuser, Edit and Delete buttons are displayed on the products page and the products detail page. | When logged in as the Superuser, Edit and Delete buttons are displayed on the products page and the products detail page. [Edit delete1](wireframes/edit_delete1.png) - [Edit delete2](wireframes/edit_delete2.png) | PASS
Ensure defensive programming is installed to prevent against someone from deleting or editing our products on the off chance they know the correct URLs. | Defensive programming is installed to prevent against someone from deleting or editing our products on the off chance they know the correct URLs. [Defensive programming](wireframes/defensive_prog.png) | PASS
Ensure when the site owner is uploading a new car image, they are provided with the correct message as to what the image will be. | When the site owner is uploading a new car image, they are provided with the correct message as to what the image will be. [Image select](wireframes/select_image.png) | PASS
Ensure when the site owner is editing a product, when clicking on the remove checkbox and then update car button, the car image is removed. | When the site owner is editing a product, when clicking on the remove checkbox and then update car button, the car image is removed. | PASS
Ensure when a user is signing up, any mistakes they make when filling out the form, is instantly displayed to them. | When a user is signing up, any mistakes they make when filling out the form, is instantly displayed to them. [Sign up errors1](wireframes/signup_errors1.png) - [Sign up errors2](wireframes/signup_errors2.png) | PASS

---


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
Ensure SORT BY dropdown select sorts cars by Price (high to low) | SORT BY dropdown select sorts cars by Price (high to low). [Sorting by price high to low](wireframes/high_to_low.png) | PASS
Ensure SORT BY dropdown select sorts cars by Price (low to high) | SORT BY dropdown select sorts cars by Price (low to high). [Sorting by price low to high](wireframes/low_to_high.png) | PASS
Ensure SORT BY dropdown select sorts cars by Rating (high to low) | SORT BY dropdown select sorts cars by Rating (high to low). [Sorting by rating high to low](wireframes/rating_high.png) | PASS
Ensure SORT BY dropdown select sorts cars by Rating (low to high) | SORT BY dropdown select sorts cars by Rating (low to high). [Sorting by rating low to high](wireframes/rating_low.png) | PASS
Ensure SORT BY dropdown select sorts cars by Name (A-Z) | SORT BY dropdown select sorts cars by Name (A-Z). [Sorting by name a-z](wireframes/name_a_z.png) | PASS
Ensure SORT BY dropdown select sorts cars by Name (Z-A) | SORT BY dropdown select sorts cars by Name (Z-A). [Sorting by name z-a](wireframes/name_z_a.png) | PASS
Ensure SORT BY dropdown select sorts cars by Category (A-Z) | SORT BY dropdown select sorts cars by Category (A-Z). [Sorting by category a-z](wireframes/category_a_z.png) | PASS
Ensure SORT BY dropdown select sorts cars by Category (Z-A) | SORT BY dropdown select sorts cars by Category (Z-A). [Sorting by category z-a](wireframes/category_z_a.png) | PASS
Ensure the amount of cars in a particular category are clearly displayed to the user. | The amount of cars in a particular category are clearly displayed to the user. [Cars in category](wireframes/product_amount.png) | PASS
Ensure when a user searches for something, they see their query ruturned, a count of the products, what they searched, with a link back to the main products page. | When a user searches for something, they see their query ruturned, a count of the products, what they searched, with a link back to the main products page. [Search result](wireframes/search_result.png) | PASS
Ensure the appropiate toast message is displayed to the user if they put in any search queries and press enter anyway. | The appropiate toast message is displayed to the user if they put in any search queries and press enter anyway. [Search error](wireframes/search_error_toast.png) | PASS


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
Ensure Back-To-Top button takes the user back to the top of the page when clicked. | Back-To-Top button takes the user back to the top of the page when clicked. | PASS
Ensure when on the cart page, clicking on the Keep Browsing Cars button returns the user to the products page. | When on the cart page, clicking on the Keep Browsing Cars button returns the user to the products page. | PASS
Ensure a custom 404 Error page is displayed to the user if they enter a page that does not exist. | A custom 404 Error page is displayed to the user if they enter a page that does not exist. [404 Error](wireframes/404_error.png) | PASS
Ensure when the admin is logged in, in order to prevent accidental deletion of a product, a popup modal is displayed to the admin with clear instructions contained. | When the admin is logged in, in order to prevent accidental deletion of a product, a popup modal is displayed to the admin with clear instructions contained. [Modal](wireframes/modal.png) | PASS

---

# STRIPE TESTING

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure the Stripe script is added to BASE.html | The Stripe script ```<script src="https://js.stripe.com/v3/"></script>``` is added to BASE.html within the block corejs. | PASS
Ensure the postloadjs block contains ```stripe_public_key json_script:"id_stripe_public_key"``` and ```client_secret json_script:"id_client_secret"``` within checkout.html. | The postloadjs block ```stripe_public_key json_script:"id_stripe_public_key"``` and ```client_secret json_script:"id_client_secret"``` within checkout.html. | PASS
Ensure the Stripe public key is added to the context of the checkout views.py | The Stripe public key is added to the context of the checkout views.py | PASS
Ensure the Stripe public key and client secret are being rendered to the browser. | The Stripe public key and client secret are being rendered to the browser. [Stripe test](wireframes/stripe_test.png) | PASS
Ensure if an invalid credit card number is entered the card number turns red. | If an invalid credit card number is entered the card number turns red. [Invalid credit card](wireframes/invalid_credit_card.png) | PASS
Ensure a message is displayed to the user if they input incorrect card details. | A message is displayed to the user if an invalid card number is inputted. [Invalid card message](wireframes/invalid_card_error.png) | PASS
Ensure Stripe Public Keys and Secret Keys are added to Gitpod variables. | Stripe Public Keys and Secret Keys are added to Gitpod variables. [Gitpod variables](wireframes/gitpod_variables.png) | PASS
Ensure Stripe payment intents are being rendered correctly, displaying as a list to the terminal. | Stripe payment intents are being rendered correctly, displaying as a list to the terminal. [Stripe payment intent test](wireframes/payment_intent.png) | PASS
Ensure the core functionality of the payment process works by generating a successful payment intent. | The core functionality of the payment process works by generating a successful payment intent. [Stripe intent success1](wireframes/payment_intent_succeeded1.png) - [Stripe intent success2](wireframes/payment_intent_succeeded2.png) | PASS
Ensure when a user submits their payment informatiom, the order is created in a database. | When a user submits their payment informatiom, the order is created in a database. [Order database](wireframes/order_db.png) | PASS
Ensure when a user submits their payment informatiom, they are redirected to a success page with a randomly generated order number. | When a user submits their payment informatiom, they are redirected to a success page with a randomly generated order number. [Order success](wireframe/order_success.png) | PASS
Ensure when a user successfully purchases a car, their cart is emptied afterwards. | When a user successfully purchases a car, their cart is emptied afterwards. | PASS
Ensure that when a purchase is made, an order summary is rendered on the checkout_success page. | When a purchase is made, an order summary is rendered on the checkout_success page. [Order summary](wireframes/order_summary.png) | PASS 
Ensure that if a user doesn't fill out street_address2, county or postcode in the order form that these aren't rendered in the order sumnmary. | If a user doesn't fill out street_address2, county or postcode in the order form that these aren't rendered in the order sumnmary. [Order summary](wireframes/order_summary.png) | PASS
Testing Stripe authentication. | By using the test credit card number ```4000 0027 6000 3184``` Stripe intiates a modal asking the customer to authenticate. If the credit card number ```4242 4242 4242 4242``` is used, no authentication is required from the user [Stripe authentication](wireframes/stripe_extra_secruity.png) | PASS
Ensure the user receives a confirmation email once their order is complete. | The user receives a confirmation email once their order is complete. | PASS


---

# STRIPE WEBHOOK TESTING


TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure Stripe webhook view is working. | Stripe webhook view is working. [Webhook Test1](wireframes/stripewh_terminal.png) - [Webhook Test2](wireframes/stripewh_test1.png) | PASS
Ensure Stripe webhook payment intent succeeded is working as intended. | Stripe webhook payment intent succeeded is working as intended. [Webhook Test3](wireframes/payment_succeeded.png) | PASS
Ensure Stripe webhook payment intent failed is working as intended. | Stripe webhook payment intent failed is working as intended. [Webhook Test4](wireframes/payment_failed.png) | PASS
Ensure webhook handler prints out the intent coming from Stripe once the user makes a payment. | Webhook handler prints out the intent coming from Stripe once the user makes a payment. Biling info, shiping info and metadata are attached. [Webhook Test5](wireframes/wh_intent.png) | PASS
Ensure that in the event of an impatient user, the webhook captures the intent and stores the order in the database. | In the event of an impatient user, the webhook captures the intent and stores the order in the database. | PASS
Ensure that in the event a user accidentally closes the broswer window, their order remains in the cart when they come back to the site. | In the event a user accidentally closes the broswer window, their order remains in the cart when they come back to the site. | PASS
If a user is filling out the order form and they hit submit but the close the browser, ensure the order does not go through. | If a user is filling out the order form and they hit submit but the close the browser, the order does not go through. | PASS
Ensure webhook handler is updated to handle the profiles. | Webhook handler is updated to handle the profiles. | PASS


---

# Stripe Webhook Testing On The Live Site

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure Stripe webhooks are being sent successfully on the live site. | Stripe webhooks are being sent successfully on the live site. [Webhook Test6](wireframes/stripe_wh_test.png) | PASS

---

# Sending Real Emails Tests

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Ensure customer receives a real email to confirm their email address. | Customer receives a real email to confirm their email address. [Email test1](wireframes/real_email_test.png) | PASS
Ensure customer receives a real email with their complete order information. | Customer receives a real email with their complete order information. Email contains an unique order number, order date and time, order total, delivery address and phone number. Order number is also added to the subject line [Email test2](wireframes/real_email_test.png) | PASS
Ensure on the CONTACT US page, when a user clicks on the email link, the user's email client opens. | When on the CONTACT US page, when a user clicks on the email link, the user's email client opens. | PASS
Ensure when a user clicks or taps on the phone number on the CONTACT US page, they are given the option to make an actual call. | When a user clicks or taps on the phone number on the CONTACT US page, they are given the option to make an actual call. | PASS
Ensure on the CONTACT US page, the RESET FORM button clears all fields when clicked. | On the CONTACT US page, the RESET FORM button clears all fields when clicked. | PASS
Ensure a Success message is displayed to the user when they click send when on the contact page. | A Success message is displayed to the user when they click send when on the contact page. [Contact success](wireframes/contact_success.png) | PASS
Ensure an Error message is displayed to the user if the form is not filled out correctly when on the contact page. | An Error message is displayed to the user if the form is not filled out correctly when on the contact page. | PASS
Ensure when the user is on the contact page, when they click send they are redirected to the Contact Success page. | When the user is on the contact page, when they click send they are redirected to the Contact Success page. | PASS
Ensure the contact form is not submitted unless all required fields are filled out. | The contact form is not submitted unless all required fields are filled out. | PASS
Ensure Contact Us messages are saved to the admin page. | Contact Us messages are saved to the admin page. [Contact msg saved](wireframes/contact_admin.png) | PASS
Ensure the user receives a confirmation email of the message they sent through the contact form. | The user receives a confirmation email of the message they sent through the contact form. [Confirmation email](wireframes/confirmation_contact.png) | PASS

---

# DETAILED WALKTHROUGH TEST

## Navigating and Purchasing

- User navigates to: https://classic-ford-cars.herokuapp.com/

- User clicks on DISCOVER NOW button or they use the main links to look up cars.

    - DISCOVER NOW button shows all the various different car products.

- User selects a car to purchase and is taken to the product detail page.
    - Here they can either KEEP BROWSING or ADD CAR TO CART.

    - Clicking on the KEEP BROWSING button takes the user to the all products page.
    - Clicking on ADD CAR TO CART displays an instant notification of the car product and cost.
        - Car cost is also displayed underneath the truck icon.

- User then clicks on GO TO SECURE CHECKOUT and is taken to the cart page with all of the product info contained. 
    - Within the product info, user sees an image.

    - The name of the model.
    - The cost.
    - Quantity.
    - And subtotal.
        - If they want, user can remove the item from the cart.
    - The user has two options:
        - To CONTINUE BROWSING (item remains in the cart).

        - Or they can SECURE CHECKOUT, which takes them to the checkout page.

- With the user now on the checkout page, the user is required to fill out a form.
    - Fields marked with an (*) are required.
        - If user fails to fill out a required field, the user is altered of the error.
    
    - Users can either create an account or login to save the information if they wish.

    - User then enters credit card details.
        - If user enters incorrect card details, the user is instantly altered of the error.

    - User can the either adjust their cart or complete the order.

        - Clicking on the ADJUST CART takes the user to the cart page.

        - Clicking on COMPLETE YOUR ORDER makes the purchase, providing there are no errors in the form.

        - User then receives an confirmation email with a complete order summary.

## Register and Login

- Clicking on the MY ACCOUNT button reveals to options:

    - Register and Login

        - Clicking on the Register button takes the user to the sign up page.

            - Users can't register an account unless all fields ae filled out.

            - When a form is submitted successfully, user receives an email to confirm their email.

            - Clicking on the link in the email opens up the website in a new broswer tab with a confirm button.

            - The user is now sucessfully registered and can log in and out whenever.

The benefits for creating an account is that users have the ability to save their order details and view their past orders.


## Project Management

- Logging in as the website's owner gives the owner extra permissions.

- Clicking on the Poject Management button takes the user to a form. 
- This form gives the admin the ability to upload more cars into the various categories.
- When the admin navigates to the products page, they have the ability to Edit or Delete a car. 

---

# FLAKE8 ERRORS

Please note that these errors are mostly related to lines being too long, being completely new to Python and Django, I was genuinely fearful of going in and trying to fix these as I was scared about breaking something within the code. Time wasn't on my side ether so apologies for not addressing all of these!

---

# THE FREE THRESHOLD

I wanted to have something whereby if the user bought a car over ???23,000 this would entitled the car buyer to a year free of mechanical services, I was unable to implement this in the way I wanted with time not being on side. So I've chosen to leave this feature out for now. 

---

# CHROME LIGHTHOUSE REPORT

## Lighthouse Test Report (Deployed)
![Lighthouse report](wireframes/lighthouse_report_deployed.png)


## Lighthouse Test Report (Locally)
![Lighthouse report](wireframes/lighthouse_test.png)


## Incognito Lighthouse Test Report (Locally)
![Lighthouse report](wireframes/incog_lighthouse_test.png)

---

# RESPONSIVENESS TESTING

## Navbar Responsiveness

Please note, the website has been tested across multiple devices.

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

## Cart Page

Ensure items on the Cart page displays as intended across devices and laptops.

- The Cart page displays as intended on laptop and larger screens.

![Cart page larger screens](wireframes/cart_items.png)

- The Cart page displays as intended on smaller screens.

![Cart page smaller screens](wireframes/cart_tablet.png)

- The Cart page displays as intended on mobile screens.

![Cart page mobile screens](wireframes/cart_mobile.png)

## Checkout Page

Ensure the Checkout page displays as intended across devices and laptops.

- The Checkout page displays as intended on laptop and larger screens.

![Checkout page larger screens](wireframes/checkout_lg.png)

- The Checkout page displays as intended on smaller screens.

![Checkout page smaller screens](wireframes/checkout_md_ls.png)
![Checkout page smaller screens](wireframes/checkout_md_pr.png)

- The Checkout page displays as intended on mobile screens.

![Cart page mobile screens](wireframes/checkout_sm.png)


## Checkout Success Page

Ensure the Checkout Success page displays as intended across devices and laptops.

- The Checkout Success page displays as intended on laptop and larger screens.

![Checkout success page larger screens](wireframes/order_summary.png)

- The Checkout Success page displays as intended on smaller screens.

![Checkput success page smaller screens](wireframes/checkout_success_tab.png)

- The Checkout Success page displays as intended on mobile screens.

![Checkput success page mobile screens](wireframes/success_mobile.png)


## Sign In Page

Ensure the Sign In page displays as intended across devices and laptops.

- The Sign In page displays as intended on laptop and tablet screens.

![Sign In page larger screens](wireframes/signin_larger.png)

- The Sign In page displays as intended on mobile screens.

![Sign In page mobile screens](wireframes/signin_mobile.png)


## Profile Page

Ensure the Profile page displays as intended across devices and laptops.

- The Profile page displays as intended on laptop and tablet screens.

![Profile page larger screens](wireframes/profile_lg.png)

- The Profile page displays as intended on mobile screens.

![Profile page mobile screens](wireframes/profile_mb.png)

---

# MOBILE DEVICES


The website has been thoroughly tested on:

- iPhone 4, 5SE, 6Plus, X, 11
- iPad, Pro, Mini

- Samsung Galaxy Note 3, Note II, Galaxy S5, Galaxy Fold

---

# DIFFERENT BROWSERS

The website has been thoroughly tested on the following browsers:

- MacBook

    - Safari
    - Chrome
    - Firefox

- Windows HP

    - Edge
    - Chrome
    - Firefox

---

# VALIDATIONS

- CSS Validator - PASSED

- HTML Validator - PASSED

---

# BUGS AND ISSUES


## Problem With Receiving Emails

On the Contact page when a user sent a message through the website, it appeared to being going through fine as they received a success message when they clicked send. The message was also being saved to the contact page on the admin site. However the user never received a confirmation of their email. To understand what was going on, in Heroku I created a variable called DEVELOPMENT and set it to True. I then restarted my app dynos and tried to submit a message. This time, I received the below error:

![Contact error](wireframes/contact_error.png)

For some strange reason, Django was putting in a new line in the subject field. The only fix I could think of was the ```strip()``` function that would help me debug this issue. So in my views.py I applied it to the ```send_mail subject``` which is now working as intended.

https://www.w3schools.com/python/ref_string_strip.asp


## Template Error

When the admin was logged in and when they navigated to the product management page they got the below error and a 500 error on the live site.

![Template error](wireframes/template_error.png)

In my attempt to make python files PEP8 compliant, in my widgets.py, I thought I was doing the right thing by reducing the amount of characters for the ``` template_name ``` by breaking the line up. Took me why too lomg to figure this out!


## Duplicate Orders

When a user purchases a car, the order goes through fine, but when they go to their profile there's a duplicate order. User is only charged for one car.

![dublicate order](wireframes/dublicate_order.png)

In my checkout views.py, I had this line of code twice ```order_form = OrderForm()``` removing the extra code that I had mistakenly added twice, resolved the issue.

Upon further investigation, this proved to be a far more complicate task to resolve. My Stripe Webhooks weren't commuincating with my site so I had to create ```STRIPE_WH_SECRET``` in my Gitpod variables. 


## Issue With The Layout Of The Cart On Mobile 

Although the functions on the cart all worked on mobile devices, the layout wasn't exactly user friendly. 

![bad layout cart](wireframes/bad_cart.png)


So in order to combat this issue, I refactored the code and used a grid. It now looks less cluttered and much more user friendly.

![good layout cart](wireframes/good_cart.png)


## Exposing Sensitive Information

When I was setting up my application in Heroku, I was having issues migrating. I shared these issues in Slack and it was then pointed that I had left my API Key exposed, Debug was set to True and I had also pushed my database to GitHub.

To ammend these vulnerabilities, I set up GitPod variables for the SECRET_KEY and for Debug. Then in my settings.py I added SECRET_KEY = os.environ.get("SECRET_KEY") and DEBUG = os.environ.get("DEBUG") at the end of file. To secure my database, I added it to .gitignore


## Unsupported Operand

Kept on getting unsupported operand type for *: 'NoneType' and 'decimal.Decimal'

![unsupported operand](wireframes/unsupported_operand.png)

- I resolved this bug by changing ``` quantity = int(request.POST.get('quantity')) ``` to ``` quantity = 1 ```

## Footer Issue

Struggling to get the Footer to display at the bottom of the page across the website. Tried numerous different properties and Bootstrap classes for a fix.

![Footer issue](wireframes/footer_issue.png)

- I resolved this issue by changing a couple of conflicting CSS rules.

## 500 Error in Cart

When I tried to remove a car from my cart I kept on getting a 500 error.

![Cart issue](wireframes/cart_issue.png)

- I resolved this bug by adding in this line of code ```request.session['cart'] = cart``` in my views.py

## Invalid Operations

When I created the checkout app, I started to get this error when I ran the server.

![Decimal error](wireframes/decimal_error.png)

- I resolved this error by making amendments to my models.py in the checkout app. I then ran migrations again, which seems to have worked.
