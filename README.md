# **Gift Nook**
![Gift Nook website in various devices](readme-testing-files/readme/main-image.png "Gift Nook website in various devices")  

[View the live website here](https://gift-nook-cae3a727fe6e.herokuapp.com/)

</br>  

Welcome to the Gift Nook website!
Gift Nook is an e-commerce website that sells bespoke gifts (handmade and personalised). It features an authentication functionality powered by Allauth and a payment functionality powered by Stripe.  These allow users to purchase products safely and securely via the website.  

Please note that this website is created for Milestone Project 4 in Code Institute's Diploma in Full Stack Software Development. The requirements are to produce a full-stack website, using HTML, CSS, JavaScript, Django+Python, relational database, stripe payments, and other additional libraries as needed. 

<br/>  

## **Table of Contents** 
---------

<br/>  

## **UX DEVELOPMENT PLANE**   
### **A. Strategy Plane**  
#### **Project Goals**   
The primary goal of this project is to create an e-commerce website that a fully-functioning e-commerce platform that is visually pleasing and intuative to a first-time user. The website has basic functionalities that are expected in an e-commerce website (such as sign up/login, ability to purchase items, and payments transactions), but also to ensure that users have a great experience and interaction within the site through additional functionalities such as writing product reviews and reading blogs.

#### **User Goals**  
The user is looking for:
- An online store/ website that is straightforward and intuitive to use, easy to navigate whilst purchasing products. 
- An online store/ website which has additional activities and engagement whilst browsing prodcuts.  

The target user for this site is:
- Young adults, between 18 - 40
- Thoughful, sentimental people
- People who enjoy the convenience of using technology and social media


#### **Site Owner Goals**  
The site owner is looking to:
- Make money by providing products (and services) to the users. 
- Manage products on the website.

#### **User Stories** 
As a shopper I want to be able to:  
   1. Quickly identify what products/services the site sells.  
   2. Quickly identify shipping costs.   
   3. Search for a product.   
   4. Identify a glimpse of the most popular products.   
   5. View all products, and easily navigate between categories.  
   6. Sort products by price.  
   7. View the individual product's page and read the relevant information.  
   8. Read a product's review.  
   9. Easily add products to a shopping bag.
   10. View the shopping bag with products added to it.  
   11. Manage the shopping bag by removing unwanted products.  
   12. Check out and easily enter my payment information.  
   13. Feel my personal and payment information is safe and secure.  
   14. View an order confirmation after purchasing.  
   15. Receive an email confirmation after purchase.  
   16. Read relevant articles/ blogs.   
   17. Easily navigate within the site, through Navigation Bar and Footer.  
   18. Easily register for an account.  
   19. Find the FAQ section for my questions.  
   20. Contact the shop via a contact form.     

As a registered user/ shopper, I want to be able to:
   1. Access all functionalities that an unregistered shopper can do.  
   2. Easily log in or log out.   
   3. Easily recover my password if forgotten.  
   4. Receive an email confirmation after registering.  
   5. Have a personalized user profile where I can see my order history and change my information.  
   6. Review products that I have purchased before.  
   7. Edit and delete my reviews.  
   8. Add products to the wishlist, so I can quickly find products I'd like to purchase. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   9. Remove products from the wishlist, so I can remove products I don't wish to purchase.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   10. Easily put the wishlist products into the shopping bag.   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

As an admin and store management, I want to be able to:
   1. Add a product.  
   2. Edit or update a product.  
   3. Delete a product.  

[Back to top &uarr;](https://github.com/lisaloudness/gift_nook)  

<br/>

### **B. Scope Plane**  
Based on all goals and user stories, a scope was defined for the site with room for future improvements.  

#### **Functional Requirements**   
The unregistered users will be able to:  
- Sign up to the site by providing the username, email, and password.    
- View all products and sort them by price.  
- Search for products.  
- View the product's detail.  
- Add products to the shopping bag.  
- Update and remove items in the shopping bag.  
- Checkout and make a payment.  
- Receive an email confirmation of the transaction.    

The registered users will be able to:  
- Do all things that unregistered users are able to do.   
- Log in to the site by providing a username and password.  
- View the profile page.  
- Update delivery/contact information on their profile page.  
- View order history on their profile page.  
- Write reviews for products that they have purchased.  
- Edit those reviews.  
- Delete those reviews.  
- Add products to their wishlist.  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Remove products from the wishlist.  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 

The admin/ site owners will be able to:
- Have all functionalities as a registered user.  
- Add a product to the site.  
- Edit or update a product.  
- Delete a product.  

#### **Non-functional Requirements**  
Users will be able to:  
- View articles/ blogs about gifts and occasions.  
- View the FAQ page to find answers to their questions.  
- Send a message to the store via contact form.  
- Navigate easily and intuitively throughout the site.  

<br/>  

### **C. Structure Plane**  
The website was organized in a Hierarchical Tree Structure that ensures the user can navigate easily and intuitively. Below is the website workflow (which was designed using [Creately](https://creately.com/)).  

![The website's structure](readme-testing-files/readme/structure.png "The website's structure")   
There's a clear page access separation between unregistered users and registered users. While unregistered users can still purchase products and receive the confirmation via email, they are not able to:  
- View their order history  
- Give reviews (and edit or delete their reviews accordingly)  
- Make a favorite list of products.  XXXXXXXXXXXXXXXXXXXXX

Those features mentioned are available for registered users.  

[Back to top &uarr;](https://github.com/lisaloudness/gift_nook)  

<br/>  


