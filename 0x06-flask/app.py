# Madaraka with flask

from flask import Flask
from flask import render_template

app = Flask(__name__)

# index page route
@app.route('/')
def index():
    return render_template('index.html')
    # return 'Home page'

# about page route
@app.route('/about')
def about():
    return render_template('about.html')
    # return 'About page'

# services page route
@app.route('/services')
def services():
    return render_template('services.html')
    # return 'Services page'

# gallery page route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
    # return 'Gallery page'

# faqs page route
@app.route('/faqs')
def faqs():
    return render_template('faqs.html')
    # return 'Faqs page'

# contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')
    # return 'Contact page'

# main entry
if __name__ == '__main__':
    app.run(debug= True, port= 8080)