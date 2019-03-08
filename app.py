from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
#configure db
db = yaml.load(open('db.yaml'))
print ('this is db-------->>>>>>>>> ', db)
app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']
#pass the app parameter into mysql module
mysql=MySQL(app)
#inserting into database
@app.route('/',methods=['GET','POST'])
def insert():
  
	if request.method == 'POST':
		
		#fetch data from database
		#empDetails = request.form
		Name = request.form.get('name')
		LName = request.form.get('lname')
		
		#Name = empDetails["name"]
		#Email = empDetails["email"]
		#here we are executing query in database using cursor
		cur = mysql.connection.cursor()
		sql = "INSERT INTO employees(name,LName) VALUES(%s,%s)"
		val = (Name,LName)
		cur.execute(sql,val)
		mysql.connection.commit()
		cur.close()
		return "Registered"
	return render_template("index.html")





#getting the details
@app.route('/employeeInfo') 
def getEmployees():
	cur=mysql.connection.cursor()
	result = cur.execute("select * from employees")  
	if result > 0 :
		empDetails = cur.fetchall()
		#return str(empdetails)
		return render_template("employees.html",empDetails=empDetails)

if __name__ == '__main__':
	app.run(debug=True)


