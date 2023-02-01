import os
from flask import Flask
import cv2
import datetime
import csv
from login import login
from dashboard import dashboard
from video_feed import video_feed_simulation
from logging import log_information

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(dashboard)

if __name__ == "__main__":
    video_feed_simulation()
    app.run(debug=False)
