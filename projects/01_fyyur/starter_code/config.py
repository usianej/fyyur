import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Connect to the database


# IMPLEMENT DATABASE URL
# Ubuntu required password
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123@localhost:5432/fyyur'
