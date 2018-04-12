from flask import Flask
from flask import render_template
from flask import request
from database import Database

app = Flask(__name__)

@app.route('/add', methods=['POST', 'GET'])
def add_id():
	if request.method=='POST':
		data = (request.form['id'],request.form["time_sleep"])
		db = Database()
		a = db.add(data)

		return a
@app.route('/update',methods = ['POST', 'GET'])
def update():
	if request.method == 'POST':
		data = (request.form['time_sleep'],request.form["id"])
		db = Database()
		a = db.update(data)
		return a


@app.route('/delete',methods = ['POST', 'GET'])
def delete():
	if request.method == 'POST':
		Id = request.form['id']
		db = Database()
		a = db.delete(Id)
		return a


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
