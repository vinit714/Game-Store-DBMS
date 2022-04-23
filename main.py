import re
from sqlite3 import Cursor
from flask import Flask, json,redirect,render_template,flash,request,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import flask
from tabulate import tabulate


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

theuser = "NAN"

@app.route("/fregdone", methods=["GET","POST"])
def regdone():
    
    name = request.form['name']
    uname = request.form['uname0']
    pswd = request.form['pswd0']
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO NEWLOGIN VALUES (%s,%s,%s)''',(name,uname,pswd))
    cursor.execute('''INSERT INTO LOGINDB VALUES (%s,%s)''',(uname,pswd))
    #rgg = gg.fetchall()
    #for x in rgg:
    #    print(x)
    mysql.connection.commit()
    cursor.close()
    return 'gg'
    
@app.route("/logincorrect",methods=["GET","POST"])
def logcheck():
    uname = request.form['uname0']
    pswd = request.form['pswd0']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM LOGINDB WHERE UNAME = %s AND PSWD = %s''',(uname,pswd))
    data=cursor.fetchall()
    if len(data)==0:
        print("Incorrect Username or Password")
        return 'Incorrect Username or Password'
    else:
        DAUSER = uname
        global theuser
        theuser = uname
        print("USER:"+uname)
        return DAUSER

def var():
    return theuser


@app.route("/gamebuy",methods=["GET","POST"])
def buygame():
    uname = var()
    gamename = request.form['gamename']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM GAMEBUY WHERE UNAME = %s AND GAME = %s''',(uname,gamename))
    data=cursor.fetchall()
    if len(data)==0:
        cursor.execute('''INSERT INTO GAMEBUY VALUES (%s,%s)''',(uname,gamename))
        mysql.connection.commit()
        cursor.close()
        return 'GAME BOUGHT'
    else:
        print("already bought")
        return 'already bought'
    

@app.route("/uc")
def cu():
    uname = var()
    return uname

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
    listdb =[]

    for x in result:
        print(x)
        listdb.append[x]
    mysql.connection.commit()
    cursor.close()
    #return listdb
    return 'terminal'

@app.route("/PT")
def PT():
    #list1 = ['a','b']
    #xx=listToString(list1)
    #xx = "\n".join(list1)
    #return xx
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM GAMES''')
    result = cursor.fetchall()
    list1 =[]

    for x in result:
        print(x)
        xx = ",".join(x)
        print(xx)
        list1 += [xx]
    #st = "\n".join(result)
    mysql.connection.commit()
    cursor.close()
    print(list1)
    lts = "<br><br>".join(list1)
    bu = '''    <form id="editg" action="editg" onsubmit="editpage()" method="post">
            <input type="submit" name="submit" value="edit">
    </form>'''
    bd = '''    <form id="deditg" action="deditg" onsubmit="deditpage()" method="post">
            <input type="submit" name="submit" value="DELETE">
    </form>'''
    #return lts + bu + bd
    return lts + bu

@app.route("/editg",methods=["GET","POST"])
def editpage():
    return render_template("editpage.html")

@app.route("/deditg",methods=["GET","POST"])
def deditpage():
    return render_template("deditpage.html")


def listToString(s):
    str1 = "" 
    for ele in s: 
        str1 += ele
    return str1 

@app.route("/TI")
def TI():
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO LOGINDB VALUES ('VDFHA','NBVM')''')
    mysql.connection.commit()
    cursor.close()
    return "IN"

@app.route("/admin")
def adminpage():
    return render_template("admin.html")


@app.route("/adminlog",methods=["GET","POST"])
def adminlogcheck():
    uname = request.form['uname0']
    pswd = request.form['pswd0']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM ADMIN WHERE UNAME = %s AND PSWD = %s''',(uname,pswd))
    data=cursor.fetchall()
    if len(data)==0:
        print("Incorrect Username or Password")
        return 'Incorrect Username or Password'
    else:
        return redirect(url_for('PT'))


@app.route("/gameadminlog",methods=["GET","POST"])
def gameadminlogcheck():
    ge = request.form['ge']
    gn = request.form['gn']
    gc = request.form['gc']
    cursor = mysql.connection.cursor()
    cursor.execute('''UPDATE GAMES SET GAME = %s, GAMECODE = %s WHERE GAME = %s;''',(gn,gc,ge))
    mysql.connection.commit()
    cursor.close()
    return "APPLIED"

@app.route("/dgameadminlog",methods=["GET","POST"])
def dgameadminlogcheck():
    ge = request.form['ge']
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM GAMES WHERE GAME = %s;''',(ge))
    mysql.connection.commit()
    cursor.close()
    return "DELETED"

@app.route("/table")
def tableee():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM LOGINDB''')
    data=cursor.fetchall()
    #print(data)
    return data


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