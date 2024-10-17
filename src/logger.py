import logging
import os
from datetime import datetime

# Generate the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Define the log file path
LOG_FILE_PATH = os.path.join(logs_path)

# Set up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
