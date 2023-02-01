from login import login
from dashboard import dashboard
from video_stream import video_stream

def main():
    # Login page
    is_logged_in = login()
    
    if is_logged_in:
        dashboard()
        video_stream()

if __name__ == "__main__":
    main()
