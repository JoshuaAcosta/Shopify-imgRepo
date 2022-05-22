# Shopify-imgRepo

## Scope of work
As part of Shopify's Data Engineering Technical Challange, we were tasked with building an image repository. <br />
For this project, a web app was developed for users to be able to upload images from their local computer up to an AWS S3 instance for storage. The actual image file is stored in an AWS S3 bucket under a directory named after their user's id and the image file name and file location are stored in a local Postgresql database.

<br />

## Local Setup
Complete the following tasks to run the application on your local system:

1. Clone repo 
2. Create database 
3. Create AWS S3 bucket
4. Setup the following .env variables 
    - FLASK_APP
    - FLASK_ENV
    - SECRET_KEY
    - DATABASE_URL
    - AWS_BUCKETNAME
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
5. activate virtual environment via pipenv shell
6. install all libraries in Pipfile 
7. In the Terminal, run 'Flask run'
8. On your browser, go to localhost:5000 and you'll visit the landing page.

<br />

## Screenshots of application

### Landing Page
![image info](/Shopify_imgRepo/static/img/screenshots/landing_page_view.png)
<br />

### Registration Page
![image info](Shopify_imgRepo/static/img/screenshots/registration_view.png)
<br />

### Login Page
![image info](/Shopify_imgRepo/static/img/screenshots/login_view.png)
<br />

### Gallery View Before Upload
![image info](/Shopify_imgRepo/static/img/screenshots/gallery_view_beforeupload.png)
<br />

### Gallery View After Upload
![image info](/Shopify_imgRepo/static/img/screenshots/gallery_view_afterupload.png)
<br />

## Instructions
1. After landing on the main page, register for a new account if you're a new user. You'll need to enter your
first and last name along with an email address and a 16 character passphrase including numbers and special characters.
2. If you're already a registered user, log in using your email and passphrase.
3. Once you're logged in, any images you've already uploaded will generate in your gallery.
4. Click "Choose File" to select the image saved locally on your computer.
5. Click upload to save the file to the cloud and view it in your gallery below.

<br />

## Possible updates in future

As this was a brief techincal challenge for Shopify, features and functionality were minimal. Given more time,
the following ideas can be implemented:

- expand data model to include more details/metadata about the image
- expand testing suite
- Ability to bulk upload/export images
- Ability to delete images by clicking a button
- Set images to default (images are currently public by default)
- Apply tags to images to improve search capabilities
- Mint images as NFT and sell on OpenSea or another NFT marketplace