## Mac Setup
* Dev environment: Mac 12.6
* Python 3.9.6
* Homebrew 3.6.3

## Target environment: Raspbian on Raspberry Pi
## Install the older version Buster
https://www.raspberrypi.org/software/operating-systems/

## Link to programming in Python
https://realpython.com/api-integration-in-python/

## Flask is the framework we are using for running the web server
* https://flask.palletsprojects.com/en/2.0.x/installation/
* https://palletsprojects.com/p/flask/

## The web site will use JQuery to make API calls to the Flask server
https://api.jquery.com

## using git
https://docs.github.com/en/get-started/using-git/about-git


# Running

# Get the package from Git first. If git doesnt exist, sudo apt-get install git
```
git clone https://github.com/brianfeinstein/tesla_stem_rov_example.git
```

# May need to install some packages on the Mac or Raspberry Pi like pip/flask/etc. For Mac start with HomeBrew install, then pip, then flask.
```
pip install flask
```

# Code to get this running on a Mac
```
# switch to using puthong 3
python3 -m venv venv 
. venv/bin/activate
# if flask hasnt been installed for python3 then run pip install flask
flask --debug run
http://127.0.0.1:5000/
```

# Code to get this running on Raspberry Pi
```
# switch to using python3
python3 -m venv venv
# before running flask you need to switch to activate python3
. venv/bin/activate
# if flask hasnt been installed for python3 then run pip install flask
pip install flask
# then may need to log out/log back in and re-run the environment activate
flask --debug run --host=0.0.0.0
```

# Webcam install
* https://raspberrypi-guide.github.io/electronics/using-usb-webcams
* https://github.com/jacksonliam/mjpg-streamer/blob/master/mjpg-streamer-experimental/plugins/output_http/README.md
* sudo apt-get install fswebcam


```
# check to see if it shows up
lsusb
dmesg | grep video
v4l2-ctl --list-formats

# test image creation with fswebcam
fswebcam -r 1280x720 -S 30 --no-banner /tmp/image1.jpg

# set up streaming with mjpg_streamer, viewable at http://127.0.0.1:8080/?action=stream
mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so"
```



