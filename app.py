from flask import Flask, render_template
import random as r

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/o-meni")
def about():
    return render_template("about.html")

#met kocke
@app.route("/kocka")
def dice():
    rnd = r.randint(1,6)
    return render_template("dice.html", kocka = rnd )



@app.route("/kocka/<N>")
def dice2(N):
    rnd = r.randint(1,int(N))
    return render_template("dice.html", kocka = rnd )


#ljubezen
@app.route("/ljubezen")
def ljubezen():
    listM=[]
    rnd = r.randint(1,20)
    return render_template("ljubezen.html", kocka = rnd )

app.run(debug=True)