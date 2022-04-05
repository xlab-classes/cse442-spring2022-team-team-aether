import mysql.connector
import bcrypt

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysqlRoot00!",
  database="serverdata"
)


def authlogin(username, password):
  cursor = db.cursor()
  cursor.execute("SELECT password FROM users WHERE username = (%s)", (username,))
  res = cursor.fetchall()
  if not res:
    print("account doesn't exist")
    return False
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
  cr = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(64), password VARCHAR(64), primary key (username))"
  cursor.execute(cr)
  db.commit()
  cursor.execute("SELECT password FROM users WHERE username = (%s)", (username,))
  detec = cursor.fetchall()
  if detec:
    print("user already exists")
    return False
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