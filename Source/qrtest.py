import qrcode
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world(name="Napat"):
    return 'Hello %s!' % name

if __name__=='__main__':
   app.run(debug = True)