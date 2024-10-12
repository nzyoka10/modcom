from flask import Flask 

app = Flask(__name__)

# index page route
@app.route('/')
def index():
    return 'My home page'

# login page
@app.route('/login')
def login():
    return 'Login page'

# register page
@app.route('/register')
def register():
    return 'Register page'

# about us page
@app.route('/about')
def about():
    return 'My About page'

# services page
@app.route('/services')
def services():
    return "Services page"

# gallery page
@app.route('/gallery')
def gallery():
    return "Gallery page"

# contact page
@app.route('/contact')
def contact():
    return "Contact page"



if __name__ == 'main':
    app.run(debug=True)