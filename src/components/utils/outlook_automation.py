from typing import Union
import win32com.client
from .error_handler import error_handler

class OutlookAutomation:
    def __init__(self) -> None:
        self.outlook: win32com.client.Dispatch = win32com.client.Dispatch("Outlook.Application")
        self.namespace: win32com.client.CDispatch = self.outlook.GetNamesapce("MAPI")
    
    @error_handler()
    def send_email(self, to:str, subject:str, body:str, attachment:Union[str, None] = None, cc:Union[str, None] = None):
        new_mail: win32com.client.CDispatch = self.outlook.CreateItem(0)
        new_mail.To = to
        new_mail.Subject = subject
        new_mail.Body = body
        if attachment: new_mail.Attachments.Add(attachment)
        if cc: new_mail.CC = cc

        new_mail.Send()

        send_email_log = f"Email sent to: {to}"
        return send_email_log
    
    @error_handler()
    def quit_outlook(self) -> str:
        self.outlook.Quit()
        
        quit_outlook_log = "Outlook closed"
        return quit_outlook_log