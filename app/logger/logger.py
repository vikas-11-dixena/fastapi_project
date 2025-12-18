import logging
import sys
from pathlib import Path

# =========================
# Logs directory & file
# =========================
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Prevent duplicate handlers (important)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # =========================
    # Console Handler (stdout)
    # =========================
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # =========================
    # File Handler (logs/app.log)
    # =========================
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # =========================
    # Attach handlers
    # =========================
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Prevent log duplication from root logger
    logger.propagate = False

    return logger
