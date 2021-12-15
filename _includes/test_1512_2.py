
from flask import Flask, render_template
from testCopy1 import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index_1512_2.html")

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return render_template("index_1512_2.html", content=function_test())

if __name__ == '__main__':
  app.run(debug=True)
