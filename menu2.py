from noname import menu2
from database import Database
import wx

class Menu2Frame(menu2):
    def __init__(self, parent=None):
        super(Menu2Frame, self).__init__(parent)
        self.db = Database()

    def cancel2(self, event):
        self.Close(True)
        exit("Program berhenti")

    def submit2(self, event):
        kabupaten = self.m_textCtrl22.GetValue() 
        desa = self.m_textCtrl23.GetValue() 
        user = self.m_textCtrl24.GetValue() 
        jalan = self.m_textCtrl25.GetValue() 
        panjanghb = self.m_textCtrl26.GetValue() 
        alasan1 = self.m_textCtrl27.GetValue() 

        self.db.query("INSERT INTO belumd(n_kabupaten2, n_desa2, n_user2, n_jalan2, panjang_hb, alasan2) VALUES (?, ?, ?, ?, ?, ?)",(kabupaten,desa,user,jalan,panjanghb,alasan1))
        self.Close(True)
        wx.MessageDialog(self, "Data Berhasil Disimpan").ShowModal()

    