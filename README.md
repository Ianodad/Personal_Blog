# [Gamer Blog](https://)
## Gamers blog help update gamers on latest new of games
### Sep 14th, 2018
#### By **[Ian Odhiambo](https://github.com/ianodad)**

## Description
This is a web application blog meant for game enthusiasts who seek the latest news on games and settings. Users can subscribe to the blog to get the latest updates on articles.

The blog supports comments from readers and blog writer can determine whether to delete the comments or not. 


## Specifications
Check SPEC.md for specs

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

Install [Postgres](https://www.postgresql.org/download/)
### Create a Virtual Environment
Run the following commands in the same terminal:
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
 -pip install python3.6
 -pip install flask
 -pip install flask-SQLAlchemy
 -pip install Flask-Bootstrap4==4.0.2
 -pip install flask-script
 -pip install flask-wtf
 -pip install flask-migrate
 -pip install flask-login
 -pip install Flask-Mail
 -pip install flask-uploads

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
None if any other are found, drop me a message

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on developer ianodad@gmail.com for any comments, reviews or advice.

## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [flask](http://flask.pocoo.org/ ) documentation.

### License
Copyright (c) **Ian Odhimabo**
+ Python3.6 - Programming language
- Flask - Python micro-framework
- Git - Version control
- Sublime text - Code editor
- Postgres - Database


## Licence
MIT (c) 2017 [Ian Odhiambo](https://github.com/ianodad)


