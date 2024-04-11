from datetime import datetime
from os import path, getcwd
import logging

file_name_datefmt:str = '%Y.%m.%d'
today:str = datetime.today().strftime(file_name_datefmt)
log_dir_name:str = 'log'
log_txt_file_path:str = path.join(getcwd(), log_dir_name, f'{today}.log')

logging.basicConfig(
    filename=log_txt_file_path,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p"
)

logger = logging.getLogger()