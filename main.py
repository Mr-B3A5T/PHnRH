import logging
import logging as log

from login import login
from dashboard import dashboard
from video_stream import video_stream
from logging import log_event

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# ... Rest of the code
