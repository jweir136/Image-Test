import flask
from datetime import datetime

IMG_URL = "image.png"
app = flask.Flask(__name__)

@app.route("/")
def index():
    print("\t[+] Page was visited at {}".format(datetime.now()))
    return flask.send_file(IMG_URL, mimetype='image/png')

if __name__ == "__main__":
    app.run()