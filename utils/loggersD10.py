import logging
import os

def get_logger():
    log_path = "artifacts/logs/test.log"

    os.makedirs("artifacts/logs", exist_ok=True)

    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, mode="w")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger