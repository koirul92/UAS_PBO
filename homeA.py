from noname import home2
from user import UserFrame
from menu1A import Menu1AFrame
from menu2A import Menu2AFrame
from menu3A import Menu3AFrame

class HomeFrame2(home2):
    def __init__(self, parent=None):
        super(HomeFrame2, self).__init__(parent)
    def adduser(self, event):
        userFrame = UserFrame(None)
        userFrame.Show()
    def adminmenu1(self, event):
        menu1AFrame = Menu1AFrame(None)
        menu1AFrame.Show()
    def adminmenu2(self, event):
        menu2AFrame = Menu2AFrame(None)
        menu2AFrame.Show()
    def adminmenu3(self, event):
        menu3AFrame = Menu3AFrame(None)
        menu3AFrame.Show()
    def exitadmin(self,event):
        self.Close(True)
        exit("Program berhenti")
