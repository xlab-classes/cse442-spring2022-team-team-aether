import authController

db = authController.db

# Stores creator (name of author of meme) and imgname (hash of meme) into user's row in database
# Returns False if the meme/creator does not exist
# Returns True upon success of storing meme in history

def storeInHistory(creator,imgname,user):
  cursor = db.cursor()
  cr = "CREATE TABLE IF NOT EXISTS history (username VARCHAR(64), idx INT, u1 VARCHAR(64), u2 VARCHAR(64), u3 VARCHAR(64), u4 VARCHAR(64), u5 VARCHAR(32), m1 VARCHAR(32), m2 VARCHAR(32), m3 VARCHAR(32), m4 VARCHAR(32), m5 VARCHAR(32))"
  cursor.execute(cr)
  db.commit()
  # Prove existance of meme
  cr = "SELECT username, imgname FROM imgstore WHERE username=%s AND imgname=%s"
  cursor.execute(cr, (creator, imgname,))
  detec = cursor.fetchall()
  if not detec:
    return False
  cr = "SELECT * FROM history WHERE username=%s"
  cursor.execute(cr, (user,))
  detec = cursor.fetchall()
  if not detec:
    create = "INSERT INTO history (username, idx, u1, m1) VALUES (%s, %s, %s, %s)"
    # print(create, flush=True);
    cursor.execute(create, (user, 2, creator, imgname,))
    db.commit()
    return True
  cr = "SELECT idx FROM history WHERE username=(%s)"
  cursor.execute(cr, (user,))
  index = cursor.fetchall()[0][0]
  cr = "UPDATE history SET u%s=%s, m%s=%s, idx=%s WHERE username=%s"
  # print(cr % (index, creator, index, imgname, (index%5)+1, user,), flush=True);
  cursor.execute(cr, (index, creator, index, imgname, (index%5)+1, user,))
  db.commit()
  return True

# Returns an array of key-value pairs (creator, meme) in the order they were viewed

def getHistory(user):
  cursor = db.cursor()
  cr = "SELECT * FROM history WHERE username=(%s)"
  cursor.execute(cr, (user,))
  detec = cursor.fetchall()
  if not detec:
    return ()     # No history for user
  historyarr = []
  index = detec[0][1]
  for i in range(5):
    u,m = detec[0][1+index], detec[0][6+index]
    if u!=None: #This implies m!=None
      historyarr.insert(0,(u,m))
    index = index%5+1
  return historyarr
