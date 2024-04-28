from functools import partial

from components.utils.error_handling import error_handler
from components.utils.etc import delete_expired_files, close_programs
from components.utils.outlook_control import Outlook
import config

dev_mail = config.DEV_MAIL
error_mail_subject = config.ERROR_MAIL_SUBJECT
error_mail_contents = config.ERROR_MAIL_CONTENTS

send_mail_error_handler:partial = partial(error_handler, on_exception=Outlook.send_mail, to=dev_mail, subject=error_mail_subject, contents=error_mail_contents)

# @error_handler()
@send_mail_error_handler()
def rpa_main(): 
    ref_dir:str = config.REF_DIR
    log_dir:str = config.LOG_DIR
    
    try: delete_expired_files(dir=log_dir, expiration_period=30)
    except: pass
    close_programs([])

if __name__=="__main__": rpa_main()