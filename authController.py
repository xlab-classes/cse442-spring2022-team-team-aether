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
def storeInHistory(imgname):
  cursor = db.cursor()
  # TODO
  # - FIGURE OUT HOW TO STORE IMAGES AS DATA
  # AND HOW TO RETRIEVE DATA
  # Below is a possible statement
  cr = "SELECT imgname FROM images WHERE imgname = (%s)"
  cursor.execute(cr, imgname)
  detec = cursor.fetchall()
  if not detec:
    return False
  # TODO
  # - FIGURE OUT IF WE NEED TO MAKE A NEW DATABASE
  # - FIGURE OUT HOW TO ADD & MODIFY HISTORY DATA TO users DB
  # This includes moving history[1] -> history[2], history[2] -> history[3] etc.
  # Unsure of what to do here due to not knowing SQL pointers
  cr = ""
  return True

def authgetData(username):
  return None

