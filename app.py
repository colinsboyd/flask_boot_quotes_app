# import the Flask class from the flask module
from flask import Flask, render_template
import os
from pymongo import MongoClient
#from bson import ObjectId
#from pymongo import MongoClient

myclient=MongoClient() 
mydb=myclient["quotes"]
mycol=mydb["quotes"]

mydoc=mycol.find();

for x in mydoc:
	print(x)

# create the application object
app = Flask(__name__,static_url_path='/static')

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
