## Testing
For testing I broke each page out on its own, and made sure each component of that page did what it was required to. The following are the tests that I conducted:

### Navbar (from base.html)
- TV Shack logo tested to direct to homepage.
- Tested toggler icon drops down to display navlinks.
- Test all navlinks to direct to appropriate pages.
- When not logged in test account button drops down to display “Register” & “Login”.
- When logged in as standard User, test account drops down to display “My Profile” & “Logout”.
- When logged in as Admin(superuser), test account drops down to display “Product Management”, “My Profile” & “Logout”.
- Test “Register” and “Login” directs to correct pages.
- Test “Product Management”, “My Profile” & “Logout” option direct to appropriate pages.
- Test empty cart brings you to “Cart empty” page.
- Add items to cart and ensure total accumulates correctly.
- Test Search bar decreases to logo on smaller devices.
- Test all category dropdowns show and link to correct pages.
- All links change color on hover.

### Homepage (index.html)
- Large image shown correctly on desktop.
- Small advertisment in middle of image shows.
- Colour scheme correct.
- "SHOP NOW" button links to All Products page.
- All Products link directing to Products page.
- All links change color on hover.

### Products (products.html, product_detail.html, add_product.html, edit_product.html)
- All Products link displays all productss page.
- Product cards have same attributes throughout.
- Card link directs to correct Product details page.
- Individual product info displayed correctly.
- Quantity selector operating as it should.
- Add to cart button adds correct quantity and cart icon updates total amount.
- Description tab and details tabs display their information when clicked.
- If Admin is logged in, “Edit” & “Delete” options are available.
- Delete button correctly deletes product. (checked Django admin to confirm).
- Edit button directs to edit products form.
- Form fields are populated with current product information.
- Updated information in each field separately and tested. All updated correct. Successful toast is displayed.
- Successful update redirects to that product details page.
- Change product image. Updates correctly. Successful toast is displayed.
- Drop down link in “Accounts” displays “New Product” form, when “Product Management” is clicked.
- New competition fields are marked as required with an asterix.
- Test that no individual field can be left blank, including image upload.
- Check price cannot be more than 8 digits and that an error is displayed under field. Error toast also displays. 

### Reviews (reviews.html)
- Reviews link renders reviews page.
- All reviews are displayed correctly with correct CSS styling.
- If not logged in, reviews are visible.
- If a User is logged in, the form for adding a review is displayed.
- Check all fields are required.
- Check email address is valid format.
- After submitting form, reviews page refreshes displaying new review.
- Check Django Admin to confirm review is stored.

### Contact Us (contact.html)
- Contact Us link renders contact page.
- Form is displayed correctly with correct CSS styling.
- Contact form available for all Users.
- Check all fields are required, exception is the “Subject” field.
- Check email address is valid format.
- After submitting form, redirect to Homepage.
- Toasts information message displayed.
- Check Django Admin to confirm contact message is stored.

### Cart(cart.html)
- Test empty cart brings you to “Cart empty” page.
- With items in cart test cart table is displayed correctly.
- Test “Continue to Products” button directs to Competitions page.
- Test “Sign in” link directs to sign in page.
- If User is logged in, “Continue to Products” and “Checkout” options are displayed.
- Test “Continue to Products” button directs to Products page.
- Test “Checkout” button directs to checkout page.

### Checkout(checkout.html, checkout_success.html)
- Test checkout page displays correctly with correct CSS.
- Check User’s information is pre-populated from profile (if User has filled in previously).
- Confirm cart snippet on right displays accurate information to what was in cart on previous page.
- Check all fields are required, exceptions are “County”, “Address 2” and “Postcode” fields.
- Check email address is valid format.
- Test on New User that “save information” button saves profile information correctly.
- Use Stripe test credit card details “card number - 4242 4242 4242 4242”, “Expiry Date – 0424” & “CCV – 424”. These allow for a test payment.
- Check my own Stripe profile to confirm payment was successful.
- Check invalid card number displays error.
- Check invalid Expiry Date displays error.
- Test “Pay Now” button submits form correctly. Success toast displays.
- Test that User is directed to payment successful page.
- Test “Continue to Products” button directs to Products page.

### Allauth pages
- Test “Register”, “Login” & “Forgot Password”  pages display correctly. Check that these pages inherit typical CSS styling of the rest of the site.
- Check all fields are required on “Register” page.
- Check email addresses must match email repeat field.
- Test email not in use already is valid.
- Check email address is valid format.
- Check Username must be minimum 4 characters
- Check password must be minimum 8 characters.
- Check password in not too common.
- Test “Sign Up” button redirects to homepage and logs new User in. Check successful toast displays.
- Check invalid details shows error on “Login” page.
- Test “Login” button redirects to homepage and logs User in. Check successful toast displays.

### Footer
- Test link to Contact Us page works.
- Test link to Reviews page works.
- Test link to Facebook page works.
- Test link to Instagram page works.