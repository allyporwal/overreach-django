# OVERREACH

## Full Stack Frameworks With Django Milestone Project

<hr>

Welcome to Overreach.

Overreach is a web app that is intended to serve two main purposes:

1. Give users a place to log their strength training workouts
2. Serve as a place that users can connect with other strength training enthusiasts

The app was deployed using Heroku and can be found here: [Overreach](https://overreach.herokuapp.com)

This is my final milestone project for the Code Institute Diploma in Full Stack Software Development. In a nutshell, the goal of this milestone project is to design a full stack web application with a relational data model, business logic, user authentication and full CRUD functionality for the users.

It will be something I continue working on as a hobby/passion project (in a cloned repository) after submitting to further develop my skills in full stack software development.

As an aisde, the name Overreach comes from a term often used in strength training. A brief period of training where a trainee "overreaches" or an "overreaching" phase are key to making good progress in the gym and busting through plateaus in strength, power or size. The logo is designed to hint at the idea of reaching up and beyond.

<hr>

### Contents:

1. [User Experience](#User-Experience)
2. [User Stories](#User-Stories)
3. [Technologies Used](#Technologies-used)
4. [Features](#Features)
5. [Testing and Validation](#Testing-and-validation)
6. [Deployment](#Deployment)

<hr>

## User Experience

 - ### Strategy
    The app is designed for keen weightlifters who want a simple and intuitive way of tracking and sharing their workouts and connecting with like-minded individuals. The goal for the owner of the site would be a reliable revenue stream from a happy userbase.

- ### Scope
    Users must be easily able to log a workout, complete with notes, and that data should be quickly accessible to them once they have saved it. Some key statistics from their workouts should be presented to them on their dashboard. They should also be able to see other users' profiles and workouts. Users can interact with other users. It should be possible to follow specific users. An admin on the site should be easily able to see all relevant user and membership data on the Django-generated admin interface.

- ### Structure
    Everything most relevant to the user must be available in one click/tap from their dashboard once they are logged in. A user needs only click once to see a detailed feed of friends' workouts, begin logging a workout, edit profile information, see a basic feed of all users' workouts or sign out. 

- ### Skeleton
    A grid system is used to ensure clean presentation of all data on all pages to the user. Extensive use of card components from Bootstrap 4.6 was key to achieving this. Wireframes were drawn out in Balsamiq to assist in the design process, although the final app does differ slightly. The design was primarily done for use on mobile devices but it performs well on desktop or tablet devices as well.

    1. Dashboard template
        - [desktop](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/dashboard_desktop.png)
        - [mobile](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/dashboard_mobile.png)

    2. Log workout template
        - [desktop](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/log_workout_desktop.png)
        - [mobile](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/log_workout_mobile.png)
    
    3. Display individual workout template
        - [desktop](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/workout_desktop.png)
        - [mobile](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/workout_mobile.png)

    4. Friends template 
        - [desktop](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/friends_desktop.png)
        - [mobile](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/friends_mobile.png)

    5. Everyone's workouts template
        - [desktop](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/everyone_desktop.png)
        - [mobile](https://github.com/allyporwal/full-stack-frameworks/blob/master/wireframes/everyone_mobile.png)

- ### Surface
    The main colour of the logo is used as the dominant colour for elements of the surface design that need accenting. Complimentary colours are used to ensure a harmonious look across the website. [Monteserrat](https://fonts.google.com/specimen/Montserrat) was the font chosen for a close match with the logo.

[Back to top](#contents)

<hr>

## User Stories

Careful attention was put into fully realising the following user stories. As a user, I want to:

- create an account with email/Google login and set up a membership using Stripe within a couple of minutes
- easily edit my profile information
- see my membership payment dates
- cancel my membership
- log workouts in an intuitive way and save notes with them
- see my workout data presented in a way that helps me train better in the future
- access any recent workout quickly
- see workouts posted by other users
- like workouts posted by other users
- comment on workouts posted by other users
- follow other users who interest me
- view the workouts of users I follow in a detailed feed

As an admin user, I want to:

- have access on the admin panel to all users' profile information
- see users' membership payment dates and status
- see comments left on workouts so they can be deleted if necessary

[Back to top](#contents)

<hr>

## Technologies Used

This project uses the following languages:

- HTML
- CSS
- Javascript
- Python

The project uses the following technologies and frameworks:

- [Bootstrap 4.6](https://getbootstrap.com/) was used for the key layout components
- [jQuery](https://api.jquery.com/) was used to enable responsive behaviour on forms and other elements
- [chart.js](https://chart.js/) is used to graph key data on a user's dashboard
- [Django](https://djangoproject.com/) is the Python framework the backend code uses
- [Heroku](https://heroku.com/) is the cloud-hosting service the app is hosted by
- [PostgreSQL](https://www.postgresql.org/) is the database used, provided by Heroku
- [SQLite3](https://www.sqlite.org/index.html/) was used for data storage in development
- [Amazon S3](https://aws.amazon.com/s3/) is used for CSS and media storage
- [Google OAuth](https://developers.google.com/identity/protocols/oauth2/) is used to enable login/registration with a Google account
- [Gitpod](https://gitpod.io) was the IDE used for writing all code
- [Stripe](https://stripe.com) provides the technology for processing payments
- [Font Awesome](https://fontawesome.com) is the source of all icons
- [dbdiagram.io](https://dbdiagram.io/) was used to plan the relational database models
- [Balsamiq](https://balsamiq.cloud) was used to sketch the wireframes
- [Gmail](https://mail.google.com) is used to send emails to users

The following libraries/packages listed below are also used:

- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) ensures that the app works with Amazon S3
- [dj-database-url](https://pypi.org/project/dj-database-url/) allows the app to work with PostgreSQL
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used for all user authentication
- [django-countries](https://pypi.org/project/django-countries/) is for the country field in the profile form
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) ensures that all Django forms are rendered with Bootstrap styling
- [django-storages](https://django-storages.readthedocs.io/en/latest/index.html) gives the functionality in a custom storage class needed to connect to S3
- [gunicorn](https://gunicorn.org/) is the WSGI server that runs the Python app
- [oauthlib](https://pypi.org/project/oauthlib/) ensures the Google OAuth integration works with Allauth
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image handling on forms
- [psycopg2-binary](https://pypi.org/project/psycopg2/) is the PostgreSQL database adapter for Python

[Back to top](#contents)

<hr>

## Features

Current features for the user include:

- User login/registration via email or Google
- Subscription payments through Stripe
- Subscription status and previous/next payment dates can be viewed
- Subscriptions can be cancelled
- Profile pictures can be uploaded
- Strength training (workout) logging, with a dynamic form that allows logging of a workout of any size
- A rest timer for timing rests between sets in a workout
- Existing workouts can be edited
- Access to all previously logged workouts
- Access to all other users' previously logged workouts
- Display of key workout data on dashboard
- The ability to like and comment on workouts
- Other users can be followed and their activity viewed on a friends feed
- Other users' profiles can be viewed, with a link to their workouts

Future user features will include:

- A more detailed dashboard displaying a greater variety of data
- Greater flexibility in the dashboard, allowing a user to choose what data they see and/or how it is presented
- Groups to allow discussion of all weight-training related matters
- Allowing a user to update card details rather than having to re-subscribe

Current admin features include:

- All workouts and comments are visible from the admin section
- All user profiles and the most important subscription information is visible as well

A key future admin feature will be:

- Automatic cancelling of a user's access to the service on the correct date once they cancel their subscription

Currently any cancelled subscriptions are visible to the admin as "Cancelled sub_id", allowing an admin user to see that and cancel the user's access. However, if the site were busy, this would need to be checked every day to ensure that there weren't people who had cancelled their subscription but still using the service.

[Back to top](#contents)

<hr>

## Testing and Validation

Extensive testing was carried out on all aspects of the app to ensure that it functions smoothly. 

All HTML was checked using the [W3](https://validator.w3.org/#validate_by_input) validator. There is one small issue outstanding with the Bootstrap navbar component. Specifically, as documented in this [Stack Overflow thread](https://stackoverflow.com/questions/24961294/bootstrap-navbar-not-working-on-ipad), leaving out the ```href="#"``` attribute appears to sometimes cause problems. As such, this has been left in. Without it, the navbar dropdown was almost invisible and completely unusable. This was the only solution I tried and it functions as intended, but just unfortunately throws the error on W3C.

All CSS was checked on [W3C] and passed without errors. All JS was tested on [Esprima](https://esprima.org/demo/validate.html) and was syntactically valid.

All Python code was checked in Gitpod with [cornflakes-linter](https://marketplace.visualstudio.com/items?itemName=kevinglasson.cornflakes-linter) and any errors in code that I had written was corrected. 

During development each feature was tested to ensure that an average user cannot break the site and to check that all pages and features worked as intended on multiple devices.

[Back to top](#contents)

<hr>

## Deployment

The project was created in Gitpod and the repository is stored at Github. If you would like to clone the project to run locally on your machine, please follow the steps below:

1. Going to the repository on Github
2. Clicking on the "Code" button at the top right
3. The link to be copied will then be displayed
4. In your IDE, ensure you are in the correct directory and then type "git clone" followed by pasting the link
5. The repository will then be cloned into your chosen directory

Once you have the cloned repository ready to go, there are a few more steps to take that are crucial to getting it running locally:

1. Install all the project's dependencies with the command: ```pip3 install -r requirements.txt```
2. Create a file called ```env.py``` - then ```import os``` at the top and add the following variables to it:
    ```python
    os.environ.setdefault("SECRET_KEY", "your_django_secret_key")
    os.environ.setdefault("STRIPE_SECRET_KEY", "your_stripe_secret_key")
    os.environ.setdefault("STRIPE_PUBLIC_KEY", "your_stripe_public_key")
    os.environ.setdefault("STRIPE_WH_SECRET", "your_stripe_webhook_secret")
    ```
3. Ensure that these variables are properly referenced in your project level ```settings.py``` file
4. At this step you can also create a couple of other commented out variables in ```env.py``` for later on that are necessary to deploy the project: 
    ```python
    os.environ.setdefault("DATABASE_URL", "for_your_postgres_database")
    os.environ.setdefault("AWS_ACCESS_KEY_ID", "for_your_amazon_aws_access_key_id")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "for_your_amazon_secret_access_key")
    ```
5. Ensure that your ```env.py``` file is in your ```.gitignore``` file so no secret keys are exposed

Now you'll need to make sure that the database files are ready by using the following commands (**in the order listed below**) in the terminal:

1. ```python3 manage.py makemigrations```
2. ```python3 manage.py migrate```

The app is nearly good to run locally. Next create a superuser so you can log into the admin section with ```python3 manage.py createsuperuser``` and finally start the server with ```python3 manage.py runserver```

If Port 8000 is running you should be able to launch the app in your browser. Be sure to make the port public if you want to start testing Stripe Webhooks.

To get the app deployed to Heroku, I took the following steps:

1. Navigated to [Heroku](https://heroku.com/) and signed in
2. Created an app by clicking New in the top right and then create new app
3. Named the app and select the region closest to you
4. In the Resources tab, selected Heroku Postgres and chose a plan
5. Ensured that dj_database_url is installed by typing ```pip3 install dj_database_url``` in the terminal
6. Also installed ```pip3 install psycopg2-binary```
7. Froze all the requirements with ```pip freeze > requirements.txt```
8. Navigated to the Settings tab on the Heroku site for the app, clicked on Reveal Config Vars and copied the ```DATABASE_URL``` value
9. Pasted the url from step 8 into the ```os.environ.setdefault("DATABASE_URL", "url_pasted_here")``` in my ```env.py``` file
10. Dumped all my test data I had input (users, workouts, and pictures) into a json file with a command in the terminal: ```./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json```
12. Updated my ```settings.py``` file by commenting out the ```DATABASES``` section and adding the following block of code - 
    ```
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
    ```
12. In the terminal, I ran ```python3 manage.py migrate```
13. Uploaded the json file from step 10 to the Postgres database with ```./manage.py loaddata db.json```
14. Created another superuser so I could log in - ```python3 manage.py createsuperuser```
15. Installed Gunicorn to act as the web server - ```pip3 install gunicorn``` and repeated step 7
16. Created the Procfile to ensure that Heroku could create a web dyno to serve the app
17. Temporarily disabled collect static with the terminal command ```heroku config:set DISABLE_COLLECTSTATIC=1 --app overreach``` - this appeared in the Heroku Config Vars
18. Added the hostname of the Heroku app to ```ALLOWED_HOSTS``` in ```settings.py```
19. Pushed the repository to Github
20. Navigated to the Deploy tab in Heroku and selected Connect to Github
21. Enabled automatic deploys from the master branch of the repository

After the above steps I needed to get Amazon S3 set up to store static files and images. This is the process I followed:

1. Created an account on [Amazon AWS](http://aws.amazon.com/)
2. Searched the services available for [S3](https://s3.console.aws.amazon.com/)
3. Created a new bucket that was set to be public
4. Turned on static website hosting for that bucket
5. Input the required CORS configuration - 
    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
6. Created a bucket policy with the generator provided by S3 and pasted it into the bucket policy editor
7. Ensured that there was access to all objects for everyone in the public access section
8. Navigated to Amazon's Identity and Access Management
9. Created a Group for management of the Overreach app and a pre-built AWS policy for that group
10. Pasted the ARN from the Amazon bucket into the Group policy to allow that group access
11. Asigned the correct Group policy to the Overreach management Group
12. Created a user for the Group and gave that user full access
13. Downloaded the CSV file containing the Access Key ID and Secret Access Key
14. Saved the keys from step 13 to my ```env.py``` file and Heroku Config Vars and also added another varible in Heroku only - ```USE_AWS``` set to ```True```
15. Removed the ```DISABLE_COLLECTSTATIC``` variable from Heroku Config Vars
16. In the terminal of my workspace, I installed boto3 and django-storages
17. I also added the following block of code to ```settings.py``` -- 
    ```python
    if 'USE_AWS' in os.environ:

    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'overreach'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
    -- this was to ensure that in production, Django would upload all the static files to S3 as well as cache the static files for faster performance for the user
18. Created ```custom_storages.py``` and used the classes from django-storage 
19. Commited all the changes and pushed to Github - Heroku then built the app and everything from ```/static``` was uploaded successfully to S3

The final key step in deployment was to ensure that users could receive emails for various notifications regarding signing up, payment and membership cancellations.

The ```webhook_handler.py``` file in the memberships app takes care of this, but the following lines below were added to the ```settings.py``` file:

```python
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'hello@overreach.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = 'hello@overreach.com'
```

In Gmail, I created an app password for the Django app and input the 16 digit password into the Heroku Config Vars with the name ```EMAIL_HOST_PASS```, corresponding to the clip from ```settings.py``` above. Also, in Heroku, ```EMAIL_HOST_USER``` was set as my own email address in Config Vars.

