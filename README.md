# epdtext-web

epdtext-web is a Flask web app to control [epdtext](https://github.com/tsbarnes/epdtext)

## Basics

Simply put, epdtext-web is an addon for epdtext that allows you to control the screen via a web app, accessible
from any computer on the same network as your Raspberry Pi.

## Installation

*Note: you'll need epdtext installed first, see
[the epdtext README](https://github.com/tsbarnes/epdtext/blob/main/README.md)*

* First, make sure you have `git` and `pip3` using this command:

```shell
sudo apt install git python3-pip
```

* Second, clone the repository and change directory into it:

```shell
git clone https://github.com/tsbarnes/epdtext-web.git /home/pi/epdtext-web
cd /home/pi/epdtext-web
```

* Third, install the Python dependencies:

```shell
sudo pip3 install -r requirements.txt
```

* Fourth, configure your secret key by creating `app.cfg` with the following contents:

```python
SECRET_KEY = "<your secret key here>"
```

* You can generate a new secret key with this command:

```shell
python -c 'import os; print(os.urandom(16))'
```

* Last, copy the service file and start the server:

```shell
sudo cp /home/pi/epdtext-web/epdtext-web.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable epdtext-web
sudo systemctl start epdtext-web
```

* Congratulations, you're set up! Now access the web app by visiting your Pi's address in a web browser!
