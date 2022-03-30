import psycopg2
from flask import Flask, render_template, request



app = Flask(__name__, template_folder='template')

def db_connection():
    conn = psycopg2.connect(database='db',
                                user='postgres',
                                password='1111',
                                host="postgres")
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Info")
    rows = cur.fetchall()
    cur.close()
    return render_template("list.html", rows=rows)

@app.route('/get')
def get():
    return render_template('get.html')

@app.route('/select', methods=['POST', 'GET'])
def select():
    operation = "SELECT"
    res = ''
    if request.method == 'POST':
            var = request.form['var']
            conn = db_connection()
            cur = conn.cursor()
            try:
                cur.execute("SELECT * from Info where Id =%s", var)
                row = cur.fetchall()
            except:
                row = "No such result found"
    cur.close()
    return render_template("result.html", row=row, operation=operation)

@app.route('/delete')
def remove():
    return render_template('delete.html')

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    operation = "DELETE"
    res = "Error!"
    if request.method == 'POST':
            var = request.form['var']
            conn = db_connection()
            cur = conn.cursor()
            try:
                cur.execute("DELETE from Info where Id = %s", var)
                conn.commit()
                res = "Row was deleted"
                cur.close()
            except:
                pass
    return render_template("result_del.html", res=res, operation=operation)

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=5000)