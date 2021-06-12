from noname import user
from database import Database
import wx


class UserFrame(user):
    def __init__(self, parent=None):
        super(UserFrame, self).__init__(parent)
        self.db = Database()

    def cancel4(self, event):
        self.Close(True)
        exit("Program berhenti")

    def submit4(self, event):
        username= self.m_textCtrl28.GetValue() 
        password = self.m_textCtrl29.GetValue() 

        self.db.query("INSERT INTO user(username, password) VALUES (?, ?)",(username, password))
        self.Close(True)
        wx.MessageDialog(self, "Data Berhasil Disimpan").ShowModal()

    