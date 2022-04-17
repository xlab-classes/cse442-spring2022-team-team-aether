import mysql.connector
from PIL import Image 
import io
import os


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="serverdata"
)


def imgstore(username, img_name): 
  cursor = db.cursor()
  cr = '''CREATE TABLE IF NOT EXISTS imgstore( 
    username varchar(64), 
    imgname varchar(32),
    imgbytes varbinary(65000)
    )'''
  
  cursor.execute(cr)
  db.commit()
  print("created table")
  
  img_file = img_name + ".jpg"
  with open("test_img.jpg", "rb") as image:
    img = image.read()
    imgbytes = bytes(img)
  
  stmt = "INSERT INTO imgstore VALUES (%s, %s, %s)" 
  insval = [username, img_name, imgbytes]
  cursor.execute(stmt, insval)
  db.commit()
  print(True)

  
#imgstore("testuser", "test_img")

def getimg(username, img_name):
  cursor = db.cursor()
  cursor.execute("SELECT imgbytes FROM imgstore WHERE username = %s AND imgname = %s", (username, img_name, ))
  res = cursor.fetchall()
  img_data = res[0][0]
  image = Image.open(io.BytesIO(img_data))
  image.save(img_name + '.jpg')
  
  print(True)

#getimg("testuser", "test_img")




