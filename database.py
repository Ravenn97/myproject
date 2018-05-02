import MySQLdb as sql
class Database():
	con = None
	cur = None
	connect = sql.connect("localhost", "root", "dotung", "loginDB")

	def __init__(self):
		pass

	def select(self):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("SELECT * FROM users")
			con.commit()
			return cur.fetchall()
		except:
			return None

	def add(self,data):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("INSERT INTO users(Id, Time_sleep) VALUES (%s,%s)" %data)
			con.commit()
			return "add thanh cong"
		except:
			return "khong the add"

	def update(self, data):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("UPDATE users SET  Time_sleep = %s WHERE Id = %s " % data)
			con.commit()
			return "update thanh cong"
		except:
			return "khong the update"

	def delete(self, Id):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("DELETE FROM users WHERE Id = %s" % Id)
			con.commit()
			return "xoa thanh cong"
		except Exception as e:
			return e

	






















