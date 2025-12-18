import logging
import sys
import os

def get_logger(name: str) -> logging.Logger: # Get configured logger
    logger = logging.getLogger(name) # Create logger instance

    if logger.handlers: # If handlers already exist, return the logger
        return logger # Return existing logger

    logger.setLevel(logging.INFO) # Set log level to INFO

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    ) # Define log format

    # ✅ Console handler (works everywhere)
    console_handler = logging.StreamHandler(sys.stdout) # Console handler
    console_handler.setFormatter(formatter) # Set formatter
    logger.addHandler(console_handler) # Add console handler to logger

    # ✅ File handler ONLY for local (NOT Vercel)
    if not os.getenv("VERCEL"): # Check if not running on Vercel
        from pathlib import Path # Import Path for directory handling
        LOG_DIR = Path("logs") # Define logs directory
        LOG_DIR.mkdir(exist_ok=True) # Create logs directory if not exists
        file_handler = logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8") # File handler
        file_handler.setFormatter(formatter) # Set formatter
        logger.addHandler(file_handler) # Add file handler to logger

    logger.propagate = False # Disable propagation to root logger
    return logger # Return configured logger
