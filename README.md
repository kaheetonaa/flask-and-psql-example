psql create database name people
$ pip install psycopg2-binary
$ pip install flask-sqlalchemy
$ pip install Flask-Migrate

$ mkdir templates static
$ touch app.py
$ cd templates
$ touch index.html

python3 -m venv venv
source venv/bin/activate

flask db init
flask db migrate
flask db upgrade

flask run
