import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='template')
Bootstrap(app)
app.secret_key = "secret key"

conn = mysql.connector.connect(
	host='localhost',
	user='flask',
	password='Michelle@26',
	database= 'week12'
)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        EmpID INT AUTO_INCREMENT PRIMARY KEY,
        EmpName VARCHAR(200),
        EmpGender VARCHAR(200),
        EmpPhone VARCHAR(200),
        EmpBdate VARCHAR(200))''')
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

        conn = mysql.connector.connect(
		host='localhost',
		user='flask',
		password='Michelle@26',
		database= 'week12'
)
        c = conn.cursor()
        c.execute("INSERT INTO employees (EmpName, EmpGender, EmpPhone, EmpBdate) VALUES ('{0}','{1}','{2}','{3}')" , (empname, empgender, empphone, empbdate))
        conn.commit()
        conn.close()

        return redirect(url_for('empinformation'))
    
    return render_template('empregistration.html')

@app.route('/empinformation')
def empinformation():
	conn = mysql.connector.connect(
		host='localhost',
		user='flask',
		password='Michelle@26',
		database= 'week12'
)
	cur = conn.cursor()
	cur.execute("SELECT * FROM employees")
	rows = cur.fetchall()
	return render_template('empinformation.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
