# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testDlg.ui'
#
# Created: Fri Jan 29 20:54:36 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_testDlg(object):
    def setupUi(self, testDlg):
        testDlg.setObjectName(_fromUtf8("testDlg"))
        testDlg.resize(394, 154)
        self.horizontalLayout = QtGui.QHBoxLayout(testDlg)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton1 = QtGui.QPushButton(testDlg)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.horizontalLayout.addWidget(self.pushButton1)

        self.retranslateUi(testDlg)
        QtCore.QMetaObject.connectSlotsByName(testDlg)

    def retranslateUi(self, testDlg):
        testDlg.setWindowTitle(_translate("testDlg", "Dialog", None))
        self.pushButton1.setText(_translate("testDlg", "לחץ פה", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testDlg = QtGui.QDialog()
    ui = Ui_testDlg()
    ui.setupUi(testDlg)
    testDlg.show()
    sys.exit(app.exec_())

