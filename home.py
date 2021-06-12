from noname import home1
from menu1 import Menu1Frame
from menu2 import Menu2Frame
from menu3 import Menu3Frame

class HomeFrame(home1):
    def __init__(self, parent=None):
        super(HomeFrame, self).__init__(parent)
    def usermenu1(self, event):
        menu1Frame = Menu1Frame(None)
        menu1Frame.Show()
    def usermenu2(self, event):
        menu2Frame = Menu2Frame(None)
        menu2Frame.Show()
    def usermenu3(self, event):
        menu3Frame = Menu3Frame(None)
        menu3Frame.Show()
    def exit1(self,event):
        self.Close(True)
        exit("Program berhenti")
