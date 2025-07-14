# Mock bootstrap for development (original dependencies unavailable)
import logging
from pathlib import Path

# Simple logger mock
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Simple messenger mock
def messenger(section, code):
    return f"[{section}:{code}] Task executed"

# Mock settings
class Settings:
    pass

settings = Settings()
