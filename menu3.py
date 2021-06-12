from noname import menu3
from database import Database
import wx


class Menu3Frame(menu3):
    def __init__(self, parent=None):
        super(Menu3Frame, self).__init__(parent)
        self.db = Database()

    def cancel3(self, event):
        self.Close(True)
        exit("Program berhenti")

    def submit3(self, event):
        kabupaten = self.m_textCtrl16.GetValue() 
        desa = self.m_textCtrl17.GetValue() 
        user = self.m_textCtrl18.GetValue() 
        jalan= self.m_textCtrl19.GetValue() 
        panjang_hp = self.m_textCtrl20.GetValue() 
        alasan1 = self.m_textCtrl21.GetValue() 

        self.db.query("INSERT INTO rusak(n_kabupaten3, n_desa3, n_user3, n_jalan3, panjang_hp, alasan3) VALUES (?, ?, ?, ?, ?, ?)",(kabupaten,desa,user,jalan,panjang_hp,alasan1))
        self.Close(True)
        wx.MessageDialog(self, "Data Berhasil Disimpan").ShowModal()