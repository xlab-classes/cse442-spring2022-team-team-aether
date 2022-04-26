import mysql.connector
import bcrypt
import hashlib
import base64


db = mysql.connector.connect(
  host="oceanus",
  user="susanbre",
  password="5018193",
  database="serverdata"
)

#db = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    password="pass",
#    database="serverdata"
#)


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
  cr = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(64), password VARCHAR(64), token VARCHAR(64))"
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

def updateToken(username, token):
  cursor = db.cursor()
  s = "UPDATE users SET token = (%s) WHERE username = (%s)"
  salt = bcrypt.gensalt()
  hashtoken = bcrypt.hashpw(token.encode(), salt)
  val = (hashtoken, username)
  cursor.execute(s, val)
  db.commit()
  return None

def verifyToken(username, token):
  cursor = db.cursor()
  cursor.execute("SELECT token FROM users WHERE username = (%s)", (username,))
  res = cursor.fetchall()
  htoken = res[0][0]
  if not htoken:
    return False
  print(token)
  print(htoken)
  if(bcrypt.checkpw(token.encode(), htoken.encode())):
    print("authenticated")
    return True
  else:
    print(token, flush=True)
    print(htoken, flush=True)
    print("not valid")
    return False


def authgetData(username):
  return None

