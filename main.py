import logging

from login import login
from dashboard import dashboard
from video_stream import video_stream
from logging import log_event

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

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
