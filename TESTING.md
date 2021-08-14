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