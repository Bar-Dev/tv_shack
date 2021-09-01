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
Once a product is added to the users cart, it will automatically total the price in USD in the top right. When the user clicks the cart it bring them to the full cart display page. This shows what products they have selected, the quantity of each, and the total cost of their items combined.
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


## Technologies
For this project I used the following technologies:

[Github](https://github.com/) - Used for repository hosting service.

[Gitpod](https://gitpod.io/) - an online IDE, used to create and edit the project code.

[Heroku](https://heroku.com) - a Cloud Application Platform that enables developers to build, run, and operate applications entirely in the cloud

[Bootstrap 4](https://getbootstrap.com/) - a CSS Framework for developing responsive and mobile-first websites

[HTML 5](https://en.wikipedia.org/wiki/HTML5) - a markup language used for structuring and presenting content on the World Wide Web

[CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets that describe how HTML elements are to be displayed on screen

[Django]( https://www.djangoproject.com/) – a high-level Python Web framework that encourages rapid development and clean, pragmatic design

[SQlite3]( https://www.sqlite.org/index.html) – database used in development through Django

[PostgreSQL]( https://www.postgresql.org/) – database used in production through Heroku

[Google Fonts]( https://fonts.google.com/) – Used to set the Font Family for the whole site

[FontAwesome](https://www.bootstrapcdn.com/fontawesome/) – used for scalable vector icons

[jQuery](https://jquery.com/) - a JavaScript library that greatly simplifies JavaScript programming

[Slack](https://slack.com/intl/en-ie/) - used by the Code Institute community for open discussions, getting answers and sharing information

[Stackoverflow](https://stackoverflow.com/) - an open community for coders to ask questions and get answers

[W3Schools](https://www.w3schools.com/about/) - for tutorials and references on web development languages

[Free Formatter](https://www.freeformatter.com/javascript-beautifier.html) - a Javascript, HTML and CSS Beautifier.

[W3 Validator](https://validator.w3.org/) - a HTML and CSS Validator.

[PEP8 Online](http://pep8online.com/) - To format all Python code.


## Future Features

**Search Icon** : I did want to expand on this page to allow users see previous searchs they had carried out. This can be something implemented in the future.

**Product Reviews**: Additionally to the site reviews I would like to expend this to have specific product reviews.

**Policies**: legal policies such as Terms & Conditions, Cookies Policy and Privacy Policy to be added to a footer at the bottom.


## Testing

Testing can be found on its own page [here](https://github.com/Bar-Dev/tv_shack/blob/main/TESTING.md)


## Deployment

A live demo can be found [here](https://bar-dev-tv-shack.herokuapp.com/).

The website is hosted using Heroku. It is linked from the master branch of my milestone repository [Bar-Dev TV Shack](https://github.com/Bar-Dev/tv_shack). When new commits are added to the repository, Heroku will rebuild and the site will update with any changes.

**Cloning via Github**:

*	Open the Github Repository link.
*	Click on the 'Clone or Download' button.
*	Copy the URL provided.
*	Open Git Bash terminal.
*	Change the current working directory to the location where you want the cloned directory to be made.
*	Type 'git clone' and paste in the URL.
*	Press Enter.

**Deploying on Heroku**

- Navigate to [Heroku](https://heroku.com).
- Install the Heroku CLI (Command Line Interface)
- Creating an account is required. When at the Heroku dashboard, click the "New" button on top right. A dropdown appears and you now click "Create New app".
- Name your app. **Note app names must be unique**.
- Choose your region.
- On heroku dashboard navigate to "App connected to GitHub" and choose your relevant Github Repository to link to Heroku app.
- Go to your Bash Terminal.
- Login to Heroku using `$ heroku login`
- Create a requirements.txt file: `$ pip3 freeze --local > requirements.txt`.
- Create Procfile: `$ echo web: python manage.py > Procfile` **Note capital "P" in Procfile.
- Create a super user profile with ‘python3 manage.py createsuperuser’.
- Git add, commit and push.
- Again on your Heroku dashboard, find the apps name, click and then go to "settings".
- Navigate to "Config Vars", click "Reveal Vars" and enter the following Vars and their values:
*AWS_ACCESS_KEY_ID
*AWS_SECRET_ACCESS_KEY
*DATABASE_URL
*SECRET_KEY
*STRIPE_PUBLIC_KEY
*STRIPE_SECRET_KEY
*STRIPE_WH_SECRET
*USE_AWS
- Navigate to “Deploy”, click on Enable Automatic Deploy. Then click “Deploy Branch” (ensure master branch selected) for first time only.
- Herokuapp will now build
- Once built successfully, you can click open app in top right.

**Note to make sure site functions correctly, free account for Stripe and AWS with an S3 bucket are required**


## Credits
### Media

The main logo was made with the help of Font Awesome.

The main Hero image was a google search but can be found at the following address [wallpapersafari](https://cdn.wallpapersafari.com/60/83/r0pR5I.jpg)

### Acknowledgements

The Code Institute tutor Chris (ckz8780). For his excellent tutorial video for the Boutique_Ado project. Which a lot of my coding snippets came from and were redesigned by me to fit my project. 

The Code Institute community on Slack. Very helpful with issues and it was good to see I was not alone with the problems I was facing.

Stack Overflow community and threads/ questions that helped me through difficulties with my project.

The Contact Us Tutorials from [Hello Web Books]( https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/) and [OverIQ]( https://overiq.com/django-1-10/building-contact-us-page/)

The Comment Tutorial that I made into my site reviews section from [DjangoCentral]( https://djangocentral.com/creating-comments-system-with-django/)

W3schools for some very helpful tips.

Seun Owonikoko (Mentor) who greatly helped me through this course.


