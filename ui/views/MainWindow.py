# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/views/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 200))
        MainWindow.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/db.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("* {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QStatusBar{\n"
"  background-color: rgb(40, 40, 40);\n"
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
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        self.main_frame.setStyleSheet("#main_frame {\n"
"    border: 1px solid rgb(124, 124, 124);\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.532663 rgba(29, 29, 29, 255));\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 25))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.title_label = QtWidgets.QLabel(self.title_frame)
        self.title_label.setGeometry(QtCore.QRect(8, 3, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("")
        self.title_label.setObjectName("title_label")
        self.title_btns_frame = QtWidgets.QFrame(self.title_frame)
        self.title_btns_frame.setGeometry(QtCore.QRect(380, -5, 111, 31))
        self.title_btns_frame.setStyleSheet("QPushButton\n"
"{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.title_btns_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_btns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_btns_frame.setObjectName("title_btns_frame")
        self.minimize_btn = QtWidgets.QPushButton(self.title_btns_frame)
        self.minimize_btn.setGeometry(QtCore.QRect(54, 10, 16, 16))
        self.minimize_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.minimize_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.minimize_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 200, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 200, 0, 220);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(255, 200, 0, 200);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  background-color: rgb(150, 150, 150);\n"
"}")
        self.minimize_btn.setText("")
        self.minimize_btn.setObjectName("minimize_btn")
        self.exit_btn = QtWidgets.QPushButton(self.title_btns_frame)
        self.exit_btn.setGeometry(QtCore.QRect(80, 10, 16, 16))
        self.exit_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.exit_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 0, 0, 220);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(255, 0, 0, 200);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  background-color: rgb(150, 150, 150);\n"
"}")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.author_label = QtWidgets.QLabel(self.title_frame)
        self.author_label.setGeometry(QtCore.QRect(203, 4, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.author_label.setFont(font)
        self.author_label.setStyleSheet("")
        self.author_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.author_label.setObjectName("author_label")
        self.verticalLayout.addWidget(self.title_frame)
        self.choices_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choices_frame.sizePolicy().hasHeightForWidth())
        self.choices_frame.setSizePolicy(sizePolicy)
        self.choices_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.choices_frame.setStyleSheet("QComboBox {\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid  rgba(255, 255, 255, 100);\n"
"    background-color: rgb(40, 40, 40);\n"
"    text-align: center;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(190, 0, 105);\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"  color: rgb(95, 95, 95);\n"
"  background-color: rgb(150, 150, 150);\n"
"}")
        self.choices_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choices_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choices_frame.setObjectName("choices_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.choices_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.game_frame = QtWidgets.QFrame(self.choices_frame)
        self.game_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_frame.setObjectName("game_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.game_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.game_cmb_box = QtWidgets.QComboBox(self.game_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_cmb_box.sizePolicy().hasHeightForWidth())
        self.game_cmb_box.setSizePolicy(sizePolicy)
        self.game_cmb_box.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.game_cmb_box.setFont(font)
        self.game_cmb_box.setObjectName("game_cmb_box")
        self.verticalLayout_3.addWidget(self.game_cmb_box)
        self.horizontalLayout_3.addWidget(self.game_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.platform_frame = QtWidgets.QFrame(self.choices_frame)
        self.platform_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.platform_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.platform_frame.setObjectName("platform_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.platform_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.platform_cmb_box = QtWidgets.QComboBox(self.platform_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platform_cmb_box.sizePolicy().hasHeightForWidth())
        self.platform_cmb_box.setSizePolicy(sizePolicy)
        self.platform_cmb_box.setMinimumSize(QtCore.QSize(140, 0))
        self.platform_cmb_box.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.platform_cmb_box.setFont(font)
        self.platform_cmb_box.setObjectName("platform_cmb_box")
        self.verticalLayout_4.addWidget(self.platform_cmb_box)
        self.horizontalLayout_3.addWidget(self.platform_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.choices_frame)
        self.actions_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actions_frame.sizePolicy().hasHeightForWidth())
        self.actions_frame.setSizePolicy(sizePolicy)
        self.actions_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.actions_frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.actions_frame.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgb(200, 0, 120);\n"
"}\n"
"\n"
"QPushButton:hover:pressed\n"
"{\n"
"  background-color: rgb(180, 0, 100);\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: rgb(190, 0, 105);\n"
"  color: rgb(255, 255, 255);\n"
"  border: unset;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  color: rgb(95, 95, 95);\n"
"  background-color: rgb(150, 150, 150);\n"
"}")
        self.actions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.actions_frame)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.export_btn = QtWidgets.QPushButton(self.actions_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy)
        self.export_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.export_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.export_btn.setFont(font)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_5.addWidget(self.export_btn)
        spacerItem4 = QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.import_btn = QtWidgets.QPushButton(self.actions_frame)
        self.import_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.import_btn.setFont(font)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_5.addWidget(self.import_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.actions_frame)
        self.verticalLayout_2.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.title_label.setText(_translate("MainWindow", "Game Assets Converter v2.0"))
        self.minimize_btn.setToolTip(_translate("MainWindow", "Minimize"))
        self.exit_btn.setToolTip(_translate("MainWindow", "Exit"))
        self.author_label.setText(_translate("MainWindow", "by Ascomods"))
        self.game_cmb_box.setToolTip(_translate("MainWindow", "Game"))
        self.platform_cmb_box.setToolTip(_translate("MainWindow", "Platform"))
        self.export_btn.setText(_translate("MainWindow", "Export"))
        self.import_btn.setText(_translate("MainWindow", "Import"))
from ui.resources.resources import *
