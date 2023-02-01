import cv2
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    video_capture = cv2.VideoCapture("fake_cctv_feed.mp4")
    ret, frame = video_capture.read()
    while ret:
        ret, frame = video_capture.read()
    return frame.tobytes()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
