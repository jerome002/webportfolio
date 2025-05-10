from flask import Flask, render_template
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():

    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-if-not-set")


