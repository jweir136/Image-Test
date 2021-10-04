import flask
from flask import request
from datetime import datetime

IMG_URL = "image.png"
app = flask.Flask(__name__)

@app.route("/")
def index():
    print("\t[+] Page was visited at {} from {}".format(datetime.now(), request.environ.get('HTTP_X_REAL_IP', request.remote_addr)))
    return flask.send_file(IMG_URL, mimetype='image/png')

if __name__ == "__main__":
    app.run()