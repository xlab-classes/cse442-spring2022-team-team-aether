import mysql.connector
import os
import authController

db = authController.db

def search(query):
    cursor = db.cursor()
    cs = "SELECT * FROM users"
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
    return ret