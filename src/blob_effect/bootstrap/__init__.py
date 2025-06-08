from pathlib import Path
from nglcobdai_utils import Messenger, ConsoleHandlerInfo, Settings, get_logger

settings = Settings()

logger = get_logger(settings.PROJECT_NAME, ch_info=ConsoleHandlerInfo())

messenger = Messenger(Path(__file__).parent.parent / "config" / "message.ini")
