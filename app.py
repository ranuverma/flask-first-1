from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/test")
def test():
    a=6
    b=5
    c=a+b
    return "given that : a = {} , b ={} \n , so Sum of 'a' and 'b' ={}".format(a,b,c)

@app.route("/test2")
def test2():
    data=request.args.get("x")
    return "the output from the URL is {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
