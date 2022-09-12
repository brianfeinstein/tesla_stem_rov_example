# this should run on the raspberry pi
from flask import Flask, escape, request, render_template, jsonify
from pprint import pprint, pformat

app = Flask(__name__)

@app.route("/")
def index():
    app.logger.debug("index called, returning template")
    return render_template("index.html")

#
# the main api that takes in a form from the web side
# looks for the "direction" element in the form
# and then calls a corresponding controller function based on the input
# 
#

@app.route("/direction", methods=["POST"])
def direction():
    posted_data = request.get_json()
    app.logger.debug("direction called with post contents: " + pformat(posted_data))
    direction = posted_data["go"]
    
    if(direction == "left"):
        return go_left()
    elif(direction == "right"):
        return go_right()
    elif(direction == "up"):
        return go_up()
    elif(direction == "down"):
        return go_down()
    else:
        return {"message": "bad direction sent: " + pformat(posted_data),
                "success": False}

#
# controller functions based on what direction was posted to the API
# each of these:
# - sends some logging info
# - should then do something with the ROV itself
# - returns a JSON set of information back to the webside
#   - in this example, it sends back: a message, a success boolean,
#     and a relative position in x/y
#
def go_left():
    app.logger.debug("go_left() called")
    # do something with ROV here
    return {"message": "successfully went left",
            "success": True,
            "x_position": -1,
            "y_position": 0}
    
def go_right():
    app.logger.debug("go_right() called")
    # do something with ROV here
    return {"message": "successfully went right",
            "success": True,
            "x_position": 1,
            "y_position": 0}
    
def go_up():
    app.logger.debug("go_up() called")
    # do something with ROV here
    return {"message": "successfully went up",
            "success": True,
            "x_position": 0,
            "y_position": 1}

def go_down():
    app.logger.debug("go_down() called")
    # do something with ROV here
    return {"message": "successfully went down",
            "success": True,
            "x_position": 0,
            "y_position": -1}
