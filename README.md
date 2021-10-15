# pitftmanager-web

pitftmanager-web is a Flask web app to control [pitftmanager](https://github.com/tsbarnes/pitftmanager)

## Basics

Simply put, pitftmanager-web is an addon for pitftmanager that allows you to control the screen via a web app, accessible
from any computer on the same network as your Raspberry Pi.

## Installation

*Note: you'll need pitftmanager installed first, see
[the pitftmanager README](https://github.com/tsbarnes/pitftmanager/blob/main/README.md)*

* First, make sure you have `git` and `pip3`
  * On Raspberry Pi OS, use this command:

    ```shell
    sudo apt install git python3-pip
    ```

  * On Arch Linux ARM, use this command:

    ```shell
    sudo pacman -S git python-pip
    ```

  * Second, clone the repository and change directory into it:

```shell
git clone https://github.com/tsbarnes/pitftmanager-web.git ~/pitftmanager-web
cd ~/pitftmanager-web
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
sudo cp ~/pitftmanager-web/pitftmanager-web.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pitftmanager-web
sudo systemctl start pitftmanager-web
```

* Congratulations, you're set up! Now access the web app by visiting your Pi's address in a web browser!
