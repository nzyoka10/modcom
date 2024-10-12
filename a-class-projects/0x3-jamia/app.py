from flask import*
import pymysql
app = Flask (__name__)

# home page route
@app.route('/')
def homepage():

    # connect to database
    connection = pymysql.connect(host='localhost', user='root', password='', database='jamia_db')

    # query to get all phones from db
    sql = "SELECT * FROM products WHERE product_category = 'phones' "

    # you need to have a cursor
    # A cursor - is used to execute above sql query above
    cursor = connection.cursor()
    # execute the command - phones
    cursor.execute(sql)
    # fetch all phone rows - phones
    phones = cursor.fetchall()

    # get electronics
    sql1 = "SELECT * FROM products WHERE product_category = 'electronics' "

    # execute electronics query
    cursor1 = connection.cursor() 
    # execute electronics - electronics
    cursor1.execute(sql1)
    # fetch electronics 
    electronics = cursor1.fetchall()

    # get footwear
    sql2 = "SELECT * FROM products WHERE product_category = 'footwear' "
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    footwear = cursor2.fetchall()

    # html file to display phone data
    return render_template("index.html", phones=phones, electronics=electronics, footwear=footwear)


@app.route('/about')
def About():
    return "this is about page "


@app.route('/register')
def Register ():
    return " this is register page "

@app.route('/login')
def Login():
    return "login page"

@app.route('/logout')
def Logout():
    return "logout page"

if __name__ == '__main__':
    app.run(debug=True,port= 8080)