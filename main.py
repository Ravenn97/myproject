from flask import Flask, request
from database import Database
import time
from crontab import CronTab

app = Flask(__name__)

def scheduleCron():
	db = Database()
	data = db.select()
	for row in data:
		my_cron = CronTab(user='van-xa')
		print(type(row[1]), len(my_cron))
		command = "python3 printjob.py {} {} >> abc.txt".format(row[0], row[1])
		comment = str(row[0])
		try:
			job = my_cron.new(command= command, comment = comment)
			job.minute.every(row[1])
			my_cron.write()
		except Exception as e:
			print(e)


@app.route('/add', methods=['POST', 'GET'])
def add_id():
	if request.method=='POST':
		data = (request.form['id'],request.form["time_sleep"])
		print(data[1], type(data[1]))
		db = Database()
		a = db.add(data)
		my_cron = CronTab(user = 'van-xa')
		command = "python3 printjob.py {} {} >> add.txt".format(data[0], data[1])
		comment = data[0]
		time_sleep = int(data[1])
		print(comment, type(comment))
		job = my_cron.new(command = command, comment = comment)
		job.minute.every(time_sleep)
		my_cron.write()
		return a




@app.route('/update',methods = ['POST', 'GET'])
def update():
	if request.method == 'POST':
		data = (request.form['time_sleep'],request.form["id"])
		db = Database()
		a = db.update(data)
		my_cron = CronTab(user = 'van-xa')
		for job in my_cron:
			if job.comment == data[0]:
				my_cron.remove(job)
				command = "python3 printjob.py {} {} >> abcd.txt".format(data[0], data[1])
				comment = str(data[0])
				time_sleep = int(data[1])
				job = my_cron.new(command= command, comment = comment)
				job.minute.every(time_sleep)
				my_cron.write()
		return a



@app.route('/delete',methods = ['POST'])
def delete():
	if request.method == 'POST':
		Id = request.form['id']
		print(Id)
		db = Database()
		a = db.delete(Id)
		my_cron = CronTab(user = 'van-xa')
		for job in my_cron:
			if job.comment == str(Id):
				my_cron.remove(job)
				my_cron.write()
		return a

	
if __name__ == '__main__':
	scheduleCron()
	app.run(debug=False, host='0.0.0.0')

