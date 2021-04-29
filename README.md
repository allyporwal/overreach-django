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

<hr>

### Contents:

1. [User Experience](#User-Experience)
2. [User Stories](#User-Stories)
3. [Technologies Used](#Technologies-used)
4. [Features](#Features)
5. [Testing](#Testing)

<hr>

## User Experience

 - ### Strategy
    The app is designed for keen weightlifters who want a simple and intuitive way of tracking and sharing their workouts and connecting with like-minded individuals. The goal for the owner of the site would be a reliable revenue stream from a happy userbase.

- ### Scope
    Users must be easily able to log a workout, complete with notes, and that data should be quickly accessible to them once they have saved it. Some key statistics from their workouts should be presented to them on their dashboard. They should also be able to see other users' profiles and workouts. Users can comment and/or like other users' workouts. It should be possible to follow specific users. An admin on the site should be easily able to see all relevant user and membership data on the Django-generated admin interface.

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

<hr>

## Features

Current features for the user include:

- User login/registration via email or Google
- Subscription payments through Stripe
- Subscription status and previous/next payment dates can be viewed
- Profile pictures can be uploaded
- Strength training (workout) logging, with a dynamic form that allows logging of a workout of any size
- 

<hr>

## Testing

Extensive testing was carried out on all aspects of the app to ensure that it functions smoothly. 