import mysql.connector
import os
import authController

db = authController.db

def search(query):
    cursor = db.cursor()
    cs = "SELECT * FROM imgtags"
    cursor.execute(cs)
    results = cursor.fetchall()
    ret = []
    def com(i1, i2):
        return i1[1] - i2[1]
    print(results)
    for meme in results:
        match = 0
        for tag in meme:
            for s in query:
                if tag == s:
                    match += 4
        if match > 0:
            ret.append((meme[0], match))
    r = sorted(ret, key=com, reverse=True)
    return r