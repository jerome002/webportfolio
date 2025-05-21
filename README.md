#  My Flask Portfolio

A professional portfolio website built with Flask, HTML, CSS, and Bootstrap to showcase your skills, projects, and contact information. Deployed on [Render](https://render.com).

##  Live Demo

 [Visit the live website](https://jeromeportfolio-com.onrender.com)  


---

## Project Structure

```
.
├── app.py                 # Main Flask application
├── templates/             # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── projects.html
├── static/
│   └── style.css          # Custom CSS
├── requirements.txt       # Python dependencies
└── render.yaml            # Render deployment config
```

---

##  Features

- Developer profile landing page
-  About section
-  Projects showcase
- Contact page with social links (Email, LinkedIn, X)
- Clean, responsive Bootstrap styling
-  Hosted on Render

---

## Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Flask (Python)
- **Deployment**: Render
- **Version Control**: Git + GitHub

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Deployment (Render)

1. Push your project to GitHub
2. Sign in to [Render](https://render.com)
3. Click **New Web Service**
4. Connect your GitHub repo
5. Fill in:
   - **Build Command**: *(leave empty)*
   - **Start Command**: `gunicorn app:app`
6. Done! Your app will be live shortly.

Make sure your project has:

- `render.yaml`
- `requirements.txt`
- `gunicorn` in your requirements

---

##  Contact

- [jkapkor@gmail.com](mailto:jkapkor@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/)
- [X (Twitter)](https://x.com/your-handle)

---

##  License

This project is licensed under the [MIT License](LICENSE).
