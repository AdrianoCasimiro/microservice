import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ.get('DBUSER'),
    dbpass=os.environ.get('DBPASS'),
    dbhost=os.environ.get('DBHOST'),
    dbname=os.environ.get('DBNAME')
)

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)


@app.route('/')
def view_registered_weathers():
    from models import Sensor
    sensores = Sensor.query.all()
    return render_template('sensor.html', sensores=sensores)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
