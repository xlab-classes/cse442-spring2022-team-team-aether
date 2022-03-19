import mysql.connector
import bcrypt

db = mysql.connector.connect(
  host="localhost",
  user="server",
  password="pass",
  database="serverdata"
)


def authlogin(username, password):
  cursor = db.cursor()
  cursor.execute("SELECT * FROM users WHERE username=?", username)
  res = cursor.fetchall()
  print(res)
  hpass = bcrypt.gensalt()
  if (bcrypt.checkpw(password, hpass)):
    return True
  else:
    return False

def authcreateAccount(username, password):
  cursor = db.cursor()
  cr = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(30) UNIQUE NOT NULL PRIMARY KEY, password VARCHAR(30) UNIQUE NOT NULL)"
  cursor.execute(cr)
  db.commit()
  salt = bcrypt.gensalt()
  hashpw = bcrypt.hashpw(password.encode(), salt)
  print("Password is " + hashpw)
  addU = "INSERT IGNORE INTO users (username, password) VALUES (%s, %s)"
  val = (username, hashpw)
  cursor.execute(addU, val)
  db.commit()
  return True

def authgetData(username):
  return None
