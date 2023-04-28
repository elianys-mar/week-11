import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='template')
app.secret_key = "secret key"

conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        EmpID INTEGER PRIMARY KEY AUTOINCREMENT,
        EmpName TEXT,
        EmpGender TEXT,
        EmpPhone TEXT,
        EmpBdate DATE)''')
print("Table created")
conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/empregistration', methods=['GET', 'POST'])
def empregistration():
    if request.method == 'POST':
        empname = request.form['EmpName']
        empgender = request.form['EmpGender']
        empphone = request.form['EmpPhone']
        empbdate = request.form['EmpBdate']

        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("INSERT INTO employees (EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (?, ?, ?, ?)" , (empname, empgender, empphone, empbdate))
        conn.commit()
        conn.close()

        return redirect(url_for('empinformation'))
    
    return render_template('empregistration.html')

@app.route('/empinformation')
def empinformation():
    with sqlite3.connect('employees.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
    return render_template('empinformation.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
