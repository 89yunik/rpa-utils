import subprocess, win32com.client
from time import sleep
from .etc import kill_task
from .error_handler import error_handler

SAP_TASK_NAME = 'saplogon.exe'

class SAPAutomation:
    def __init__(self):
        self.session = None
        self.shell = None
    
    @error_handler(on_exception=kill_task, task=SAP_TASK_NAME)
    def log_in(self, pw:str, system:str, client:str, user:str) -> str:
        subprocess.check_call(['C:/Program Files (x86)/SAP/FrontEnd/SAPgui/sapshcut.exe',
                               f'-system={system}', f'-client={client}', f'-user={user}', f'-pw={pw}'])
    
        sleep(2)
        sap_gui_auto = win32com.client.GetObject('SAPGUI').GetScriptingEngine
        self.session = sap_gui_auto.findById('con[0]/ses[0]')
        sleep(1)

        log_in_log = "SAP login"
        return log_in_log
    
    @error_handler(updated_exc_message=RuntimeError("Popup window does not exist or is already closed."), exit_program=False)
    def close_popup(self) -> str:
        message_text = self.session.findById("wnd[1]/usr/txtMESSTXT1")
        confirm_button = self.session.findById("wnd[1]/tbar[0]/btn[0]")
        confirm_button.press()

        close_popup_log = "SAP popup closed"
        return close_popup_log
    
    @error_handler(on_exception=kill_task, task=SAP_TASK_NAME)
    def move_tcode(self, tcode:str) -> str:
        tcode_input = self.session.findById('wnd[0]/tbar[0]/okcd')
        search_button = self.session.findById('wnd[0]/tbar[0]/btn[0]')

        tcode_input.text = tcode
        search_button.press()

        move_tcode_log = f"Moved to SAP transaction code {tcode}"
        return move_tcode_log