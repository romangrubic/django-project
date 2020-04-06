## Full Stack Frameworks with Django Project - Code Institute
---
# Star Trek
Do you like Star Trek? Are you looking for a community of people who like Star Trek franchise as much as you? Then join our community! We have 
news from Star Trek franchise and Federation itself! You can find nice goodies for you or friends in our store. Yes, of course we have Raktajino mugs.
Or just join for discussion about everything Star Trek in our Forum where you can chat with other Trekkies. Live long and prosper!


#### Click on the link to see live demo!
[Star Trek project](https://star-trek-by-romangrubic.herokuapp.com/)

---
## Summary
* [Project Background](#project-background)
* [Technologies used](#technologies-used)
* [Deployment](#deployment)
    * [AWS S3](#aws-deployment)
    * [Heroku](#heroku-deployment)
    * [Local deployment](#local-deployment)


---
## Project Background

Welcome to my Full Stack Frameworks with Django Project for Code Institute. 

The goal of this project was to allow the user to create an account and make a purchase of product/membership with Stripe. Database used is a SQL database PostgresSQL.

I am a big Star Trek fan so for my last project with Code Institute, I decided to make a Star Trek web-site, where beside creating account and purchasing a product via Stripe, 
user can also read news from Star Trek franchise, find games about Star Trek and join discussions about Star Trek in a discussion forum. Users can also chat via private
messaging system and edit their profiles so beside this project being a web-shop, it is also a form of social network for people who like Star Trek.

[Back to top](#summary)

[![Build Status](https://travis-ci.org/romangrubic/Star-Trek-Django.svg?branch=master)](https://travis-ci.org/romangrubic/Star-Trek-Django)

---
## Technologies Used 
The website is designed using following technologies:

### Programming languages
-	**HTML** - the project used HTML to define structure and layout of the web page;
-	**CSS** - the project used CSS stylesheets to specify style of the web document elements;
-	**JavaScript** - the project used JavaScript to implement Stripe, EmailJS and custom Javascript.
-	**Python** - the project back-end functions are written using Python.

### Libraries
-	**[Font Awesome](https://fontawesome.com/v4.7.0/)** - Font Awesome icons were used throughout the web-site.

-	**[jQuery](https://code.jquery.com/jquery-3.4.1.min.js)** - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation.

### Frameworks & Extensions
-	**[Django]( https://www.djangoproject.com/)** – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 

-	**[Bootstrap](https://getbootstrap.com/)** – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.

-	**[EmailJS](https://www.emailjs.com/)** – Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, 
create an email template, and use their Javascript library to trigger an email.


### Database
-	**[Heroku Postgres](https://www.heroku.com/postgres/)** – PostgreSQL is one of the world's most popular relational database management systems.

### Others
-	**[GitHub](https://github.com/)** - GitHub is a global company that provides hosting for software development version control using Git.

-	**[Gitpod](www.gitpod.io)** - One-click ready-to-code development environments for GitHub.

-	**[Heroku](www.heroku.com)** - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.

-	**[Travis-CI](https://travis-ci.org/)** – Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub. 

-	**[AWS-S3](https://aws.amazon.com/s3/)** – Object storage service that offers industry-leading scalability, data availability, security, and performance.

[Back to top](#summary)

---
## Deployment

### AWS Deployment

Created a new Amazon account and connect to amazon service AWS3 account are cloud based serve where the project media and staicfiles will be stored unto.
 At first, we locate S3 on amazon service then we create a bucket. While creating the bucket on S3, the note that public access must be all switched off to allow 
 access for users.

Once we've created the bucket, we now can now click on it's properties and enable the Static Website Hosting option, so it can serve the purpose of hosting our 
static files, you will need to imput an `index.html` and `error.html` before saving. Then we go into the created bucket Permissions and click into CORS configuration, 
this part already have a prefilled default config, All that is needed is just to write the default code and save the config.

Then we go into the bucket policy to allows access to the contents across all web and inside this we will put in here some code including arn address displayed at 
the top of the heading. Then we go into amazon IAM to allow identity and access management of our stored files and folder. In the IAM service, we add a new group 
for our application and then we set the policies to ALL Then it generates a downlaodable zip file containing ID and KEY for us to use for the newly added group. 
This ID and KEY as to be stored in an environment variable.

This then allows us to into our terminal window and install some settings Boto3 Django Storages

The Django Storages is passed into the installed apps in settings and also a custom_storage file is created to store credentials in environment variable. And once 
everything looks fine we can run `python3 manage.py collectstatic`. This will collect all the static files in our app including any changes that is made. N.B this 
command has to be run in the development(local) environment each time a change is been made in the static files/folder And your folder and files should display in 
your AWS S3 BUCKETS


### Heroku deployment

The site is hosted through Heroku and is synced to the master branch of the Git repository. 
This means that the latest push to the heroku branch will update the live site automatically.       

The process for initial deployment is as follows -      
- 1. Log into Heroku dashboard and select "Create new app" from teh dropdown menu located on the top right.     
- 2. Enter a name for the app, select a region where you would like your app to be hosted & click the "Create app" button.        
- 3. In the app dashboard, click on settings. Under "Config Vars", click "Reveal Config Vars" and set the variables in Heroku as they are in you env.py file:
- 4. Type in your local terminal: `$ heroku login -i` and once you are logged in, create a requirements file `$ pip3 freeze -- local > requirements.txt`
and create a Procfile for Heroku by typing `echo web: gunicorn <YOUR_PROJECT_NAME>.wsgi:application > Procfile`
- 5. Go back to Heroku, and at Django `Settings` copy `https://<app_name>.herokuapp.com/` 
- 6. Go to Heroku and connect it to GitHub repository so that will automatically update itself after each push. You can also click to wait for CI to pass before pushing 
if you are using Travis CI or any CI
- 7. Once the build is complete, go back to Heroku and click on `Open App`


### Local deployment

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/romangrubic/Star-Trek-Django.git` 
into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to top](#summary)

---