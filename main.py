import logging

from login import login
from dashboard import dashboard
from video_stream import video_stream

def log_event(event_message):
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info(event_message)

def main():
    # Login page
    is_logged_in = login()
    
    if is_logged_in:
        log_event("User logged in")
        dashboard()
        video_stream()
    else:
        log_event("Login failed")

if __name__ == "__main__":
    main()
