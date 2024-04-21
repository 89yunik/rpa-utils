from os import path, getcwd, pardir

SRC_DIR:str = path.dirname(path.abspath(__file__))
REF_DIR:str = path.abspath(path.join(SRC_DIR, pardir, '1. 참고자료'))
LOG_DIR:str = path.join(getcwd(), 'log')

DEV_MAIL:str = 'dev_mail@example.com'
ERROR_MAIL_SUBJECT:str = '[example RPA] 에러'
ERROR_MAIL_CONTENTS:str = ''