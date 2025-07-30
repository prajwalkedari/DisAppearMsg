from flask import Flask, render_template,request
import json 
import random
import string
from dotenv import dotenv_values
config=dotenv_values(".env")
app = Flask(__name__)

def random_alphanumeric_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def GetMsg(id):
    with open(config["file"], "r+") as file:
        data = json.load(file)
        # link : [msg ,1]
        DL =data.get(id)
        if DL is None :
            return "MSG EXPIRE (404 Not Found )"
        if DL[1] <= 1:
            data.pop(id)
        else:
            data[id][1] -= 1
        msg = DL[0]
        print(DL,data)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        if DL[1] == 0:
            return "MSG EXPIRE"
        return f"Msg is :::= >{msg}"


        




with open("data.json", "r") as file:
    data = json.load(file)
@app.route("/")
def hello_world():
    return render_template("MessageTaker.html")


@app.route("/msgSummiter", methods=["GET","POST"])
def MsgTaker():
    if request.method =="POST":
        msg = request.form["msgBox"]
        counter = request.form["counter"]
        link= random_alphanumeric_string(4)
        data[link]=[msg,int(counter)] 
        with open("data.json", "w") as file:
          json.dump(data, file, indent=4)
        return f"this an link Can Fowrad (OneView) <BR><BR> <a href='http://127.0.0.1:5000/Msg/{link}'>http://127.0.0.1:5000/Msg/{link}<a> <br> By Prajwal"
    return "<h1>THIS NOT FOR VIST<h1>"


@app.route("/Msg/<id>")
def MsgShower(id):

    return GetMsg(id)

app.run(debug=True,port=5000)