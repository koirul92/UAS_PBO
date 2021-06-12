from noname import menu2A
from database import Database
import wx


class Menu2AFrame(menu2A):
    def __init__(self, parent=None):
        self.db = Database()
        self.panjangbaris = self.getjumlahdata()
        super(Menu2AFrame, self).__init__(parent,self.panjangbaris)
        self.data2A = self.getdata2A()
        self.setdata2A()
    
    def getjumlahdata(self):
        self.db.query("SELECT COUNT(*) from belumd")
        return self.db.resultOne()

    def getdata2A(self):
        self.db.query("SELECT * from belums")
        return self.db.resultAll()

    def setdata2A(self):
        for i in range (self.panjangbaris[0]) :
            for j in range (7) :
                self.m_grid3.SetCellValue((i,j),str(self.data2A[i][j]))
                

    def kembali1(self, event):
        self.Close(True)