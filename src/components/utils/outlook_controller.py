import win32com.client as w32
from .etc import close_program
from .error_handler import error_handler

class OutlookController:
    app = w32.gencache.EnsureDispatch('Outlook.Application')

    @staticmethod
    @error_handler()
    def close(): close_program(program='OUTLOOK.EXE')

    @staticmethod
    @error_handler()
    def send_mail(to:str, subject:str, contents:str, attachment:str=None, cc:str=None):
        new_mail = OutlookController.app.CreateItem(0)
        new_mail.To = to
        new_mail.Subject = subject
        new_mail.HTMLBody = contents
        if attachment: new_mail.Attachments.Add(attachment)
        if cc: new_mail.CC = cc

        new_mail.Send()