import logging
import posix_ipc
from flask import Flask, render_template, flash, redirect

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
    return redirect('/')


@app.route('/previous')
def previous():
    mq.send("previous", timeout=10)
    flash("Sent 'previous' message to epdtext")
    return redirect('/')


@app.route('/button0')
def button0():
    mq.send("button0", timeout=10)
    flash("Sent 'KEY1' message to epdtext")
    return redirect('/')


@app.route('/button1')
def button1():
    mq.send("button1", timeout=10)
    flash("Sent 'KEY2' message to epdtext")
    return redirect('/')


@app.route('/button2')
def button2():
    mq.send("button2", timeout=10)
    flash("Sent 'KEY3' message to epdtext")
    return redirect('/')


@app.route('/button3')
def button3():
    mq.send("button3", timeout=10)
    flash("Sent 'KEY4' message to epdtext")
    return redirect('/')


@app.route('/reload')
def reload():
    mq.send("reload", timeout=10)
    flash("Sent 'reload' message to epdtext")
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
