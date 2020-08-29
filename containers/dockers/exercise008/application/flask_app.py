from flask import Flask
import os,sys
import mongo_app

app = Flask(__name__)

@app.route('/')
def hello():
  return {True:"Hello There! Welcome to K8s!"}

@app.route('/welcome/<fname>/<lname>')
def hello_world(fname,lname):
  return {True:"Hello There! {} {}!! How are you !  Welcome to Docker!".format(fname,lname)}

@app.route('/hello_mongo/')
def hello_mongo_app():
    print("hello_mongo .... ")
    try:
        return {"result":mongo_app.driver()}
        #return {"result":"Arun is the host!!"}
    except Exception as err:
        return {"result":"Failed"}

if __name__ == "__main__":
    app.run(host=os.environ['FLASKHOSTNAME'],port=os.environ['FLASKPORT'],debug=True)
