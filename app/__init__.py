#flask by default understands that from app import app
#the init file is run immediately

#importing Flask class from flask.py file
#case sensitive.. importing the class Flask

from flask import Flask


#creating an instance of the Flask class, in order to run this app
#name parameter will default to folder name

#creating an instance of that class Flask


app = Flask(__name__)


#from the app folder, import the routes.py file, and startup at index
#will alwasu look for '/' as starting route

from app import routes
