import sys
import mysql.connector
from PIL import Image 
import io
import os
import authController
import generate

db = authController.db


def imgstore(username, img_name, tag_arr): 
  db.reconnect()
  cursor = db.cursor()
  cursor.execute('set global max_allowed_packet=67108864')
  cr = '''CREATE TABLE IF NOT EXISTS imgstore( 
    username varchar(64), 
    imgname varchar(32),
    imgbytes varbinary(65000)
    )'''
  cursor.execute(cr)
  db.commit()
  print("created table imgstore")
  
  img_file = img_name + ".jpg"
  with open(img_file, "rb") as image:
    img = image.read()
    imgbytes = bytes(img)
  
  stmt = "INSERT INTO imgstore VALUES (%s, %s, %s)" 
  insval = [username, img_name, imgbytes]
  cursor.execute(stmt, insval)
  db.commit()
  print(True)


  tag_cr = '''CREATE TABLE IF NOT EXISTS imgtags( 
    imghash varchar(32),
    tag1 varchar(16),
    tag2 varchar(16),
    tag3 varchar(16),
    tag4 varchar(16),
    tag5 varchar(16)
    )'''
  cursor.execute(tag_cr)
  db.commit()
  print("created table imgtags")
  
  cursor.execute("INSERT INTO imgtags VALUES (%s, %s, %s, %s, %s, %s)", (img_name, tag_arr[0], tag_arr[1], tag_arr[2], tag_arr[3], tag_arr[4], ))
  db.commit()
  db.close()
  return(True)

  
#imgstore("testuser", "test_img")

def getuserimg(username, img_name):
  db.reconnect()
  cursor = db.cursor()
  cursor.execute('set global max_allowed_packet=67108864')
  cursor.execute("SELECT imgbytes FROM imgstore WHERE username = %s AND imgname = %s", (username, img_name, ))
  res = cursor.fetchall()
  img_data = res[0][0]
  #image = Image.open(io.BytesIO(img_data))
  #image.save(img_name + '.jpg')
  db.close()
  print(True)
  return img_data

def getalluserimgs(username):
  db.reconnect()
  cursor = db.cursor()
  cursor.execute('set global max_allowed_packet=67108864')
  cursor.execute("SELECT * FROM imgstore WHERE username = %s", (username,))
  res = cursor.fetchall()
  #img_data = res[0][0]
  #image = Image.open(io.BytesIO(img_data))
  #image.save(img_name + '.jpg')
  db.close()
  print(True)
  return res

#getimg("testuser", "test_img")

def getall():
  if(not db.is_connected()):
    db.reconnect()
  cursor = db.cursor()
  cursor.execute('set global max_allowed_packet=67108864')
  cursor.execute("SELECT * FROM imgstore")
  result = cursor.fetchall()
  db.close()
  return result 

def imgbyhash(hashval):
  if(not db.is_connected()):
    db.reconnect()
  #print("in imgbyhash")
  sys.stdout.flush()
  cursor = db.cursor()
  cursor.execute('set global max_allowed_packet=67108864')
  cursor.execute("SELECT imgbytes FROM imgstore where imgname = %s", (hashval,))
  #print("almsot got the result")
  sys.stdout.flush()
  result = cursor.fetchall()
  db.close()
  #print("got the result")
  sys.stdout.flush()
  #print(result)
  sys.stdout.flush()
  #print(result[0][0])
  sys.stdout.flush()
  #print(result)
  sys.stdout.flush()
  return result[0][0]



