from sys import argv
from functools import partial
from time import sleep
from os import path

from components.utils.error_handler import error_handler
from components.utils.etc import delete_expired_files, kill_tasks
# from components.utils.outlook_controller import OutlookAutomation
from components.utils.chrome_automation import ChromeAutomation
import config

dev_mail = config.DEV_MAIL
error_mail_subject = config.ERROR_MAIL_SUBJECT
error_mail_contents = config.ERROR_MAIL_CONTENTS

# send_mail_error_handler:partial = partial(error_handler, on_exception=OutlookAutomation.send_mail, to=dev_mail, subject=error_mail_subject, contents=error_mail_contents)

@error_handler()
# @send_mail_error_handler()
def rpa_main(): 
    ref_dir:str = config.REF_DIR
    log_dir:str = config.LOG_DIR
    
    try: delete_expired_files(dir=log_dir, expiration_period=30)
    except: pass
    kill_tasks([])

    if len(argv)>1:
        for user_inputs in argv[1:]: print(user_inputs)

    # chrome_driver_path = path.join(ref_dir, 'chromedriver.exe')
    # naver_url = "https://www.naver.com"

    # chrome_test = ChromeAutomation()
    # chrome_test.start_browser(driver_path=chrome_driver_path)
    # chrome_test.open_url(url=naver_url)
    # chrome_test.control_elements_by_xpath({'//*[@id="query"]':'test'})
    # sleep(5)

    rpa_main_log = 'Program exited'
    return rpa_main_log

if __name__=="__main__": rpa_main()