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

# single item route
@app.route('/singleitem/<product_id>')
def singleitem(product_id):

     # connect to database
    connection = pymysql.connect(host='localhost', user='root', password='', database='jamia_db')

    # query to get record
    sql =  "SELECT * FROM products WHERE product_id = %s "

    # create cursor
    cursor = connection.cursor()

    # execute query
    cursor.execute(sql, product_id)

    # get the single product
    product = cursor.fetchone()

    return render_template("singleitem.html", product=product)

# upload route
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    # check method, to add products
    if request.method == 'POST':

        # get form inputs
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # database connection
        connection = pymysql.connect(host='localhost', user='root', password='', database='jamia_db')

        # create a cursor
        cursor = connection.cursor()


        # query to process form
        sql = """
                INSERT INTO products(product_name, product_desc, product_cost, product_category, product_image_name)
                VALUES (%s, %s, %s, %s, %s)
            """
        data = (product_name, product_description, product_cost, product_category, product_image_name.filename)

        # execute the query
        cursor.execute(sql, data)

        # save changes
        connection.commit()



        return render_template("upload.html", message = "New product added!")   

    else:
        return render_template("upload.html", error = "Please add a product")

# fashion route
# helps to see all the routes
@app.route('/fashion')
def fashion():
    return "this is fashion page "

# route to upload fashion
@app.route('/uploadfashion')
def uploadfashion():
    return render_template("uploadfashion.html")

# about page route
@app.route('/about')
def About():
    return "this is about page "

# register route
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
    app.run(debug = True, port = 8080)