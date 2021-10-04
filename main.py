import flask

IMG_URL = "image.png"
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.send_file(IMG_URL, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="10.215.178.236")