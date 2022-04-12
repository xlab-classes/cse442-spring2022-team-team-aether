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
  cr = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(64), password VARCHAR(64))"
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

# Will store a user selected meme into their history
# returns False if the image does not exist, true otherwise
def storeInHistory(creator,imgname):
  cursor = db.cursor()
  cr = "CREATE TABLE IF NOT EXISTS history (username VARCHAR(64), idx INT, u1 VARCHAR(64), u2 VARCHAR(64), u3 VARCHAR(64), u4 VARCHAR(64), u5 VARCHAR(32), m1 VARCHAR(32), m2 VARCHAR(32), m3 VARCHAR(32), m4 VARCHAR(32), m5 VARCHAR(32))"
  cursor.execute(cr)
  db.commit()
  # Prove existance of meme
  cr = "SELECT username, img_name FROM imgstore WHERE username=%s AND img_name=%s"
  cursor.execute(cr, (creator, imgname,))
  detec = cursor.fetchall()
  print("Executed existance SQL code", flush=True);
  if not detec:
    return False
  # TODO FIGURE OUT HOW TO SELECT A SPECIFIC USER
  user = "testuser1"
  # currently a dummy user is used independent of user database
  cr = "SELECT * FROM history WHERE username=%s"
  cursor.execute(cr, (user,))
  detec = cursor.fetchall()
  if not detec:
    create = "INSERT INTO history (username, idx, u1, m1) VALUES (%s, %s, %s, %s)"
    cursor.execute(create, (user, 2, creator, imgname,))
    db.commit()
    return True
  cr = "SELECT idx FROM history WHERE username=(%s)"
  cursor.execute(cr, (user,))
  index = cursor.fetchall()[0][0]
  cr = "UPDATE history SET u%s=%s, m%s=%s, idx=%s WHERE username=%s"
  cursor.execute(cr, (index, creator, index, imgname, (index+1)%5, user,))
  return True

def authgetData(username):
  return None

