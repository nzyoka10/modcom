# app.py file

from flask import Flask, render_template

app = Flask(__name__)

# first route to page 1
@app.route('/')
def page1():
    # return 'Hello World!'
    return render_template('page1.html')

# second route to page 2
@app.route('/login')
def page2():
    # return 'Hello, this is page 2 (Login page)!'
    return render_template('page2.html')

# page 3 route
@app.route('/page3')
def page3():
    return 'This is Page 3 --- view page!!!'


# main entry point
if __name__ == 'main':
    app.run(debug=True, port=8080)
