# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/qt4gui_layouts/startscreen.ui'
#
# Created: Fri Mar 13 11:13:15 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(217, 258)
        Dialog.setMinimumSize(QtCore.QSize(217, 258))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(71, 16777215))
        self.password_lineEdit.setMaxLength(10)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.user1_lineEdit = QtGui.QLineEdit(Dialog)
        self.user1_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user1_lineEdit.setMaxLength(6)
        self.user1_lineEdit.setObjectName("user1_lineEdit")
        self.horizontalLayout_3.addWidget(self.user1_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.user2_lineEdit = QtGui.QLineEdit(Dialog)
        self.user2_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user2_lineEdit.setMaxLength(6)
        self.user2_lineEdit.setObjectName("user2_lineEdit")
        self.horizontalLayout_2.addWidget(self.user2_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(24, 51, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 2, 1)
        self.surgery_radioButton = QtGui.QRadioButton(Dialog)
        self.surgery_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.surgery_radioButton.setChecked(True)
        self.surgery_radioButton.setObjectName("surgery_radioButton")
        self.gridLayout.addWidget(self.surgery_radioButton, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(23, 51, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 2, 1)
        self.reception_radioButton = QtGui.QRadioButton(Dialog)
        self.reception_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.reception_radioButton.setObjectName("reception_radioButton")
        self.gridLayout.addWidget(self.reception_radioButton, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 103, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "openMolar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "System Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "User 1(required)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "User 2 (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.surgery_radioButton.setText(QtGui.QApplication.translate("Dialog", "Surgery Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.reception_radioButton.setText(QtGui.QApplication.translate("Dialog", "Reception Machine", None, QtGui.QApplication.UnicodeUTF8))

