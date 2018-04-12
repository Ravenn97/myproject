import MySQLdb as sql
class Database():
	con = None
	cur = None
	connect = sql.connect("localhost", "root", "dotung", "loginDB")

	def __init__(self):
		pass



	def add(self,data):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("INSERT INTO users(Id, Time_sleep) VALUES (%s,%s)" %data)
			con.commit()
			return "add thanh cong"
		except:
			return "khong the add"
		finally:
			cur.close()
			con.close()

	def update(self, data):
		con = Database.connect
		cur = con.cursor()
		try:
			cur.execute("UPDATE users SET  Time_sleep = %s WHERE Id = %s " % data)
			con.commit()
			return "update thanh cong"
		except:
			return "khong the update"
		finally:
			cur.close()
			con.close()

	def delete(self,id):
		con = Database.connect
		cur = con.cursor()
		try:
			cursor.execute("DELETE FROM `users` WHERE `users`.`Id` = %s" %id)
			con.commit()
			return "xoa thanh cong"
		except:
			return "khong the xoa"
		finally:
			cur.close()
			con.close()

	def close(self):
		try:
			if self.cursor == self.con:
				self.con.close()
				self.cursor.close()
		except:
			pass






















def insertUser(username,password):

    db = sql.connect("localhost","root","dotung","loginDB" )
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users