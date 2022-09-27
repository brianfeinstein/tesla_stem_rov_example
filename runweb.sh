#!/bin/bash
python3 -m venv venv
. venv/bin/activate
flask --debug run --host=0.0.0.0
