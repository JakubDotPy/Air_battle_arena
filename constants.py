# ==============================================================================
#  Copyright
#  Dogfight Arena
#  Version: 13.04.20 13:39
#  Author: Jakub Cervinka
# ==============================================================================
import logging.config
import os

CWD = os.getcwd()
os.makedirs(os.path.join(CWD, 'logs'), exist_ok=True)


class ProdFormatter(logging.Formatter):
    """filter to modify log record for use in production

    uses '- %(message)s'
    if the record is BANNER then '%(message)s'
    """

    banner_fmt = '%(message)s'

    def __init__(self):
        super().__init__(fmt='- %(message)s', datefmt=None, style='%')

    def format(self, record):
        format_orig = self._style._fmt

        # formatter for banner
        if len(record.msg) > 150:
            self._style._fmt = self.banner_fmt

        # Call the original formatter to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format
        self._style._fmt = format_orig

        return result

LOGGER_NAME = 'air_battle'
LOG_CONF = {
    'version'   : 1,
    'formatters': {
        'verbose'   : {
            'format': '%(asctime)s %(levelname)-8s %(funcName)-18s %(message)s'
            },
        'simple'    : {
            'format': '%(levelname)-8s %(message)s'
            },
        'production': {
            '()': ProdFormatter,
            },
        },
    'handlers'  : {
        'console_hand' : {
            'class'    : 'logging.StreamHandler',
            'stream'   : 'ext://sys.stdout',
            'level'    : 'DEBUG',
            'formatter': 'verbose',  # TODO: change this to production
            },
        'file_hand_rot': {
            'class'      : 'logging.handlers.RotatingFileHandler',
            'filename'   : os.path.join(CWD, 'logs', 'air.log'),
            'encoding'   : 'utf-8',
            'maxBytes'   : 3_145_728,  # 3MB
            'backupCount': 5,  # five files with log backup
            'level'      : 'DEBUG',
            'formatter'  : 'verbose',
            },
        'file_err_hand': {
            'class'    : 'logging.FileHandler',
            'filename' : os.path.join(CWD, 'logs', 'air_ERROR.log'),
            'encoding' : 'utf-8',
            'level'    : 'ERROR',
            'formatter': 'verbose',
            },
        },
    'loggers': {
        LOGGER_NAME: {
            'handlers': ['console_hand', 'file_hand_rot', 'file_err_hand'],
            'level'   : 'DEBUG',
            },
        },
    }
logging.config.dictConfig(LOG_CONF)
logging.getLogger(LOGGER_NAME).setLevel(logging.DEBUG)

BANNER_START = r"""
 █████╗ ██╗██████╗     ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██║██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
███████║██║██████╔╝    ██████╔╝███████║   ██║      ██║   ██║     █████╗  
██╔══██║██║██╔══██╗    ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██║  ██║██║██║  ██║    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
"""

BANNER_END = r"""
    ___ ___ _  _ ___ ___ _  _ ___ ___  
   | __|_ _| \| |_ _/ __| || | __|   \ 
   | _| | || .` || |\__ \ __ | _|| |) |
   |_| |___|_|\_|___|___/_||_|___|___/      in {sec}s
 """
BANNER_ERROR = r"""
   ▓█████  ██▀███   ██▀███   ▒█████   ██▀███  
   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
   ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  
   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
      ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ 
      ░  ░   ░        ░         ░ ░     ░     
"""

