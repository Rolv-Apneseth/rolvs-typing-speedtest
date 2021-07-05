# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(540, 572)
        mainWindow.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.labelMainMenu = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMainMenu.sizePolicy().hasHeightForWidth())
        self.labelMainMenu.setSizePolicy(sizePolicy)
        self.labelMainMenu.setMinimumSize(QtCore.QSize(0, 100))
        self.labelMainMenu.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.labelMainMenu.setFont(font)
        self.labelMainMenu.setStyleSheet("")
        self.labelMainMenu.setTextFormat(QtCore.Qt.PlainText)
        self.labelMainMenu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMainMenu.setObjectName("labelMainMenu")
        self.verticalLayout_3.addWidget(self.labelMainMenu)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.buttonStart = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonStart.setFont(font)
        self.buttonStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonStart.setAutoDefault(True)
        self.buttonStart.setObjectName("buttonStart")
        self.verticalLayout_3.addWidget(self.buttonStart)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.comboBoxSelectMode = QtWidgets.QComboBox(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelectMode.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectMode.setSizePolicy(sizePolicy)
        self.comboBoxSelectMode.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxSelectMode.setFont(font)
        self.comboBoxSelectMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxSelectMode.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBoxSelectMode.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxSelectMode.setIconSize(QtCore.QSize(0, 0))
        self.comboBoxSelectMode.setFrame(False)
        self.comboBoxSelectMode.setObjectName("comboBoxSelectMode")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxSelectMode)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.buttonSettings = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)
        self.buttonSettings.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonSettings.setFont(font)
        self.buttonSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSettings.setAutoDefault(True)
        self.buttonSettings.setObjectName("buttonSettings")
        self.verticalLayout_3.addWidget(self.buttonSettings)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.buttonStatistics = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStatistics.sizePolicy().hasHeightForWidth())
        self.buttonStatistics.setSizePolicy(sizePolicy)
        self.buttonStatistics.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonStatistics.setFont(font)
        self.buttonStatistics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonStatistics.setAutoDefault(True)
        self.buttonStatistics.setObjectName("buttonStatistics")
        self.verticalLayout_3.addWidget(self.buttonStatistics)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.buttonExit = QtWidgets.QPushButton(mainWindow)
        self.buttonExit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonExit.setFont(font)
        self.buttonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonExit.setAutoDefault(True)
        self.buttonExit.setObjectName("buttonExit")
        self.verticalLayout_3.addWidget(self.buttonExit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Speed Type Test"))
        self.labelMainMenu.setText(_translate("mainWindow", "Main Menu"))
        self.buttonStart.setText(_translate("mainWindow", "Begin"))
        self.comboBoxSelectMode.setItemText(0, _translate("mainWindow", "Common Phrases"))
        self.comboBoxSelectMode.setItemText(1, _translate("mainWindow", "Facts"))
        self.comboBoxSelectMode.setItemText(2, _translate("mainWindow", "Famous Literature Excerpts"))
        self.comboBoxSelectMode.setItemText(3, _translate("mainWindow", "Famous Quotes"))
        self.comboBoxSelectMode.setItemText(4, _translate("mainWindow", "Random Text: Brown"))
        self.comboBoxSelectMode.setItemText(5, _translate("mainWindow", "Random Text: Gutenberg"))
        self.comboBoxSelectMode.setItemText(6, _translate("mainWindow", "Random Text: Webtext"))
        self.buttonSettings.setText(_translate("mainWindow", "Settings"))
        self.buttonStatistics.setText(_translate("mainWindow", "Statistics"))
        self.buttonExit.setText(_translate("mainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
