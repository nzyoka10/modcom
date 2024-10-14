# lab1905.netlify.app
# Mkulima app

from flask import Flask 
from flask import render_template

app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# about page route
@app.route('/about')
def about():
    return render_template('about.html')

# services page route
@app.route('/services')
def services():
    return render_template('services.html')

# gallery page route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# FAQS route
@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

# contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Main entry
if __name__ == '__main__':
    app.run(debug= True)