## logger

import os
import sys
import logging
import inspect

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # , mode="a"),
        logging.StreamHandler(sys.stdout),
    ],
)

s = inspect.stack()
name = os.path.normpath(s[0].filename).split(os.sep)[-2]
logger = logging.getLogger(name)
