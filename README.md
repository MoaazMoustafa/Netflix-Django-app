# A Movies Blog using Django framework

#### Video Demo: < https://www.youtube.com/watch?v=rXaEs1Drzzc&ab_channel=moaazmoustafa>

#### Description:

This is a Django web application in which the user can register a new account and add new movies to the web app
I used the django built in authentication to authenticate the users and used the django admin panel and customized it
In this project i used django and ORM and DTL and bootstrap
the user can upload poster for there loved movies
I used Django, Postgresql, Bootstrap, ORM, DML.

This project  consits of three apps the first one is the main app which is named Netflix.
The second one is the movies one which consists of the the models it has three models the main one is the Movie and an Actor model and Review model
These models map in the Postgres database as tables thanks to the ORM (object releational mapper)
I used a lot of fields such as char, text, number, image, many to many and Forign key
The third app is the accounts app in which it control the users and there accounts.

I used signals in this app so every time a movie created it sends an email to specific people (but i disabled it for security reasons).


I also customized the admin panel so i divided it into sections and let the admin search by the name of the movie.
One of the most powerful features of the ORM that it secure the app from the SQL injection attack


I used templates inheritance : I created a base_layout in the main templates directory and inhireted from it all the other templates.

There are requirements for this project to run such as django and psycopg2 python library and pillow python library I mentioned all of them in the requirements file
I used postgresql databse for this project and adjust all its configuration in the settings file in the main app which is the netflix app
configuration like the host, port, username and password.

one of the most powerful features of django web framework is the signals. You can adjust a signal for many events like post save , pre save, post delete and much more.

The main feature of this project is the CRUD operation in which the user can Create, Retrive, Update and Delete movies from the blog.
The user can add poster for the movies when he upload them. User can view movies and see all its details such as likes, rating, poster, actors and reviews.
The user can also delete any movie he wants. He also can update whatever movie with whatever details he wants.
Template Inheritance:
● Include → get another template and put it inside the current template.
● extends →get another template defined blocks to be replaced in current.
● block → to define blocks inside template.
Note: include, and extends sees from templates directory So even if the template files are in the same dir
you will need to write the inner folder under templates directory if exists when extends or include.
Template inheritance is a way of organization and re-use of an already existing template in order to
eliminate the code redundancy (a great example of django “DRY”)
