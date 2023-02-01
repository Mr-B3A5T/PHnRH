import logging

def log_information(info):
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info(info)
'''
V
'''