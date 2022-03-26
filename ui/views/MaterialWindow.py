# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/views/MaterialWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MaterialWindow(object):
    def setupUi(self, MaterialWindow):
        MaterialWindow.setObjectName("MaterialWindow")
        MaterialWindow.resize(640, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MaterialWindow.sizePolicy().hasHeightForWidth())
        MaterialWindow.setSizePolicy(sizePolicy)
        MaterialWindow.setMinimumSize(QtCore.QSize(640, 520))
        MaterialWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MaterialWindow.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/db.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MaterialWindow.setWindowIcon(icon)
        MaterialWindow.setStyleSheet("* {\n"
"   font: 9pt \"Montserrat\";\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"  background-color: rgb(31, 38, 79);\n"
"}\n"
"\n"
"QStatusBar{\n"
"  background-color: rgb(31, 38, 79);\n"
"}\n"
"\n"
"#actionsGrpBox > QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgb(11, 103, 198);\n"
"}\n"
"\n"
"#actionsGrpBox > QPushButton:hover:pressed\n"
"{\n"
"  background-color: rgb(10, 89, 170);\n"
"}\n"
"\n"
"#actionsGrpBox > QPushButton{\n"
"  background-color: rgb(31, 94, 255);\n"
"  color: rgb(255, 255, 255);\n"
"  border: unset;\n"
"  border-radius: 4px;\n"
"  font-size:12px;\n"
"}\n"
"\n"
"#actionsGrpBox > QPushButton:disabled{\n"
"  background-color: rgb(185, 186, 189);\n"
"}\n"
"\n"
"QToolTip {\n"
"  color: black;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox {\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox {\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid  rgb(255, 255, 255);\n"
"  background-color: rgb(31, 38, 79);\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QListView {\n"
" border: unset;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"  background-color: rgb(10, 89, 170);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"  background-color: rgb(11, 103, 198);\n"
"}\n"
"\n"
"QListView{\n"
"  outline: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {              \n"
"    border: unset;\n"
"    background-color: rgb(31, 38, 79);\n"
"    width:10px;    \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-radius: 4px;\n"
"    background-color: rgb(11, 95, 181);\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    height: 0px;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}")
        MaterialWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MaterialWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gameGrpBox = QtWidgets.QGroupBox(self.frame)
        self.gameGrpBox.setMinimumSize(QtCore.QSize(0, 0))
        self.gameGrpBox.setObjectName("gameGrpBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gameGrpBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gameCmbBox = QtWidgets.QComboBox(self.gameGrpBox)
        self.gameCmbBox.setMinimumSize(QtCore.QSize(200, 0))
        self.gameCmbBox.setObjectName("gameCmbBox")
        self.horizontalLayout_2.addWidget(self.gameCmbBox)
        self.horizontalLayout_3.addWidget(self.gameGrpBox)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.platformGrpBox = QtWidgets.QGroupBox(self.frame)
        self.platformGrpBox.setObjectName("platformGrpBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.platformGrpBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.platformCmbBox = QtWidgets.QComboBox(self.platformGrpBox)
        self.platformCmbBox.setMinimumSize(QtCore.QSize(100, 0))
        self.platformCmbBox.setObjectName("platformCmbBox")
        self.horizontalLayout_4.addWidget(self.platformCmbBox)
        self.horizontalLayout_3.addWidget(self.platformGrpBox)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.actionsGrpBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionsGrpBox.sizePolicy().hasHeightForWidth())
        self.actionsGrpBox.setSizePolicy(sizePolicy)
        self.actionsGrpBox.setMinimumSize(QtCore.QSize(258, 0))
        self.actionsGrpBox.setMaximumSize(QtCore.QSize(258, 16777215))
        self.actionsGrpBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.actionsGrpBox.setObjectName("actionsGrpBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.actionsGrpBox)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openBtn.sizePolicy().hasHeightForWidth())
        self.openBtn.setSizePolicy(sizePolicy)
        self.openBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.openBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.openBtn.setToolTip("")
        self.openBtn.setWhatsThis("")
        self.openBtn.setText("")
        self.openBtn.setObjectName("openBtn")
        self.horizontalLayout.addWidget(self.openBtn)
        self.saveBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.saveBtn.setText("")
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.saveAsBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsBtn.sizePolicy().hasHeightForWidth())
        self.saveAsBtn.setSizePolicy(sizePolicy)
        self.saveAsBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.saveAsBtn.setText("")
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.horizontalLayout.addWidget(self.saveAsBtn)
        self.importBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importBtn.sizePolicy().hasHeightForWidth())
        self.importBtn.setSizePolicy(sizePolicy)
        self.importBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.importBtn.setText("")
        self.importBtn.setObjectName("importBtn")
        self.horizontalLayout.addWidget(self.importBtn)
        self.exportBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportBtn.sizePolicy().hasHeightForWidth())
        self.exportBtn.setSizePolicy(sizePolicy)
        self.exportBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.exportBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exportBtn.setText("")
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout.addWidget(self.exportBtn)
        self.goBackBtn = QtWidgets.QPushButton(self.actionsGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goBackBtn.sizePolicy().hasHeightForWidth())
        self.goBackBtn.setSizePolicy(sizePolicy)
        self.goBackBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.goBackBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.goBackBtn.setText("")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.horizontalLayout_3.addWidget(self.actionsGrpBox)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)
        self.contentGrpBox = QtWidgets.QGroupBox(self.frame_2)
        self.contentGrpBox.setMinimumSize(QtCore.QSize(0, 0))
        self.contentGrpBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contentGrpBox.setObjectName("contentGrpBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.contentGrpBox)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.contentListView = QtWidgets.QListView(self.contentGrpBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentListView.sizePolicy().hasHeightForWidth())
        self.contentListView.setSizePolicy(sizePolicy)
        self.contentListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contentListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.contentListView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.contentListView.setObjectName("contentListView")
        self.verticalLayout_3.addWidget(self.contentListView)
        self.verticalLayout.addWidget(self.contentGrpBox)
        self.verticalLayout_2.addWidget(self.frame_2)
        MaterialWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MaterialWindow)
        self.statusbar.setObjectName("statusbar")
        MaterialWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MaterialWindow)
        QtCore.QMetaObject.connectSlotsByName(MaterialWindow)

    def retranslateUi(self, MaterialWindow):
        _translate = QtCore.QCoreApplication.translate
        self.gameGrpBox.setTitle(_translate("MaterialWindow", "Game"))
        self.platformGrpBox.setTitle(_translate("MaterialWindow", "Platform"))
        self.actionsGrpBox.setTitle(_translate("MaterialWindow", "Actions"))
        self.contentGrpBox.setTitle(_translate("MaterialWindow", "Content"))
from ui.resources.resources import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MaterialWindow = QtWidgets.QMainWindow()
    ui = Ui_MaterialWindow()
    ui.setupUi(MaterialWindow)
    MaterialWindow.show()
    sys.exit(app.exec_())