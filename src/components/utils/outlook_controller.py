import win32com.client as w32
from .etc import close_program

class OutlookController:
    app = w32.gencache.EnsureDispatch('Outlook.Application')

    @staticmethod
    def close(): close_program(program='OUTLOOK.EXE')

    @staticmethod
    def send_mail(to:str, subject:str, contents:str, attachment:str=None, cc:str=None):
        new_mail = OutlookController.app.CreateItem(0)
        new_mail.To = to
        new_mail.Subject = subject
        new_mail.HTMLBody = contents
        if attachment: new_mail.Attachments.Add(attachment)
        if cc: new_mail.CC = cc

        new_mail.Send()