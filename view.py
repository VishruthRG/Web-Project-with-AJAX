from flask import request, Flask, render_template, redirect
from flaskext.mysql import MySQL
import math
import numpy as np
import os
import csv
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Vishruth!1'
app.config['MYSQL_DATABASE_DB'] = 'wt_project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def view():
	return render_template('index.html')

@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/login.html')
def login():
	return render_template('login.html')

@app.route('/trial.html')
def grade():
	return render_template('trial.html')


@app.route('/view', methods=['POST'])
def show():
	text = request.form.to_dict()
	input_text = text['input']
	#k = input_text.split(" ")
	#print(k)
	row_num = 13089
	with open('essays.csv', 'a') as fd:
		row = [row_num, row_num, 10, input_text, 0, 0, 0, 0, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',]
		writer = csv.writer(fd)
		writer.writerow(row)

	os.system('python MLProject.py')
	import MLProject as proj
	output = proj.y_pred
	if(len(input_text) < 100):
		output = 0
		print('Too short to grade')
		return render_template('display.html', input=input_text, score=output)
	output = math.ceil(output[0] * 100)
	return render_template('display.html', input=input_text, score=output)

@app.route('/signup.php', methods=['POST'])
def signup():
	data = request.form.to_dict()
	#print(data)
	firstname = data['firstname']
	lastname = data['lastname']
	email = data['email']
	username = data['username']
	gender = data['gender']
	#dob = data['dob']
	password = data['password']
	cur = mysql.get_db().cursor()
	cur.execute("INSERT INTO users (firstname,lastname,username,password,gender,email) VALUES (%s,%s,%s,%s,%s,%s)", (firstname, lastname, username, password, gender, email))
	mysql.get_db().commit()
	cur.close()
	return render_template('index.html')

@app.route('/signup.html')
def signupshow():
	return render_template('signup.html')





if __name__ == "__main__":
	app.run()

