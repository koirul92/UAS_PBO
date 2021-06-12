from noname import menu3A
from database import Database
import wx

class Menu3AFrame(menu3A):
    def __init__(self, parent=None):
        self.db = Database()
        self.panjangbaris = self.getjumlahdata()
        super(Menu3AFrame, self).__init__(parent,self.panjangbaris)
        self.data3A = self.getdata3A()
        self.setdata3A()
    
    def getjumlahdata(self):
        self.db.query("SELECT COUNT(*) from rusak")
        return self.db.resultOne()

    def getdata3A(self):
        self.db.query("SELECT * from rusak")
        return self.db.resultAll()

    def setdata3A(self):
        for i in range (self.panjangbaris[0]) :
            for j in range (7) :
                self.m_grid5.SetCellValue((i,j),str(self.data3A[i][j]))
                

    def kembali1(self, event):
        self.Close(True)