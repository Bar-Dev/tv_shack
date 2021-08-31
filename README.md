# TV Shack
**Full Stack Frameworks with Django MS4 Project.**

The purpose of this site is to convey the use of a number of different areas within my coding studies. Such as HTML, CSS, Javascript, Python / Django. Using a common model and basing around an online TV store to purvey such areas of the code. From here on down the Readme is treated as in the words of the site developer.

**---- Welcome to TV Shack!! ----**


### User Stories
*As a user I want to:*

**Browse/Payment:**

 * Be able to easily navigate the site
 * Browse all available products
 * View extra information about a particular product
 * Add products to my cart
 * View my cart total at anytime
 * View all items in my cart and total cost in detail
 * Use an user friendly paymnet system 
 * Pay by credit/debit card
 * View different products by category
 * Be able to quick an easily search for a product

**Registering/Login:**

 *	Save my details for future checkouts
 *	Easily register with the site
 *	Easily login

**User Profile:**

 * View my default user details
 * Update these details if necessary
 * View my previous orders/transactions with the site

**Contact:**

 * Easily identify how to contact Administrators if needed
 * Use a simple form to contact the Administrators

**Reviews:**

 * View reviews from previous Users
 * Add my own review to the site


*As a Site Administrator I want to:*
 * View all products easily
 * View all products in an organised fashion
 * Have an edit product function
 * Have a delete product function
 * Have a add product function
 * View all users of the site
 * Remove users if required
 * View all user reviews in Django Admin
 * View all user contact messages in Django Admin

### Scope
The scope for this Milestone project is to develop a site that offers all kinds of Television Products and Monitors. Users should be able to navigate through the site browsing by categories or by the installed search engine. They can add one or multiple products to their cart.

To complete their cart checkout, A visitor will need to register and login as a User. As a user they will be giving a profile page and be able to view previous transactions. Then will also then be able to save their information and previous purchases to review at a later date.

While it is a fully functionable site, it is open to further expansion in the future.


### Skeleton

**Navbar**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/header.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/header.png?raw=true" alt="Navbar" style="max-width:100%;"></a>


**Home Page**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/body.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/body.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Footer**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/footer.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/footer.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Products**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/products.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/products.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Profile**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/profile.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/profile.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Checkout**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/checkout.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/checkout.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Reviews**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/reviews.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/reviews.png?raw=true" alt="Navbar" style="max-width:100%;"></a>

**Add_Review**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/add_review.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/add_review.png?raw=true" alt="Navbar" style="max-width:100%;"></a>


### Structure

#### Navbar
The navbar features the logo of the site name in the middle.. To the right on the navbar are the links to “Account" and "Cart". The “Account” dropdown shows link to reveal “Register“ or “Login“ if not logged in yet. If User is logged in these options are “My Profile” or “Logout“. Additionally, if it is Admin that has logged in the dropdown will feature the “Product Management” link. 
Additionally then on the left is a "Search Bar" this shortens to a "Search Icon" on smaller devices which opens the search bar on the page.
Directly under the navbar is the navigation items for the products. This reduced to a Dropdown Toggle on smaller devices.

#### Hone Logo
By clicking the main logo the user will re-direct to the home page.

#### Homepage
The homepage consists of a main hero image relating to the TV & Film industry and displays an advertisment regarding shipping costs. Inside that is a "SHOP NOW" button which leads you to the products page.

#### Footer
The footer consists of "Contact Us", "Reviews", "Logo" and social media links. Each one brings you to the relevant pages.

#### Products
You can enter the products page by clicking "SHOP NOW" or by selecting "All Products" from the dropdown links in the catagories. The Products page will display all current products of the site. Each product is displayed with an image, price, rating and a short discription.

#### Contact Us Page
If a user has further question for us. They can contact us through the use of the Contact form. This form asks for User’s Name, Email, message Subject and the Message.

#### Reviews Page
From time to time a user may feel like leaving a site review about their experience on the site. This may be what they like, don’t like, suggestions for products etc. All visitors to the site can view this reviews page and read these from newest to oldest. If the visitor to the site is logged in, below the reviews a form for submitting is revealed, containing Name, Email and Message.

#### Cart Page
Once a product is added to the users cart, it will automatically total the price in USD in the top right. When the user clicks the cart it bring them to the full cart display page. This shows what competition entries they have selected, the quantity of each, and the total cost of their items combined.
The user then has the option to return to the other products or continue to the checkout page. They can also Update and Remove items from their cart on this page.
Only if the User has registered and logged in will they be given the checkout option.

#### Checkout page
Once the User is happy to checkout, this page will display a form, which asks for the users personal information. Underneath the details form is a checkbox asking the user if they would like their details saved for future use.
At the bottom there is also a field for the user to input their card details and then checkout.
To the right there is a summary of what the User has added to their cart so they can check one last time that they have added the right products and quantities.

#### Confirmation Page
If the User credentials are valid in the checkout form, they will they be directed to the confirmation page, thanking them for their order. It also informs them that they will receive a confirmation mail soon.

#### Profile Page
A register user can access their details under the account menu. This page gives the user a details form (pre-filled if checkbox is selected on checkout page). The User can edit and update these details using this form.
To the left of the form is an order history display. Here previous orders made by the user are displayed, showing order number, order date, products and quantities of each and finally a total for the order.

#### Add product page
If the user is a site Admin, they have the option under account of adding new products. A form is displayed which requires the standard product details. There is then the option for the admin to either enter a URL for the image of the products or to upload their own.

#### Edit product page
As an Admin, the user has extra options on the products page. They can edit or delete that particular product. If they choose edit, this will open a similar page to the add products page but all form details will be pre-filled. They then make their alterations and update the product.


### Surface
The colour scheme for this project uses colours with a unique contrast to each other. The navbar colouring remains consistant throughout all pages. Colours used in the site where as below:

<a target="_blank" rel="noopener noreferrer" href="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/colours.png?raw=true"><img src="https://github.com/Bar-Dev/tv_shack/blob/main/static/wireframes/colours.png?raw=true" alt="Colours" style="max-width:100%;"></a>