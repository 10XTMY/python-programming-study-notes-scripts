import logging
import logging_logger  # when doing this by default it creates a heirarchy and all messages
# are propagated to the base logger, to stop this set propagation to False in logger

# https://docs.python.org/3.7/library/logging.html#logging.basicConfig
# by default it prints the name as root
# it is best practice to create your own logger instead, see logging_logger.py
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:S')  # attributes found in documentation url above

# 5 different log levels
logging.debug('debug message')
logging.info('info message')
# only below are printed to console by default
# to change which logging levels are printed to console
# you need to edit the basicConfig (see above)
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# log handlers dispatch the appropriate log message to the handler's specific destination
# (std output, files, http, email etc)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# set level and format for each handler
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# create the formatter for each handler
stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# set the formatters for each handler
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

# add the handlers to the desired logger
logging_logger.logger.addHandler(stream_handler)
logging_logger.logger.addHandler(file_handler)

# test the logger
# logging_logger.logger.warning('this is a warning')
# logging_logger.logger.error('this is an error')

logger = logging_logger.logger

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logger.error(e, exc_info=True)  # exc True includes stack trace in logger

# if you want to catch all and still include the stack trace
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logger.error('Error: %s', traceback.format_exc())  # exc True includes stack trace in logger

# for large applications that require a lot of logs, use a rotating file handler to keep them small and tidy
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
handler = RotatingFileHandler('rotating.log', maxBytes=2000, backupCount=5)  # keeps 5 backup files
logger.addHandler(handler)

i = 0
for _ in range(10000):

    logger.info(f'rotating file handler test {i}')
    i += 1

# if application runs for a long time use a timed rotating file handler
# s, m, h, d, midnight, w0, w1 (mondey, tuesday... w7 sunday)
timed_handler = TimedRotatingFileHandler('timedRotating.log', when='s', interval=5, backupCount=5)
logger.addHandler(timed_handler)
import time

for _ in range(6):
    logger.info('rotating test')
    time.sleep(5)

# see python-json-logger for json logging

