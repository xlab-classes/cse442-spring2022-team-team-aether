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
