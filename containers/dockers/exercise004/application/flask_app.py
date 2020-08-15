from flask import Flask
import os,sys

app = Flask(__name__)

@app.route('/welcome/<fname>/<lname>')
def hello_world(fname,lname):
  return {True:"Hello There! {} {}!! How are you !  Welcome to Docker!".format(fname,lname)}

if __name__ == "__main__":
    print(os.environ['CODER'])
    app.run(host=os.environ['FLASKHOSTNAME'],port=os.environ['FLASKPORT'],debug=True)