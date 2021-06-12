from noname import menu1
from database import Database
import wx


class Menu1Frame(menu1):
    def __init__(self, parent=None):
        super(Menu1Frame, self).__init__(parent)
        self.db = Database()

    def cancel1(self, event):
        self.Close(True)
        exit("Program berhenti")

    def submit1(self, event):
        kabupaten = self.m_textCtrl3.GetValue() 
        desa = self.m_textCtrl4.GetValue() 
        user = self.m_textCtrl5.GetValue() 
        jalan = self.m_textCtrl6.GetValue() 
        jalanss = self.m_textCtrl7.GetValue() 
        jalansd = self.m_textCtrl8.GetValue() 
        alasan1 = self.m_textCtrl9.GetValue() 

        self.db.query("INSERT INTO belums(n_kabupaten, n_desa, n_user, n_jalan, panjang_ss, panjang_hs, alasan1) VALUES (?, ?, ?, ?, ?, ?, ?)",(kabupaten,desa,user,jalan,jalanss,jalansd,alasan1))
        self.Close(True)
        wx.MessageDialog(self, "Data Berhasil Disimpan").ShowModal()
