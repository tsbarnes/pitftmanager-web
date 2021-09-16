import logging
import posix_ipc
from flask import Flask, render_template, flash

app = Flask(__name__)
app.config.from_pyfile("app.cfg")
try:
    mq = posix_ipc.MessageQueue("/epdtext_ipc")
    mq.block = False
except posix_ipc.PermissionsError:
    logging.error("couldn't open message queue")
    exit(1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/next')
def next():
    mq.send("next", timeout=10)
    flash("Sent 'next' message to epdtext")
    return render_template('index.html')


@app.route('/previous')
def previous():
    mq.send("previous", timeout=10)
    flash("Sent 'previous' message to epdtext")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
