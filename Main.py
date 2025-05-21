from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
import hashlib
import datetime

x = datetime.datetime.now()
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

#blockchain = Blockchain()






@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/admin")
def admin():

    return render_template('adlog.html')
@app.route("/admintrust")
def admintrust():

    return render_template('admintrust.html')

@app.route("/user")
def user():

    return render_template('user.html')
@app.route("/register")
def register():

    return render_template('register.html')
@app.route("/addsatellite")
def addsatellite():

    return render_template('addsatellite.html')



@app.route("/login")
def emp():
    return render_template('login.html')
@app.route("/adminhome")
def adminhome():



    return render_template('adminhome.html')
@app.route("/adminhome1")
def adminhome1():



    return render_template('adminhome1.html')
@app.route("/adduser")
def adduser():
    return render_template('adduser.html')

@app.route("/viewsatellite")
def viewsatellite():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("SELECT * from satelliteinfo ")
    data = cursor.fetchall()
    return render_template('viewsatellite.html',data=data)
@app.route("/userinfo")
def userinfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register ")
    data = cursor.fetchall()

    return render_template('userinfo.html',data=data)
@app.route("/adduserdata")
def adduserdata():
    return render_template('adduserdata.html')

@app.route("/adddepartment")
def adddepartment():
    return render_template('adddepartment.html')
@app.route("/reports")
def reports():
    return render_template('reports.html')



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':



           return render_template('adminhome.html')

       else:
        return render_template('index.html', error=error)

@app.route("/trustlogin", methods=['GET', 'POST'])
def trustlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':



           return render_template('adminhome1.html')

       else:
        return render_template('index.html', error=error)

@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
     if request.method == 'POST':
          name = request.form['name']


          pnumber = request.form['phone']
          email = request.form['email']
          maddress = request.form['maddress']
          uname = request.form['uname']
          password = request.form['password']
          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("SELECT * from satelliteinfo where saddress='" + str(maddress) + "'")
          data = cursor.fetchone()
          sa=data[1]


          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("insert into register values('','"+name+"','"+pnumber+"','"+email+"','"+maddress+"','"+uname+"','"+password +"','"+str(sa)+"')")
          conn.commit()
          conn.close()


     return render_template('adduser.html')
@app.route("/newsatellite", methods=['GET', 'POST'])
def newsatellite():
     if request.method == 'POST':
          sno = request.form['sno']

          name = request.form['name']
          saddress = request.form['saddress']



          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("insert into satelliteinfo values('','"+sno+"','"+name+"','"+saddress+"')")
          conn.commit()
          conn.close()


     return render_template('addsatellite.html')

@app.route("/newdata", methods=['GET', 'POST'])
def newdata():
     if request.method == 'POST':
          sno = request.form['sno']

          file = request.files['file']
          details = request.form['details']
          file.save("static/upload/" + secure_filename(file.filename))

          str1 = str(sno) + str(file)
          result = hashlib.sha1(str1.encode())

          # printing the equivalent hexadecimal value.
          print("The hexadecimal equivalent of SHA1 is : ")
          print(result.hexdigest())
          b = result.hexdigest()
          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("select * from newdata");
          data = cursor.fetchone()
          print(data)
          if data is None:
              conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
              cursor = conn.cursor()
              cursor.execute(
                  "insert into newdata values('','" + sno + "','" + file.filename + "','" + details + "','0','"+str(b)+"')")
              conn.commit()
              conn.close()
          else:
              conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
              cursor1 = conn1.cursor()
              cursor1.execute("select max(id) from newdata")
              da = cursor1.fetchone()
              print(da)
              for i in da:
                  d = i
              print(d)
              # str()

              conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
              cursor111 = conn111.cursor()
              cursor111.execute("select * from newdata where id='" + str(d) + "'")
              da11 = cursor111.fetchall()
              for item11 in da11:
                  df1 = item11[4]
                  print(df1)
              conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
              cursor = conn.cursor()
              cursor.execute(
                  "insert into newdata values('','" + sno + "','" + file.filename + "','" + details + "','"+str(df1)+"','" + str(
                      b) + "')")
              conn.commit()
              conn.close()






     return render_template('adduserdata.html')





@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
     if request.method == 'POST':
          name = request.form['uname']

          password = request.form['password']
          session['uname']=name



          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("select * from register where uname='"+name+"' and password='"+password+"'")
          data = cursor.fetchone()
          if data is None:
              return "Username And Password Wrong"
          else:
              conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
              cursor = conn.cursor()
              cursor.execute("select * from register where uname='" + name + "' and password='" + password + "'")
              data = cursor.fetchall()
              return render_template('UserHome.html',data=data)


@app.route("/userhome")
def userhome():
    uname=session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register where uname='"+uname+"' ")
    data = cursor.fetchall()
    return render_template('userhome.html',data=data)
@app.route("/uviewdata")
def uviewsatcom():
    uname=session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register where uname='"+uname+"'")
    data = cursor.fetchone()
    if data is None:
        data1 = "No data Found"
        print("test")
    else:
        ma=data[7]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
        cursor = conn.cursor()
        cursor.execute("SELECT * from newdata where sno='" + str(ma) + "'")
        data = cursor.fetchall()
        if data is None:
            data=''
            data1="No data Found"
            print("test")
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
            cursor = conn.cursor()
            cursor.execute("SELECT * from newdata where sno='" + str(ma) + "'")
            data = cursor.fetchall()
            data1=str(ma)+" Data Information"


    return render_template('uviewdata.html',data=data,data1=data1)

