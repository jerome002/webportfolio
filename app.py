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
   return render_template("index.html", name="Jerome Kapkor", current_year=datetime.now().year)
@app.route("/projects")
def projects():
    
   projects = [
    {
        "title": "Portfolio Website",
        "points": [
            "Responsive personal website to showcase my work",
            "Includes About, Projects, and Contact pages",
            "Built with:"
        ],
        "badges": ["Flask", "HTML5", "CSS3", "Bootstrap 5", "Jinja2"],
        "link": "https://jeromeportfolio-com.onrender.com/"
    },
    {
        "title": "COVID-19 Data Tracker",
        "points": [
            "Visualizes global COVID-19 stats with charts",
            "Includes downloadable reports",
            "Built with:"
        ],
        "badges": ["Flask", "Python", "Pandas", "Plotly", "Data Analysis"],
        "link": "https://github.com/jerome002/Covid-19-Data-Tracker-project.git"
    },
    {
        "title": "Banking System",
        "points": [
            "User login and account management",
            "Deposit, withdraw, and view transaction history",
            "Export to PDF/CSV, admin dashboard"
            "Built with:"
        ],
        "badges": ["Flask", "MySQL", "Flask-WTF", "Bootstrap 5", "Authentication"],
        "link": "https://github.com/jerome002/Banking-System.git"
    },
    {
        "title": "Restaurant Website",
        "points": [
            "Multi-section website for a restaurant",
            "Displays menu, about info, and contact details",
            "Responsive design using:"
           
        ],
        "badges": ["Flask", "HTML5", "CSS3", "JavaScript", "Bootstrap 5"],
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

if __name__ == '__main__':
    app.run(debug=True)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-if-not-set")


