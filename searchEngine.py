import mysql.connector
import os
import authController
import sys

db = authController.db

def search(query):
    db.reconnect()
    cursor = db.cursor()
    cs = "SELECT * FROM imgtags"
    cursor.execute(cs)
    results = cursor.fetchall()
    ret = []
    print(results)
    for meme in results:
        match = 0
        for tag in meme:
            for s in query:
                if tag == s:
                    match += 1
        if match > 0:
            ret.append(meme[0])
    print(ret)
    sys.stdout.flush()
    return ret