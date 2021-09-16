import logging
import posix_ipc
from flask import Flask, render_template

app = Flask(__name__)
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
    return render_template('index.html')


@app.route('/previous')
def previous():
    mq.send("previous", timeout=10)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
