from flask import Flask,render_template,request
import mysql.connector
import random
import string
from dotenv import dotenv_values
config=dotenv_values(".env")
print(config)

def random_alphanumeric_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


connection = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)

cur = connection.cursor()
app = Flask(__name__)

#Messgae Taker 
@app.route("/")
def MsgCreate():
    return render_template("MessageTaker.html")

@app.route("/msgSummiter", methods=["POST","GET"])
def MsgCowpo():
    if request.method=="POST":
        link= random_alphanumeric_string(4)
        cur.execute(f'insert into {config["table"]} values ( "{link}" ,"{request.form["msgBox"]}" , {request.form["counter"]})' )
        connection.commit()
        return f"share this link <a href='http://127.0.0.1:5000/msg/{link}'>http://127.0.0.1:5000/msg/{link}</a>"
    else :
        return "Go Back to work"
    


@app.route("/msg/<msgid>")
def MsgView(msgid):
    print(f'select * from {config["table"]} where link="{msgid}"')
    msgg =cur.execute(f'select * from {config["table"]} where link="{msgid}"')
    d=cur.fetchone()
    cur.execute(f'UPDATE {config["table"]} SET counter = counter  - 1 WHERE  link="{msgid}" AND counter > 0;')
    cur.execute(f'DELETE FROM {config["table"]} WHERE  link="{msgid}" AND counter = 0;')
    connection.commit()
    if d is not None :
        return f"msg is <br><br> {d[1]}"
    return "MSG is Expire or Not Create " 

app.run(port=5000,debug=1)