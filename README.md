## Mac Setup
* Dev environment: Mac 12.6
* Python 3.9.6
* Homebrew 3.6.3

## Target environment: Raspbian on Raspberry Pi
https://www.raspberrypi.org/software/operating-systems/

## Link to programming in Python
https://realpython.com/api-integration-in-python/

## Flask is the framework we are using for running the web server
* https://flask.palletsprojects.com/en/2.0.x/installation/
* https://palletsprojects.com/p/flask/

## The web site will use JQuery to make API calls to the Flask server
https://api.jquery.com

## video capture
* https://www.linux-projects.org/uv4l/tutorials/
* https://www.linux-projects.org/uv4l/installation/
* https://www.linux-projects.org/uv4l/tutorials/streaming-server/

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
python3 -m venv venv 
. venv/bin/activate
flask --debug run
http://127.0.0.1:5000/
```

# Code to get this running on Raspberry Pi
```
/home/pi/.local/bin/flask --debug run --host=0.0.0.0
```




