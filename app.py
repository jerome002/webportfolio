from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback_secret_key")


@app.route("/")
def home():
   return render_template("index.html", name="Jerome Kapkor", current_year= datetime.now().year)
@app.route("/projects")
def projects():
    
   projects = [
    {
        "title": "Portfolio Website",
        "points": [
            "Responsive personal website to showcase my work",
            "Includes About, Projects, and Contact pages",
            "Devoloped using:"
        ],
        "badges": ["Flask", "HTML5", "CSS3", "Bootstrap 5", "Jinja2"],
        "link": "https://jeromeportfolio-com.onrender.com/"
    },
  {
    "title": "Restaurant Management System",
    "description": "A full-featured restaurant management system designed to streamline daily operations. It allows management of menu items, inventory, staff, customer orders, sales reports, and reservations through a clean and responsive interface.",
    "points": [
        "Dynamic multi-section system for menu, orders, and inventory",
        "Admin dashboard for managing products, staff, and daily sales",
        "Real-time order tracking for efficient workflow",
        "Fully responsive UI optimized for mobile and desktop",
        "Built with modular, scalable architecture"
    ],
    "badges": ["Node.js", "Express", "MongoDB", "React", "Bootstrap 5"],
    "link": "#"
},
{
    "title": "Blog Web App",
    "description": "A fully functional clone of a modern web application built using Flask. The project replicates core features such as user accounts, content management, and dynamic pages—demonstrating backend logic, template rendering, and responsive UI design.",
    "points": [
        "Built with Flask using modular Blueprints and Jinja2 templates",
        "Implements user authentication (signup, login, logout)",
        "Dynamic content rendering with clean routing structure",
        "Responsive frontend using HTML5, CSS3, JavaScript, and Bootstrap 5",
        "Focuses on replicating real-world app workflows and UI interactions"
    ],
    "badges": ["Flask", "Jinja2", "HTML5", "CSS3", "JavaScript", "Bootstrap 5"],
    "link": "#"
}


]


   return render_template("projects.html", name="Jerome Kapkor", projects=projects, current_year=datetime.now().year)
@app.route("/about")
def about():
    return render_template("about.html", name="Jerome Kapkor", current_year=datetime.now().year)

@app.route('/contact')
def contact():

    return render_template('contact.html')
@app.route('/services')
def services():
    return render_template('services.html', name="Jerome Kapkor", current_year=datetime.now().year) 

if __name__ == '__main__':
    app.run(debug=True)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-if-not-set")


