# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_typingWindow(object):
    def setupUi(self, typingWindow):
        typingWindow.setObjectName("typingWindow")
        typingWindow.resize(1534, 607)
        self.verticalLayout = QtWidgets.QVBoxLayout(typingWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.labelTitle = QtWidgets.QLabel(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.labelTitle.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.labelMainText = QtWidgets.QLabel(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMainText.sizePolicy().hasHeightForWidth())
        self.labelMainText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelMainText.setFont(font)
        self.labelMainText.setStyleSheet("padding: 0 100px; font-size: 26pt;")
        self.labelMainText.setLineWidth(1)
        self.labelMainText.setMidLineWidth(1)
        self.labelMainText.setTextFormat(QtCore.Qt.RichText)
        self.labelMainText.setScaledContents(False)
        self.labelMainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMainText.setWordWrap(True)
        self.labelMainText.setIndent(-1)
        self.labelMainText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelMainText.setObjectName("labelMainText")
        self.verticalLayout.addWidget(self.labelMainText)
        self.lineInput = QtWidgets.QLineEdit(typingWindow)
        self.lineInput.setMinimumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaximumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaxLength(100000)
        self.lineInput.setObjectName("lineInput")
        self.verticalLayout.addWidget(self.lineInput)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayoutButtons.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        spacerItem5 = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem5)
        self.buttonMainMenu = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMainMenu.sizePolicy().hasHeightForWidth())
        self.buttonMainMenu.setSizePolicy(sizePolicy)
        self.buttonMainMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayoutButtons.addWidget(self.buttonMainMenu)
        spacerItem6 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem6)
        self.buttonRestart = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRestart.sizePolicy().hasHeightForWidth())
        self.buttonRestart.setSizePolicy(sizePolicy)
        self.buttonRestart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonRestart.setObjectName("buttonRestart")
        self.horizontalLayoutButtons.addWidget(self.buttonRestart)
        spacerItem7 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem7)
        self.buttonNewText = QtWidgets.QPushButton(typingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewText.sizePolicy().hasHeightForWidth())
        self.buttonNewText.setSizePolicy(sizePolicy)
        self.buttonNewText.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNewText.setObjectName("buttonNewText")
        self.horizontalLayoutButtons.addWidget(self.buttonNewText)
        spacerItem8 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem8)
        self.labelTime = QtWidgets.QLabel(typingWindow)
        self.labelTime.setObjectName("labelTime")
        self.horizontalLayoutButtons.addWidget(self.labelTime)
        self.labelUnit = QtWidgets.QLabel(typingWindow)
        self.labelUnit.setObjectName("labelUnit")
        self.horizontalLayoutButtons.addWidget(self.labelUnit)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayoutButtons)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(typingWindow)
        QtCore.QMetaObject.connectSlotsByName(typingWindow)

    def retranslateUi(self, typingWindow):
        _translate = QtCore.QCoreApplication.translate
        typingWindow.setWindowTitle(_translate("typingWindow", "Typing window"))
        self.labelTitle.setText(_translate("typingWindow", "Mode"))
        self.labelMainText.setText(_translate("typingWindow", "Random text to type out blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"))
        self.buttonMainMenu.setText(_translate("typingWindow", "Main Menu"))
        self.buttonRestart.setText(_translate("typingWindow", "Restart"))
        self.buttonNewText.setText(_translate("typingWindow", "New Text"))
        self.labelTime.setText(_translate("typingWindow", "1000"))
        self.labelUnit.setText(_translate("typingWindow", "s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    typingWindow = QtWidgets.QWidget()
    ui = Ui_typingWindow()
    ui.setupUi(typingWindow)
    typingWindow.show()
    sys.exit(app.exec_())
