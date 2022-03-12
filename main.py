from sqlite3 import Cursor
from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import flask


local_server=True
app=Flask(__name__)
app.secret_key="dbmsproject"

#app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/dbname'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:AJcena714!!@localhost/dbp'
db=SQLAlchemy(app)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AJcena714!!'
app.config['MYSQL_DB'] = 'dbp'

@app.route("/fregdone", methods=["GET","POST"])
def regdone():
    
    name = request.form['name']
    uname = request.form['uname0']
    pswd = request.form['pswd0']
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO NEWLOGIN VALUES (%s,%s,%s)''',(name,uname,pswd))
    #rgg = gg.fetchall()
    #for x in rgg:
    #    print(x)
    mysql.connection.commit()
    cursor.close()
    return 'gg'
    

#    name= request.form['name']
#    uname=request.form['uname0']
#    pswd=request.form['pswd0']

#    cursor = mysql.connection.cursor()
#    cursor.execute('''INSERT INTO LOGINDB VALUES (%s,%s,%s)''',(name,uname,pswd))
#    mysql.connection.commit()
#    cursor.close()
#    return "submitted"


@app.route("/show")
def show():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM LOGINDB''')
    result = cursor.fetchall()
    for x in result:
        print(x)
    mysql.connection.commit()
    cursor.close()
    return "terminalin"

@app.route("/TI")
def TI():
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO LOGINDB VALUES ('VDFHA','NBVM')''')
    mysql.connection.commit()
    cursor.close()
    return "IN"



'''
class test(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
'''

class logindb(db.Model):
    uname=db.Column(db.String(16),primary_key=True)
    pswd=db.Column(db.String(16))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")
'''
@app.route("/login")
def loginpage1():
    return render_template("loginpage.html")
'''
@app.route("/login")
def loginpage():
    return render_template("loginpage.html")

@app.route("/signup")
def signuppage():
    return render_template("signup.html")

#test
'''
@app.route("/test")
def testING():
    try:
        a=test.query.all()
        print(a)
        return 'DB CONNECTED'
    except Exception as e:
        print(e)
        return f'NOOOOOOOO {e}'
'''
@app.route("/test")
def testING():
    try:
        a=logindb.query.all()
        print(a)
        return 'DB CONNECTED'
    except Exception as e:
        print(e)
        return f'NOOOOOOOO {e}'


app.run(debug=False)