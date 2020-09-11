import math
from flask import Flask
from flask import render_template ,url_for,request
app= Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/infix" ,methods=['GET','POST'])
def infix():
    return render_template('infix.html',ans="")


@app.route("/postfix" ,methods=['GET','POST'])
def postfix():
    return render_template('postfix.html',ans="")


@app.route("/prefix" ,methods=['GET','POST'])
def prefix():
    return render_template('prefix.html',ans="")


@app.route("/ans1", methods=["GET","POST"])
def ans1():
    if request.method=="POST":
        exp=request.form["display"]

    return render_template('infix.html',ans=evaluate(exp))

def evaluate(str):
    return eval(str,{'cos':math.cos,'sin':math.sin,'tan':math.tan,'log10':math.log10,'ln':math.log, 'sqrt':math.sqrt, 'POW': math.pow, 'arccos': math.acos, 'arcsin': math.asin, 'arctan': math.atan, 'pi': math.pi, 'fact': math.factorial, 'rad': math.radians, 'deg': math.degrees })


@app.route("/ans2",methods=["GET","POST"])
def ans2():
    if request.method=="POST":
        exp2=request.form["display"]

    obj = Evaluate(len(exp2))
    return render_template('postfix.html',answer=obj.evaluatePostfix(exp2))







if __name__ == '__main__':
    app.run(debug=True)
