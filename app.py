import logging
import posix_ipc
from flask import Flask, render_template, flash, redirect, request

from system import System


app = Flask(__name__)
app.config.from_pyfile("app.cfg")
try:
    mq = posix_ipc.MessageQueue("/pitftmanager_ipc")
    mq.block = False
except posix_ipc.PermissionsError:
    logging.error("couldn't open message queue")
    exit(1)


@app.route('/')
def index():
    return render_template('index.html', system=System)


@app.route('/next_app')
def next_app():
    mq.send("next", timeout=10)
    flash("Sent 'next' message to pitftmanager")
    return redirect('/')


@app.route('/previous_app')
def previous_app():
    mq.send("previous", timeout=10)
    flash("Sent 'previous' message to pitftmanager")
    return redirect('/')


@app.route('/switch_app')
def switch_app():
    app_name = request.args.get('app')
    mq.send("switch_app " + app_name, timeout=10)
    flash("Sent 'switch_app' message to pitftmanager")
    return redirect('/')


@app.route('/load_app')
def load_app():
    app_name = request.args.get('app')
    mq.send("load_app " + app_name, timeout=10)
    flash("Sent 'load_app' message to pitftmanager")
    return redirect('/')


@app.route('/remove_app')
def remove_app():
    app_name = request.args.get('app')
    mq.send("remove_app " + app_name, timeout=10)
    flash("Sent 'remove_app' message to pitftmanager")
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
