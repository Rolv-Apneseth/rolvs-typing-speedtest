# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_typingWindow(object):
    def setupUi(self, typingWindow):
        typingWindow.setObjectName("typingWindow")
        typingWindow.resize(1534, 615)
        typingWindow.setStyleSheet("QWidget {\n"
"    \n"
"    background: rgb(50, 50, 50);\n"
"    color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QFrame {    \n"
"    \n"
"    \n"
"    border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton, QComboBox {\n"
"    \n"
"    background: rgb(70, 70, 70)\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(typingWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QtCore.QSize(0, 30))
        self.labelTitle.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(28)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelMainText = QtWidgets.QLabel(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMainText.sizePolicy().hasHeightForWidth())
        self.labelMainText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelMainText.setFont(font)
        self.labelMainText.setStyleSheet("padding: 50px 100px;")
        self.labelMainText.setTextFormat(QtCore.Qt.RichText)
        self.labelMainText.setWordWrap(True)
        self.labelMainText.setObjectName("labelMainText")
        self.verticalLayout.addWidget(self.labelMainText)
        self.lineInput = QtWidgets.QLineEdit(typingWindow)
        self.lineInput.setMinimumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaximumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaxLength(50000)
        self.lineInput.setObjectName("lineInput")
        self.verticalLayout.addWidget(self.lineInput)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayoutButtons.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        spacerItem4 = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem4)
        self.buttonBack = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBack.sizePolicy().hasHeightForWidth())
        self.buttonBack.setSizePolicy(sizePolicy)
        self.buttonBack.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayoutButtons.addWidget(self.buttonBack)
        spacerItem5 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem5)
        self.buttonRestart = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRestart.sizePolicy().hasHeightForWidth())
        self.buttonRestart.setSizePolicy(sizePolicy)
        self.buttonRestart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonRestart.setObjectName("buttonRestart")
        self.horizontalLayoutButtons.addWidget(self.buttonRestart)
        spacerItem6 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem6)
        self.buttonNewText = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewText.sizePolicy().hasHeightForWidth())
        self.buttonNewText.setSizePolicy(sizePolicy)
        self.buttonNewText.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNewText.setObjectName("buttonNewText")
        self.horizontalLayoutButtons.addWidget(self.buttonNewText)
        spacerItem7 = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayoutButtons)

        self.retranslateUi(typingWindow)
        QtCore.QMetaObject.connectSlotsByName(typingWindow)

    def retranslateUi(self, typingWindow):
        _translate = QtCore.QCoreApplication.translate
        typingWindow.setWindowTitle(_translate("typingWindow", "Typing window"))
        self.labelTitle.setText(_translate("typingWindow", "Mode"))
        self.labelMainText.setText(_translate("typingWindow", "Random text to type out blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"))
        self.buttonBack.setText(_translate("typingWindow", "Back"))
        self.buttonRestart.setText(_translate("typingWindow", "Restart"))
        self.buttonNewText.setText(_translate("typingWindow", "New Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    typingWindow = QtWidgets.QWidget()
    ui = Ui_typingWindow()
    ui.setupUi(typingWindow)
    typingWindow.show()
    sys.exit(app.exec_())
