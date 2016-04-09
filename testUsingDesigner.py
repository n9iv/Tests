from PyQt4 import QtCore, QtGui
from testDlg_ui import Ui_testDlg

import sys

class testDlgDerived(Ui_testDlg):
    def regEvents(self):
        self.pushButton1.clicked.connect(self.pushButton1_clicked)

    def pushButton1_clicked(self):
        QtGui.QMessageBox.about(QtGui.QWidget(), "Hi","Hii")


app = QtGui.QApplication(sys.argv)
testDlg = QtGui.QDialog()
ui = testDlgDerived() #was: ui = Ui_testDlg()
ui.setupUi(testDlg)
ui.regEvents() # The trick, derive from the designer class and add methods as you wish
testDlg.show()
sys.exit(app.exec_())