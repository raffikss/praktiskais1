import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# Configuring logging file
log_file = 'logs.log'
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

#Formating logging file formater?
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

#Adding logging file to the logger
logger.addHandler(file_handler)