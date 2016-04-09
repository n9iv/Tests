from PyQt4 import QtCore, QtGui
from wzSelectComponent_ui import Ui_WizardPage
import sys


class selectComponent(Ui_WizardPage):
    def regEvents(self):
        self.componentsList.itemSelectionChanged.connect(self.componentChanged)



    def componentChanged(self):
        si = self.componentsList.selectedItems()
        name = si[0].text()
        self.componentImage.setPixmap(QtGui.QPixmap("r\\"+name+".png"))

app = QtGui.QApplication(sys.argv)
testDlg = QtGui.QDialog()
ui = selectComponent() #was: ui = Ui_testDlg()
ui.setupUi(testDlg)
ui.regEvents() # The trick, derive from the designer class and add methods as you wish
testDlg.show()
sys.exit(app.exec_())