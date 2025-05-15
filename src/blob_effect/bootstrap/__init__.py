from nglcobdai_utils import Messenger, RotatingFileHandlerInfo, Settings, get_logger

settings = Settings()

_fh = RotatingFileHandlerInfo(
    log_level=settings.LOG_LEVEL,
    filename=settings.LOG_PATH,
    max_bytes=settings.MAX_BYTES,
    backup_count=settings.BACKUP_COUNT,
)
logger = get_logger(settings.PROJECT_NAME, fh_info=_fh)

messenger = Messenger("src/config/message.ini")