@app.route("/dwnd")
def dwnd():
    uname=session['uname']
    id=request.args.get('id')
    import re, uuid
    print("The MAC address in formatted and less complex way is : ", end="")
    print('-'.join(re.findall('..', '%012x' % uuid.getnode())))
    s = '-'.join(re.findall('..', '%012x' % uuid.getnode()))
    s1 = s.upper()

    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT * from register where maddress='" + str(s1) + "'")
    data1 = cursor1.fetchone()
    if data1 is None:
        uname1 = 'Unkown User'
    else:
        uname1 = data1[1]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("SELECT * from newdata where id='"+str(id)+"'")
    data = cursor.fetchone()
    if data is None:
        print("test")
    else:
        s=data[1]
        fname=data[2]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
        cursor = conn.cursor()
        cursor.execute("SELECT * from satelliteinfo where sno='" + str(s) + "'")
        data = cursor.fetchone()
        if data is None:
            print("test")
        else:
            ma=data[3]


            # joins elements of getnode() after each 2 digits.
            # using regex expression

            if str(ma) == str(s1):
                str1 = str(id) + str(s1)
                result = hashlib.sha1(str1.encode())

                # printing the equivalent hexadecimal value.
                print("The hexadecimal equivalent of SHA1 is : ")
                print(result.hexdigest())
                b = result.hexdigest()
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                cursor = conn.cursor()
                cursor.execute("select * from datablock");
                data = cursor.fetchone()
                print(data)
                if data is None:
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into datablock values('','" + uname1 + "','" + str(s1) + "','" + str(fname) + "','0','" + str(
                            b) + "','','"+str(x)+"')")
                    conn.commit()
                    conn.close()
                else:
                    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor1 = conn1.cursor()
                    cursor1.execute("select max(id) from datablock")
                    da = cursor1.fetchone()
                    print(da)
                    for i in da:
                        d = i
                    print(d)
                    # str()

                    conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor111 = conn111.cursor()
                    cursor111.execute("select * from datablock where id='" + str(d) + "'")
                    da11 = cursor111.fetchall()
                    for item11 in da11:
                        df1 = item11[5]
                        print(df1)
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into datablock values('','" + uname1 + "','" + str(s1) + "','" + str(fname) + "','"+str(df1)+"','" + str(
                            b) + "','','"+str(x)+"')")
                    conn.commit()
                    conn.close()
                data="Decryption SuccessFull Download Now"
                return render_template('dwn1.html', data=data,fname=fname)
                print("test")
            else:
                str1 = str(id) + str(s1)
                result = hashlib.sha1(str1.encode())

                # printing the equivalent hexadecimal value.
                print("The hexadecimal equivalent of SHA1 is : ")
                print(result.hexdigest())
                b = result.hexdigest()
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                cursor = conn.cursor()
                cursor.execute("select * from datablock");
                data = cursor.fetchone()
                print(data)
                if data is None:
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into datablock values('','" + uname1 + "','" + str(s1) + "','" + str(
                            fname) + "','0','" + str(
                            b) + "','Attack Found','"+str(x)+"')")
                    conn.commit()
                    conn.close()
                else:
                    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor1 = conn1.cursor()
                    cursor1.execute("select max(id) from datablock")
                    da = cursor1.fetchone()
                    print(da)
                    for i in da:
                        d = i
                    print(d)
                    # str()

                    conn111 = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor111 = conn111.cursor()
                    cursor111.execute("select * from datablock where id='" + str(d) + "'")
                    da11 = cursor111.fetchall()
                    for item11 in da11:
                        df1 = item11[5]
                        print(df1)
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into datablock values('','" + uname1 + "','" + str(s1) + "','" + str(
                            fname) + "','"+str(df1)+"','" + str(
                            b) + "','Attack Found','"+str(x)+"')")
                    conn.commit()
                    conn.close()
                    data="verification failed"

                print("normal")



    return render_template('ubooksatcom.html',data=data)
@app.route("/booksatcom", methods=['GET', 'POST'])
def booksatcom():
     if request.method == 'POST':
          uname=session['uname']
          hname = request.form['hname']

          ename = request.form['ename']
          date = request.form['date']
          details = request.form['details']
          f = request.files['file']
          f = request.files['file']
          f.save("static/upload/" + secure_filename(f.filename))



          conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
          cursor = conn.cursor()
          cursor.execute("insert into hbooking values('','"+hname+"','"+ename+"','"+date+"','"+details+"','"+f.filename+"','"+uname +"')")
          conn.commit()
          conn.close()


     return render_template('usatcombook.html')

@app.route("/download")
def download():
    path = request.args.get('id')



    return send_file(path, as_attachment=True)


@app.route("/blockinfo")
def blockinfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='satcom')
    cursor = conn.cursor()
    cursor.execute("select * from datablock")
    data = cursor.fetchall()
    return render_template('blockinfo.html',data=data)










if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)