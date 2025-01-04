import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# Iestatam zurnalesanas failu
log_file = 'logs.log'
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Formatejam zurnalesanas faila aprīkotāju?
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Pievienojam zurnalesanas failu pie zuranletaja
logger.addHandler(file_handler)