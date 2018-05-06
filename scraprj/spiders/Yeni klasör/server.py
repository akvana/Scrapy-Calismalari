from flask import Flask
import sqlite3 as lite
import sys
import time
con = None
con = lite.connect('dbser.db', check_same_thread = False)
cur = con.cursor()
set = '0123456789'
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        cur.execute("SELECT sayi FROM server WHERE id='1' ")
        datax=cur.fetchone()
        strx=str(datax)
        x=int(''.join([c for c in strx if c in set]))
        xx=x
        xx+=1
        cur.execute("UPDATE server SET sayi='%s' WHERE id='1' " % (xx))
        return str(x)
    except:
        time.sleep(3)
        cur.execute("SELECT sayi FROM server WHERE id='1' ")
        datax=cur.fetchone()
        strx=str(datax)
        x=int(''.join([c for c in strx if c in set]))
        xx=x
        return str(xx)
app.run('127.0.0.1', 8999, debug=False,threaded=True)

