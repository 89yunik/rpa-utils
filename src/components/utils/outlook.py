import win32com.client as w32
from .etc import close_program

def close_outlook(): close_program(program='OUTLOOK.EXE')

class Outlook:
    def __init__(self): self.open()

    def open(self): self.outlook = w32.gencache.EnsureDispatch('Outlook.Application')

    @staticmethod
    def close(): close_outlook()

    def send_mail(self, to:str, subject:str, contents:str, attachment:str=None, cc:str=None):
        new_mail = self.outlook.CreateItem(0)
        new_mail.To = to
        new_mail.Subject = subject
        new_mail.HTMLBody = contents
        if attachment: new_mail.Attachments.Add(attachment)
        if cc: new_mail.CC = cc

        new_mail.Send()

    # def delete_mail(self, condition:str):
    #     folder_length:int = len(self.outlook.Folders)
    #     for i in range(1, folder_length + 1):
    #         root_folder = self.outlook.Folders.Item(i)
    #         for sub_folder in reversed(root_folder.Folders):
    #             for mail in reversed(sub_folder.Items):
    #                 try:
    #                     if condition(mail.Sender): mail.Delete()
    #                 except: pass