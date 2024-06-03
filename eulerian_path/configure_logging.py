import logging
from pathlib import Path

log_file_path = Path("log_file.txt")

def setup_logging(log_file_path=log_file_path):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler(log_file_path, mode="w")]
    )