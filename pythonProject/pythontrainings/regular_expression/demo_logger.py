import logging

# Create and configure logger
logging.basicConfig(encoding='utf-8',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
logging.critical("Its a serious error")
