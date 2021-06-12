from noname import menu1A

from database import Database
import wx


class Menu1AFrame(menu1A):
    def __init__(self, parent=None):
        self.db = Database()
        self.panjangbaris = self.getjumlahdata()
        super(Menu1AFrame, self).__init__(parent,self.panjangbaris)
        self.data1A = self.getdata1A()
        self.setdata1A()
    
    def getjumlahdata(self):
        self.db.query("SELECT COUNT(*) from belums")
        return self.db.resultOne()

    def getdata1A(self):
        self.db.query("SELECT * from belums")
        return self.db.resultAll()

    def setdata1A(self):
        for i in range (self.panjangbaris[0]) :
            for j in range (8) :
                self.m_grid1.SetCellValue((i,j),str(self.data1A[i][j]))
                

    def kembali1(self, event):
        self.Close(True)