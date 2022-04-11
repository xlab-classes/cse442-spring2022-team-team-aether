import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysqlRoot00!",
  database="serverdata"
)


def imgstore(username, imgname, imgbyte): 
  cursor = db.cursor()
  cr = "CREATE TABLE IF NOT EXISTS imgstore (username varchar(64), img_name varchar(64), img_byte varbinary(max) foreign key (username) references users (username) "
  cursor.execute(cr)
  db.commit()

  insVal = "INSERT INTO imgstore (username, img_name, img_byte) VALUES (%s, %s, %s)"
  val = [username, imgname, imgbyte]
  print(val)
  cursor.execute(insVal, val)
  db.commit()
  return True

###
# def getimg(username, imgname): 
#   cursor = db.cursor()
#   query = "SELECT img_byte FROM imgstore WHERE username = %s AND img_name = %s"
#   cursor.execute(query, (username, imgname))


  

