import mysql.connector
import bcrypt

db = mysql.connector.connect(
  host="localhost",
  user="server",
  password="pass",
  database="serverdata"
)

def login(username, password):

  return
