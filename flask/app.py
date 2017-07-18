from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_entry():
   return render_template('entry.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         phone = request.form['phone']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO table1(name,phone) VALUES (?,?)",(nm,phone) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/search')
def search_entry():
    return render_template('search.html')

@app.route('/getrec',methods = ['POST','GET'])
def getrec():
    if request.method == 'GET':
        
        try:
            nm = request.form['nm']
            
            with sql.connect('database.db') as con:
                
                cur = con.cursor()
                
                cur.execute("SELECT name,phone FROM table1 WHERE name = ?",(nm))
                msg = "Record displayed successfully"
                
                
        except:
            con.rollback()
            msg = "error in seach operation"
            
        finally:
            return render_template("result1.html", msg = msg)
            con.close()        
                
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from table1")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
