# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wzSelectComponent.ui'
#
# Created: Sat Jan 30 09:37:08 2016
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(615, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WizardPage.sizePolicy().hasHeightForWidth())
        WizardPage.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(WizardPage)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtGui.QFrame(WizardPage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.componentsList = QtGui.QListWidget(WizardPage)
        self.componentsList.setObjectName(_fromUtf8("componentsList"))
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.componentsList.addItem(item)
        self.horizontalLayout.addWidget(self.componentsList)
        self.componentImage = QtGui.QLabel(WizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.componentImage.sizePolicy().hasHeightForWidth())
        self.componentImage.setSizePolicy(sizePolicy)
        self.componentImage.setText(_fromUtf8(""))
        self.componentImage.setPixmap(QtGui.QPixmap(_fromUtf8("Clock.png")))
        self.componentImage.setObjectName(_fromUtf8("componentImage"))
        self.horizontalLayout.addWidget(self.componentImage)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        __sortingEnabled = self.componentsList.isSortingEnabled()
        self.componentsList.setSortingEnabled(False)
        item = self.componentsList.item(0)
        item.setText(_translate("WizardPage", "Clock", None))
        item = self.componentsList.item(1)
        item.setText(_translate("WizardPage", "Small Switch", None))
        item = self.componentsList.item(2)
        item.setText(_translate("WizardPage", "Big Switch", None))
        item = self.componentsList.item(3)
        item.setText(_translate("WizardPage", "Net", None))
        item = self.componentsList.item(4)
        item.setText(_translate("WizardPage", "PC", None))
        item = self.componentsList.item(5)
        item.setText(_translate("WizardPage", "Pizza", None))
        self.componentsList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

