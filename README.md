psql create database name people<br>
$ pip install psycopg2-binary<br>
$ pip install flask-sqlalchemy<br>
$ pip install Flask-Migrate<br>

$ mkdir templates static<br>
$ touch app.py<br>
$ cd templates<br>
$ touch index.html<br>

python3 -m venv venv<br>
source venv/bin/activate<br>

flask db init<br>
flask db migrate<br>
flask db upgrade<br>

flask run<br>
