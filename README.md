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
2. [Technologies Used](#Technologies-used)

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

- [Bootstrap 4.6]() was used for the key layout components
- [jQuery]() was used to enable responsive behaviour on forms and other elements
- [chart.js]() is used to graph key data on a user's dashboard
- [Django]() is the Python framework the backend code uses
- [Heroku]() is the cloud-hosting service the app is hosted by
- [PostgreSQL]() is the database used, provided by Heroku
- [SQLite3]() was used for data storage in development
- [Amazon S3]() is used for CSS and media storage
- [Google OAuth]() is used to enable login/registration with a Google account
- [Gitpod]() was the IDE used for writing all code
- [Stripe]() provides the technology for processing payments
- [Font Awesome]() is the source of all icons
- [dbdiagram.io](https://dbdiagram.io/) was used to plan the relational database models
- [Balsamiq](https://balsamiq.cloud) was used to sketch the wireframes

The following libraries/packages listed below are also used:

- [boto3]()
- [botocore]()
- [dj-database-url]()
- [django-allauth]()
- [django-countries]()
- [django-crispy-forms]()
- [django-storages]()
- [gunicorn]()
- [oauthlib]()
- [Pillow]() for image handling on forms
- [psycopg2-binary]()

