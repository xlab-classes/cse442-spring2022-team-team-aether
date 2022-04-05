import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysqlRoot00!",
  database="serverdata"
)


def imgstore(username, imgbyte): 
    cursor = db.cursor()
    cr = "CREATE TABLE IF NOT EXISTS imgstore username varchar(64), imgs varbinary(max) foreign key (username) references users (username) "
    cursor.execute(cr)
    db.commit()

    insVal = "INSERT INTO imgstore (username, imgbyte) VALUES (%s, %s)"
    val = [username, imgbyte]
    print(val)
    cursor.execute(insVal, val)
    db.commit()
    return True



  

