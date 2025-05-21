from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv #Needed for flash messages

@app.route("/")
def home():
   return render_template("index.html", name="Jerome Kapkor", current_year=datetime.now().year)
@app.route("/projects")
def projects():
    projects = [
        {"title": "Portfolio Website", "description": "A personal portfolio website.", "link": "#"},
        {"title": "E-Commerce App", "description": "Full-featured e-commerce web app.", "link": "#"},
        {"title": "REST API", "description": "A RESTful API built with Flask.", "link": "#"},
        {"title": "Chat Application", "description": "Real-time chat app using WebSockets.", "link": "#"},
        {"title": "Blog Platform", "description": "A blogging platform with user authentication.", "link": "#"},
    ]
    return render_template("projects.html ", name="Jerome Kapkor", projects=projects, current_year=datetime.now().year)
@app.route("/about")
def about():
    return render_template("about.html", name="Jerome Kapkor", current_year=datetime.now().year)

@app.route('/contact')
def contact():

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-if-not-set")


