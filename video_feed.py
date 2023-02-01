import cv2
import datetime
import csv

def video_feed_simulation():
    video = cv2.VideoCapture("video.mp4")
    
    while True:
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
        cv2.imshow("Simulated video feed", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()
