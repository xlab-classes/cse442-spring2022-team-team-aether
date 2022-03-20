import mysql.connector
import bcrypt

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="serverdata"
)


def authlogin(username, password):
  cursor = db.cursor()
  cursor.execute("SELECT password FROM users WHERE username = (%s)", (username,))
  res = cursor.fetchall()
  print(res[0][0])
  hpass = res[0][0]
  if (bcrypt.checkpw(password.encode(), hpass.encode())):
    print("logged in")
    return True
  else:
    print("failed")
    return False

def authcreateAccount(username, password):
  cursor = db.cursor()
  cr = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(64), password VARCHAR(64))"
  cursor.execute(cr)
  db.commit()
  salt = bcrypt.gensalt()
  hashpw = bcrypt.hashpw(password.encode(), salt)
  print("Password is " + hashpw.decode())

  addU = "INSERT INTO users (username, password) VALUES (%s, %s)"
  val = [username, hashpw]
  print(val)
  cursor.execute(addU, val)
  db.commit()
  return True

def authgetData(username):
  return None