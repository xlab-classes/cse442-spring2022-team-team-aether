import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysqlRoot00!",
  database="serverdata"
)


def imgstore(username, img_tag, img_file): 
  cursor = db.cursor()
  cr = '''CREATE TABLE IF NOT EXISTS imgstore( 
    username varchar(64), 
    itag varchar(32),
    img_bytes varbinary(8000)
    )'''
  cursor.execute(cr)
  db.commit()
  print("created table")

  imgUname = "INSERT INTO imgstore (username, itag) VALUES (%s, %s)"
  insVal = [username, img_tag]
  cursor.execute(imgUname, insVal)
  db.commit()
  print("username & imgtag inserted")
  
  with open(img_file, "rb") as image:
    img = image.read()
    imgby = bytearray(img)
    print(len(imgby))
    cursor.execute("INSERT INTO imgstore (img_bytes) VALUES (%s)", (imgby,))
    db.commit()
  
  print("received file")








