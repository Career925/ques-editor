from flask import Flask,render_template,request,redirect
from urllib.parse import urlencode
import requests

def enc(q):
  urlencode(q)

app = Flask("app")

apiUrl = "https://vinayak341.pythonanywhere.com"

@app.route("/")
def home():
  ques = requests.get(apiUrl+"/get-all-questions").json()

  return render_template("index.html",ques = ques)

@app.route("/remove")
def remove():
  ques = request.args.get('q')
  print(ques)

  res = requests.post(apiUrl+f"/rm-question?ques={ques}").json()

  print("response :: ",res)

  return redirect("/")

@app.route("/add")
def add_page():
  return render_template("add.html")

@app.route("/add-question",methods=['POST'])
def add():
  cont = request.form

  requests.post(apiUrl+f"/add-question?ques={cont['ques']}&ans={cont["ans"]}")

  return redirect("/")

app.run("0.0.0.0","5745")