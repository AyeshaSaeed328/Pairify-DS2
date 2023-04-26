# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import csv
from . resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: \n"
"url(:/icons/images/icons/cil-magnifying-glass.png)")

        self.verticalLayout_8.addWidget(self.btn_new)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 150, 261, 311))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"download.png"))
        self.stackedWidget.addWidget(self.home)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(48, 47, 131, 61))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 140, 131, 61))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 220, 131, 61))
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(170, 60, 231, 31))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(7, 7, 7, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
        brush5 = QBrush(QColor(221, 221, 221, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_2.setPalette(palette)
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(170, 150, 231, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_3.setPalette(palette1)
        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(170, 380, 221, 91))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_4.setPalette(palette2)
        self.insert_btn = QPushButton(self.frame)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setGeometry(QRect(320, 550, 75, 24))
        self.insert_btn.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        if (self.tableWidget.rowCount() < 2000):
            self.tableWidget.setRowCount(2000)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(430, 10, 721, 501))
        self.tableWidget.setStyleSheet(u"border-top-color: rgb(85, 0, 127);")
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setRowCount(2000)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Name', 'Age', 'Priority','Symptoms'])
        self.remove_btn = QPushButton(self.frame)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(520, 540, 101, 24))
        self.remove_btn.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.textEdit_5 = QTextEdit(self.frame)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(30, 500, 361, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_5.setPalette(palette3)

        def updateTextEdit():
                items = self.listWidget.selectedItems()
                selected_items_text = [str(item.text()) for item in items]
                current_text = self.textEdit_4.toPlainText()
                new_text = "\n".join(selected_items_text)
                if current_text:
                        self.textEdit_4.setPlainText(current_text + ", " + new_text)
                else:
                        self.textEdit_4.setPlainText(new_text)

        def updateTextEdit2():
                items = self.listWidget_2.selectedItems()
                selected_items_text = [str(item.text()) for item in items]
                current_text = self.textEdit_10.toPlainText()
                new_text = "\n".join(selected_items_text)
                if current_text:
                        self.textEdit_10.setPlainText(current_text + ", " + new_text)
                else:
                        self.textEdit_10.setPlainText(new_text)                

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(170, 230, 231, 121))
        self.listWidget.setSelectionMode(

            QAbstractItemView.SelectionMode.ExtendedSelection
        )
        # item = QListWidgetItem("Nausea")
        # self.listWidget.addItem(item)
        # # self.listWidget.itemSelectionChanged.connect(updateTextEdit)
        
        # for i in range(10):
        #     item = QListWidgetItem("Item %i" % i)
        #     self.listWidget.addItem(item)
        self.new_page = QWidget()
        self.frame_3 = QFrame(self.new_page)

        self.listWidget_2 = QListWidget(self.frame_3)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(200, 370, 231, 121))
        self.listWidget_2.setSelectionMode(

            QAbstractItemView.SelectionMode.ExtendedSelection
        )

        with open("project file 2.csv", 'r') as file:
                symptoms_file = csv.reader(file)
                next(symptoms_file)
                for symptoms,priority in symptoms_file:
                        self.listWidget.addItem(symptoms)
                        self.listWidget_2.addItem(symptoms)
        self.listWidget.itemSelectionChanged.connect(updateTextEdit)
        self.listWidget_2.itemSelectionChanged.connect(updateTextEdit2)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.widgets)
        
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.edit_btn_2 = QPushButton(self.frame_3)
        self.edit_btn_2.setObjectName(u"edit_btn_2")
        self.edit_btn_2.setGeometry(QRect(490, 540, 75, 24))
        self.edit_btn_2.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.textEdit_9 = QTextEdit(self.frame_3)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(200, 290, 231, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_9.setPalette(palette4)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 270, 131, 61))
        self.textEdit_10 = QTextEdit(self.frame_3)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(200, 530, 231, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_10.setPalette(palette5)
        self.tableWidget_3 = QTableWidget(self.frame_3)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        if (self.tableWidget_3.rowCount() < 2000):
            self.tableWidget_3.setRowCount(2000)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(470, 10, 691, 501))
        self.tableWidget_3.setStyleSheet(u"border-top-color: rgb(85, 0, 127);")
        self.tableWidget_3.setHorizontalHeaderLabels(['ID', 'Name', 'Age', 'Priority','Symptoms'])
        self.tableWidget_3.setInputMethodHints(Qt.ImhNone)
        self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_3.setAlternatingRowColors(False)
        self.tableWidget_3.setRowCount(2000)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 180, 131, 61))
        self.search_btn_2 = QPushButton(self.frame_3)
        self.search_btn_2.setObjectName(u"search_btn_2")
        self.search_btn_2.setGeometry(QRect(240, 140, 75, 24))
        self.search_btn_2.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.textEdit_11 = QTextEdit(self.frame_3)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(200, 70, 231, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_11.setPalette(palette6)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 50, 171, 61))
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 360, 131, 61))
        self.restet_btn = QPushButton(self.frame_3)
        self.restet_btn.setObjectName(u"restet_btn")
        self.restet_btn.setGeometry(QRect(330, 140, 75, 24))
        self.restet_btn.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.textEdit_12 = QTextEdit(self.frame_3)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(200, 200, 231, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textEdit_12.setPalette(palette7)
        

        self.verticalLayout_20.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Medical Triage System-DSII Project", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None))
        self.insert_btn.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Max", None))
        self.edit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter Patient ID to search", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None))
        self.restet_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi




# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(1280, 720)
#         MainWindow.setMinimumSize(QSize(940, 560))
#         self.styleSheet = QWidget(MainWindow)
#         self.styleSheet.setObjectName(u"styleSheet")
#         font = QFont()
#         font.setFamilies([u"Segoe UI"])
#         font.setPointSize(10)
#         font.setBold(False)
#         font.setItalic(False)
#         self.styleSheet.setFont(font)
#         self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "\n"
# "SET APP STYLESHEET - FULL STYLES HERE\n"
# "DARK THEME - DRACULA COLOR BASED\n"
# "\n"
# "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
# "\n"
# "QWidget{\n"
# "	color: rgb(221, 221, 221);\n"
# "	font: 10pt \"Segoe UI\";\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Tooltip */\n"
# "QToolTip {\n"
# "	color: #ffffff;\n"
# "	background-color: rgba(33, 37, 43, 180);\n"
# "	border: 1px solid rgb(44, 49, 58);\n"
# "	background-image: none;\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 2px solid rgb(255, 121, 198);\n"
# "	text-align: left;\n"
# "	padding-left: 8px;\n"
# "	margin: 0px;\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Bg App */\n"
# "#bgApp {	\n"
# "	background"
#                         "-color: rgb(40, 44, 52);\n"
# "	border: 1px solid rgb(44, 49, 58);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Left Menu */\n"
# "#leftMenuBg {	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "}\n"
# "#topLogo {\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	background-image: url(:/images/images/images/PyDracula.png);\n"
# "	background-position: centered;\n"
# "	background-repeat: no-repeat;\n"
# "}\n"
# "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
# "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
# "\n"
# "/* MENUS */\n"
# "#topMenu .QPushButton {	\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 22px solid transparent;\n"
# "	background-color: transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#topMenu .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#topMenu .QPushButton:pressed {	\n"
# "	background-color: rgb(18"
#                         "9, 147, 249);\n"
# "	color: rgb(255, 255, 255);\n"
# "}\n"
# "#bottomMenu .QPushButton {	\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 20px solid transparent;\n"
# "	background-color:transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#bottomMenu .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#bottomMenu .QPushButton:pressed {	\n"
# "	background-color: rgb(189, 147, 249);\n"
# "	color: rgb(255, 255, 255);\n"
# "}\n"
# "#leftMenuFrame{\n"
# "	border-top: 3px solid rgb(44, 49, 58);\n"
# "}\n"
# "\n"
# "/* Toggle Button */\n"
# "#toggleButton {\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 20px solid transparent;\n"
# "	background-color: rgb(37, 41, 48);\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "	color: rgb(113, 126, 149);\n"
# "}\n"
# "#toggleButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#toggleButton:pressed {\n"
# "	background-color: rgb("
#                         "189, 147, 249);\n"
# "}\n"
# "\n"
# "/* Title Menu */\n"
# "#titleRightInfo { padding-left: 10px; }\n"
# "\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Extra Tab */\n"
# "#extraLeftBox {	\n"
# "	background-color: rgb(44, 49, 58);\n"
# "}\n"
# "#extraTopBg{	\n"
# "	background-color: rgb(189, 147, 249)\n"
# "}\n"
# "\n"
# "/* Icon */\n"
# "#extraIcon {\n"
# "	background-position: center;\n"
# "	background-repeat: no-repeat;\n"
# "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
# "}\n"
# "\n"
# "/* Label */\n"
# "#extraLabel { color: rgb(255, 255, 255); }\n"
# "\n"
# "/* Btn Close */\n"
# "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
# "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
# "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
# "\n"
# "/* Extra Content */\n"
# "#extraContent{\n"
# "	border"
#                         "-top: 3px solid rgb(40, 44, 52);\n"
# "}\n"
# "\n"
# "/* Extra Top Menus */\n"
# "#extraTopMenu .QPushButton {\n"
# "background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 22px solid transparent;\n"
# "	background-color:transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#extraTopMenu .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#extraTopMenu .QPushButton:pressed {	\n"
# "	background-color: rgb(189, 147, 249);\n"
# "	color: rgb(255, 255, 255);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Content App */\n"
# "#contentTopBg{	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "}\n"
# "#contentBottom{\n"
# "	border-top: 3px solid rgb(44, 49, 58);\n"
# "}\n"
# "\n"
# "/* Top Buttons */\n"
# "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
# "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
#                         "le: solid; border-radius: 4px; }\n"
# "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
# "\n"
# "/* Theme Settings */\n"
# "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
# "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
# "\n"
# "/* Bottom Bar */\n"
# "#bottomBar { background-color: rgb(44, 49, 58); }\n"
# "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
# "\n"
# "/* CONTENT SETTINGS */\n"
# "/* MENUS */\n"
# "#contentSettings .QPushButton {	\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 22px solid transparent;\n"
# "	background-color:transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#contentSettings .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#contentSettings .QPushButton:pressed {	\n"
# "	background-color: rgb(189, 147, 249);\n"
# "	color: rgb"
#                         "(255, 255, 255);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "QTableWidget */\n"
# "QTableWidget {	\n"
# "	background-color: transparent;\n"
# "	padding: 10px;\n"
# "	border-radius: 5px;\n"
# "	gridline-color: rgb(44, 49, 58);\n"
# "	border-bottom: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::item{\n"
# "	border-color: rgb(44, 49, 60);\n"
# "	padding-left: 5px;\n"
# "	padding-right: 5px;\n"
# "	gridline-color: rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::item:selected{\n"
# "	background-color: rgb(189, 147, 249);\n"
# "}\n"
# "QHeaderView::section{\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	max-width: 30px;\n"
# "	border: 1px solid rgb(44, 49, 58);\n"
# "	border-style: none;\n"
# "    border-bottom: 1px solid rgb(44, 49, 60);\n"
# "    border-right: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::horizontalHeader {	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "}\n"
# "QHeaderView::section:horizontal\n"
# "{\n"
# "    border: 1px solid rgb(33, 37, 43);\n"
# "	background-co"
#                         "lor: rgb(33, 37, 43);\n"
# "	padding: 3px;\n"
# "	border-top-left-radius: 7px;\n"
# "    border-top-right-radius: 7px;\n"
# "}\n"
# "QHeaderView::section:vertical\n"
# "{\n"
# "    border: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "LineEdit */\n"
# "QLineEdit {\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	border-radius: 5px;\n"
# "	border: 2px solid rgb(33, 37, 43);\n"
# "	padding-left: 10px;\n"
# "	selection-color: rgb(255, 255, 255);\n"
# "	selection-background-color: rgb(255, 121, 198);\n"
# "}\n"
# "QLineEdit:hover {\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QLineEdit:focus {\n"
# "	border: 2px solid rgb(91, 101, 124);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "PlainTextEdit */\n"
# "QPlainTextEdit {\n"
# "	background-color: rgb(27, 29, 35);\n"
# "	border-radius: 5px;\n"
# "	padding: 10px;\n"
# "	selection-color: rgb(255, 255, 255);\n"
# "	selection-background-c"
#                         "olor: rgb(255, 121, 198);\n"
# "}\n"
# "QPlainTextEdit  QScrollBar:vertical {\n"
# "    width: 8px;\n"
# " }\n"
# "QPlainTextEdit  QScrollBar:horizontal {\n"
# "    height: 8px;\n"
# " }\n"
# "QPlainTextEdit:hover {\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QPlainTextEdit:focus {\n"
# "	border: 2px solid rgb(91, 101, 124);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "ScrollBars */\n"
# "QScrollBar:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    height: 8px;\n"
# "    margin: 0px 21px 0 21px;\n"
# "	border-radius: 0px;\n"
# "}\n"
# "QScrollBar::handle:horizontal {\n"
# "    background: rgb(189, 147, 249);\n"
# "    min-width: 25px;\n"
# "	border-radius: 4px\n"
# "}\n"
# "QScrollBar::add-line:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "    width: 20px;\n"
# "	border-top-right-radius: 4px;\n"
# "    border-bottom-right-radius: 4px;\n"
# "    subcontrol-position: right;\n"
# "    subcontrol-origin: margin;\n"
# "}\n"
# ""
#                         "QScrollBar::sub-line:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "    width: 20px;\n"
# "	border-top-left-radius: 4px;\n"
# "    border-bottom-left-radius: 4px;\n"
# "    subcontrol-position: left;\n"
# "    subcontrol-origin: margin;\n"
# "}\n"
# "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
# "{\n"
# "     background: none;\n"
# "}\n"
# "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
# "{\n"
# "     background: none;\n"
# "}\n"
# " QScrollBar:vertical {\n"
# "	border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    width: 8px;\n"
# "    margin: 21px 0 21px 0;\n"
# "	border-radius: 0px;\n"
# " }\n"
# " QScrollBar::handle:vertical {	\n"
# "	background: rgb(189, 147, 249);\n"
# "    min-height: 25px;\n"
# "	border-radius: 4px\n"
# " }\n"
# " QScrollBar::add-line:vertical {\n"
# "     border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "     height: 20px;\n"
# "	border-bottom-left-radius: 4px;\n"
# "    border-bottom-right-radius: 4px;\n"
# "     subcontrol-position: bottom;\n"
# "     su"
#                         "bcontrol-origin: margin;\n"
# " }\n"
# " QScrollBar::sub-line:vertical {\n"
# "	border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "     height: 20px;\n"
# "	border-top-left-radius: 4px;\n"
# "    border-top-right-radius: 4px;\n"
# "     subcontrol-position: top;\n"
# "     subcontrol-origin: margin;\n"
# " }\n"
# " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
# "     background: none;\n"
# " }\n"
# "\n"
# " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
# "     background: none;\n"
# " }\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "CheckBox */\n"
# "QCheckBox::indicator {\n"
# "    border: 3px solid rgb(52, 59, 72);\n"
# "	width: 15px;\n"
# "	height: 15px;\n"
# "	border-radius: 10px;\n"
# "    background: rgb(44, 49, 60);\n"
# "}\n"
# "QCheckBox::indicator:hover {\n"
# "    border: 3px solid rgb(58, 66, 81);\n"
# "}\n"
# "QCheckBox::indicator:checked {\n"
# "    background: 3px solid rgb(52, 59, 72);\n"
# "	border: 3px solid rgb(52, 59, 72);	\n"
# "	back"
#                         "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "RadioButton */\n"
# "QRadioButton::indicator {\n"
# "    border: 3px solid rgb(52, 59, 72);\n"
# "	width: 15px;\n"
# "	height: 15px;\n"
# "	border-radius: 10px;\n"
# "    background: rgb(44, 49, 60);\n"
# "}\n"
# "QRadioButton::indicator:hover {\n"
# "    border: 3px solid rgb(58, 66, 81);\n"
# "}\n"
# "QRadioButton::indicator:checked {\n"
# "    background: 3px solid rgb(94, 106, 130);\n"
# "	border: 3px solid rgb(52, 59, 72);	\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "ComboBox */\n"
# "QComboBox{\n"
# "	background-color: rgb(27, 29, 35);\n"
# "	border-radius: 5px;\n"
# "	border: 2px solid rgb(33, 37, 43);\n"
# "	padding: 5px;\n"
# "	padding-left: 10px;\n"
# "}\n"
# "QComboBox:hover{\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QComboBox::drop-down {\n"
# "	subcontrol-origin: padding;\n"
# "	subco"
#                         "ntrol-position: top right;\n"
# "	width: 25px; \n"
# "	border-left-width: 3px;\n"
# "	border-left-color: rgba(39, 44, 54, 150);\n"
# "	border-left-style: solid;\n"
# "	border-top-right-radius: 3px;\n"
# "	border-bottom-right-radius: 3px;	\n"
# "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
# "	background-position: center;\n"
# "	background-repeat: no-reperat;\n"
# " }\n"
# "QComboBox QAbstractItemView {\n"
# "	color: rgb(255, 121, 198);	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	padding: 10px;\n"
# "	selection-background-color: rgb(39, 44, 54);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Sliders */\n"
# "QSlider::groove:horizontal {\n"
# "    border-radius: 5px;\n"
# "    height: 10px;\n"
# "	margin: 0px;\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "QSlider::groove:horizontal:hover {\n"
# "	background-color: rgb(55, 62, 76);\n"
# "}\n"
# "QSlider::handle:horizontal {\n"
# "    background-color: rgb(189, 147, 249);\n"
# "    border: none;\n"
# "    h"
#                         "eight: 10px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "QSlider::handle:horizontal:hover {\n"
# "    background-color: rgb(195, 155, 255);\n"
# "}\n"
# "QSlider::handle:horizontal:pressed {\n"
# "    background-color: rgb(255, 121, 198);\n"
# "}\n"
# "\n"
# "QSlider::groove:vertical {\n"
# "    border-radius: 5px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "QSlider::groove:vertical:hover {\n"
# "	background-color: rgb(55, 62, 76);\n"
# "}\n"
# "QSlider::handle:vertical {\n"
# "    background-color: rgb(189, 147, 249);\n"
# "	border: none;\n"
# "    height: 10px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "QSlider::handle:vertical:hover {\n"
# "    background-color: rgb(195, 155, 255);\n"
# "}\n"
# "QSlider::handle:vertical:pressed {\n"
# "    background-color: rgb(255, 121, 198);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "CommandLinkButton */\n"
# "QCommandLi"
#                         "nkButton {	\n"
# "	color: rgb(255, 121, 198);\n"
# "	border-radius: 5px;\n"
# "	padding: 5px;\n"
# "	color: rgb(255, 170, 255);\n"
# "}\n"
# "QCommandLinkButton:hover {	\n"
# "	color: rgb(255, 170, 255);\n"
# "	background-color: rgb(44, 49, 60);\n"
# "}\n"
# "QCommandLinkButton:pressed {	\n"
# "	color: rgb(189, 147, 249);\n"
# "	background-color: rgb(52, 58, 71);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Button */\n"
# "#pagesContainer QPushButton {\n"
# "	border: 2px solid rgb(52, 59, 72);\n"
# "	border-radius: 5px;	\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "#pagesContainer QPushButton:hover {\n"
# "	background-color: rgb(57, 65, 80);\n"
# "	border: 2px solid rgb(61, 70, 86);\n"
# "}\n"
# "#pagesContainer QPushButton:pressed {	\n"
# "	background-color: rgb(35, 40, 49);\n"
# "	border: 2px solid rgb(43, 50, 61);\n"
# "}\n"
# "\n"
# "")
#         self.appMargins = QVBoxLayout(self.styleSheet)
#         self.appMargins.setSpacing(0)
#         self.appMargins.setObjectName(u"appMargins")
#         self.appMargins.setContentsMargins(10, 10, 10, 10)
#         self.bgApp = QFrame(self.styleSheet)
#         self.bgApp.setObjectName(u"bgApp")
#         self.bgApp.setStyleSheet(u"")
#         self.bgApp.setFrameShape(QFrame.NoFrame)
#         self.bgApp.setFrameShadow(QFrame.Raised)
#         self.appLayout = QHBoxLayout(self.bgApp)
#         self.appLayout.setSpacing(0)
#         self.appLayout.setObjectName(u"appLayout")
#         self.appLayout.setContentsMargins(0, 0, 0, 0)
#         self.leftMenuBg = QFrame(self.bgApp)
#         self.leftMenuBg.setObjectName(u"leftMenuBg")
#         self.leftMenuBg.setMinimumSize(QSize(60, 0))
#         self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
#         self.leftMenuBg.setFrameShape(QFrame.NoFrame)
#         self.leftMenuBg.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
#         self.verticalLayout_3.setSpacing(0)
#         self.verticalLayout_3.setObjectName(u"verticalLayout_3")
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.topLogoInfo = QFrame(self.leftMenuBg)
#         self.topLogoInfo.setObjectName(u"topLogoInfo")
#         self.topLogoInfo.setMinimumSize(QSize(0, 50))
#         self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
#         self.topLogoInfo.setFrameShape(QFrame.NoFrame)
#         self.topLogoInfo.setFrameShadow(QFrame.Raised)
#         self.topLogo = QFrame(self.topLogoInfo)
#         self.topLogo.setObjectName(u"topLogo")
#         self.topLogo.setGeometry(QRect(10, 5, 42, 42))
#         self.topLogo.setMinimumSize(QSize(42, 42))
#         self.topLogo.setMaximumSize(QSize(42, 42))
#         self.topLogo.setStyleSheet(u"")
#         self.topLogo.setFrameShape(QFrame.NoFrame)
#         self.topLogo.setFrameShadow(QFrame.Raised)
#         self.titleLeftApp = QLabel(self.topLogoInfo)
#         self.titleLeftApp.setObjectName(u"titleLeftApp")
#         self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
#         font1 = QFont()
#         font1.setFamilies([u"Segoe UI Semibold"])
#         font1.setPointSize(12)
#         font1.setBold(False)
#         font1.setItalic(False)
#         self.titleLeftApp.setFont(font1)
#         self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
#         self.titleLeftDescription = QLabel(self.topLogoInfo)
#         self.titleLeftDescription.setObjectName(u"titleLeftDescription")
#         self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
#         self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
#         font2 = QFont()
#         font2.setFamilies([u"Segoe UI"])
#         font2.setPointSize(8)
#         font2.setBold(False)
#         font2.setItalic(False)
#         self.titleLeftDescription.setFont(font2)
#         self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

#         self.verticalLayout_3.addWidget(self.topLogoInfo)

#         self.leftMenuFrame = QFrame(self.leftMenuBg)
#         self.leftMenuFrame.setObjectName(u"leftMenuFrame")
#         self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
#         self.leftMenuFrame.setFrameShadow(QFrame.Raised)
#         self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
#         self.verticalMenuLayout.setSpacing(0)
#         self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
#         self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
#         self.toggleBox = QFrame(self.leftMenuFrame)
#         self.toggleBox.setObjectName(u"toggleBox")
#         self.toggleBox.setMaximumSize(QSize(16777215, 45))
#         self.toggleBox.setFrameShape(QFrame.NoFrame)
#         self.toggleBox.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
#         self.verticalLayout_4.setSpacing(0)
#         self.verticalLayout_4.setObjectName(u"verticalLayout_4")
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.toggleButton = QPushButton(self.toggleBox)
#         self.toggleButton.setObjectName(u"toggleButton")
#         sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
#         self.toggleButton.setSizePolicy(sizePolicy)
#         self.toggleButton.setMinimumSize(QSize(0, 45))
#         self.toggleButton.setFont(font)
#         self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
#         self.toggleButton.setLayoutDirection(Qt.LeftToRight)
#         self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

#         self.verticalLayout_4.addWidget(self.toggleButton)


#         self.verticalMenuLayout.addWidget(self.toggleBox)

#         self.topMenu = QFrame(self.leftMenuFrame)
#         self.topMenu.setObjectName(u"topMenu")
#         self.topMenu.setFrameShape(QFrame.NoFrame)
#         self.topMenu.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_8 = QVBoxLayout(self.topMenu)
#         self.verticalLayout_8.setSpacing(0)
#         self.verticalLayout_8.setObjectName(u"verticalLayout_8")
#         self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
#         self.btn_home = QPushButton(self.topMenu)
#         self.btn_home.setObjectName(u"btn_home")
#         sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
#         self.btn_home.setSizePolicy(sizePolicy)
#         self.btn_home.setMinimumSize(QSize(0, 45))
#         self.btn_home.setFont(font)
#         self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_home.setLayoutDirection(Qt.LeftToRight)
#         self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

#         self.verticalLayout_8.addWidget(self.btn_home)

#         self.btn_widgets = QPushButton(self.topMenu)
#         self.btn_widgets.setObjectName(u"btn_widgets")
#         sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
#         self.btn_widgets.setSizePolicy(sizePolicy)
#         self.btn_widgets.setMinimumSize(QSize(0, 45))
#         self.btn_widgets.setFont(font)
#         self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
#         self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);\n"
# "")

#         self.verticalLayout_8.addWidget(self.btn_widgets)

#         self.btn_new = QPushButton(self.topMenu)
#         self.btn_new.setObjectName(u"btn_new")
#         sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
#         self.btn_new.setSizePolicy(sizePolicy)
#         self.btn_new.setMinimumSize(QSize(0, 45))
#         self.btn_new.setFont(font)
#         self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_new.setLayoutDirection(Qt.LeftToRight)
#         self.btn_new.setStyleSheet(u"background-image: \n"
# "url(:/icons/images/icons/cil-magnifying-glass.png)")

#         self.verticalLayout_8.addWidget(self.btn_new)


#         self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

#         self.bottomMenu = QFrame(self.leftMenuFrame)
#         self.bottomMenu.setObjectName(u"bottomMenu")
#         self.bottomMenu.setFrameShape(QFrame.NoFrame)
#         self.bottomMenu.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
#         self.verticalLayout_9.setSpacing(0)
#         self.verticalLayout_9.setObjectName(u"verticalLayout_9")
#         self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

#         self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


#         self.verticalLayout_3.addWidget(self.leftMenuFrame)


#         self.appLayout.addWidget(self.leftMenuBg)

#         self.extraLeftBox = QFrame(self.bgApp)
#         self.extraLeftBox.setObjectName(u"extraLeftBox")
#         self.extraLeftBox.setMinimumSize(QSize(0, 0))
#         self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
#         self.extraLeftBox.setFrameShape(QFrame.NoFrame)
#         self.extraLeftBox.setFrameShadow(QFrame.Raised)
#         self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
#         self.extraColumLayout.setSpacing(0)
#         self.extraColumLayout.setObjectName(u"extraColumLayout")
#         self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
#         self.extraTopBg = QFrame(self.extraLeftBox)
#         self.extraTopBg.setObjectName(u"extraTopBg")
#         self.extraTopBg.setMinimumSize(QSize(0, 50))
#         self.extraTopBg.setMaximumSize(QSize(16777215, 50))
#         self.extraTopBg.setFrameShape(QFrame.NoFrame)
#         self.extraTopBg.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
#         self.verticalLayout_5.setSpacing(0)
#         self.verticalLayout_5.setObjectName(u"verticalLayout_5")
#         self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.extraTopLayout = QGridLayout()
#         self.extraTopLayout.setObjectName(u"extraTopLayout")
#         self.extraTopLayout.setHorizontalSpacing(10)
#         self.extraTopLayout.setVerticalSpacing(0)
#         self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
#         self.extraIcon = QFrame(self.extraTopBg)
#         self.extraIcon.setObjectName(u"extraIcon")
#         self.extraIcon.setMinimumSize(QSize(20, 0))
#         self.extraIcon.setMaximumSize(QSize(20, 20))
#         self.extraIcon.setFrameShape(QFrame.NoFrame)
#         self.extraIcon.setFrameShadow(QFrame.Raised)

#         self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

#         self.extraLabel = QLabel(self.extraTopBg)
#         self.extraLabel.setObjectName(u"extraLabel")
#         self.extraLabel.setMinimumSize(QSize(150, 0))

#         self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

#         self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
#         self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
#         self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
#         self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
#         self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
#         icon = QIcon()
#         icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.extraCloseColumnBtn.setIcon(icon)
#         self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

#         self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


#         self.verticalLayout_5.addLayout(self.extraTopLayout)


#         self.extraColumLayout.addWidget(self.extraTopBg)

#         self.extraContent = QFrame(self.extraLeftBox)
#         self.extraContent.setObjectName(u"extraContent")
#         self.extraContent.setFrameShape(QFrame.NoFrame)
#         self.extraContent.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_12 = QVBoxLayout(self.extraContent)
#         self.verticalLayout_12.setSpacing(0)
#         self.verticalLayout_12.setObjectName(u"verticalLayout_12")
#         self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
#         self.extraTopMenu = QFrame(self.extraContent)
#         self.extraTopMenu.setObjectName(u"extraTopMenu")
#         self.extraTopMenu.setFrameShape(QFrame.NoFrame)
#         self.extraTopMenu.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
#         self.verticalLayout_11.setSpacing(0)
#         self.verticalLayout_11.setObjectName(u"verticalLayout_11")
#         self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
#         self.btn_share = QPushButton(self.extraTopMenu)
#         self.btn_share.setObjectName(u"btn_share")
#         sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
#         self.btn_share.setSizePolicy(sizePolicy)
#         self.btn_share.setMinimumSize(QSize(0, 45))
#         self.btn_share.setFont(font)
#         self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_share.setLayoutDirection(Qt.LeftToRight)
#         self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

#         self.verticalLayout_11.addWidget(self.btn_share)

#         self.btn_adjustments = QPushButton(self.extraTopMenu)
#         self.btn_adjustments.setObjectName(u"btn_adjustments")
#         sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
#         self.btn_adjustments.setSizePolicy(sizePolicy)
#         self.btn_adjustments.setMinimumSize(QSize(0, 45))
#         self.btn_adjustments.setFont(font)
#         self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
#         self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

#         self.verticalLayout_11.addWidget(self.btn_adjustments)

#         self.btn_more = QPushButton(self.extraTopMenu)
#         self.btn_more.setObjectName(u"btn_more")
#         sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
#         self.btn_more.setSizePolicy(sizePolicy)
#         self.btn_more.setMinimumSize(QSize(0, 45))
#         self.btn_more.setFont(font)
#         self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_more.setLayoutDirection(Qt.LeftToRight)
#         self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

#         self.verticalLayout_11.addWidget(self.btn_more)


#         self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

#         self.extraCenter = QFrame(self.extraContent)
#         self.extraCenter.setObjectName(u"extraCenter")
#         self.extraCenter.setFrameShape(QFrame.NoFrame)
#         self.extraCenter.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
#         self.verticalLayout_10.setObjectName(u"verticalLayout_10")
#         self.textEdit = QTextEdit(self.extraCenter)
#         self.textEdit.setObjectName(u"textEdit")
#         self.textEdit.setMinimumSize(QSize(222, 0))
#         self.textEdit.setStyleSheet(u"background: transparent;")
#         self.textEdit.setFrameShape(QFrame.NoFrame)
#         self.textEdit.setReadOnly(True)

#         self.verticalLayout_10.addWidget(self.textEdit)


#         self.verticalLayout_12.addWidget(self.extraCenter)

#         self.extraBottom = QFrame(self.extraContent)
#         self.extraBottom.setObjectName(u"extraBottom")
#         self.extraBottom.setFrameShape(QFrame.NoFrame)
#         self.extraBottom.setFrameShadow(QFrame.Raised)

#         self.verticalLayout_12.addWidget(self.extraBottom)


#         self.extraColumLayout.addWidget(self.extraContent)


#         self.appLayout.addWidget(self.extraLeftBox)

#         self.contentBox = QFrame(self.bgApp)
#         self.contentBox.setObjectName(u"contentBox")
#         self.contentBox.setFrameShape(QFrame.NoFrame)
#         self.contentBox.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_2 = QVBoxLayout(self.contentBox)
#         self.verticalLayout_2.setSpacing(0)
#         self.verticalLayout_2.setObjectName(u"verticalLayout_2")
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.contentTopBg = QFrame(self.contentBox)
#         self.contentTopBg.setObjectName(u"contentTopBg")
#         self.contentTopBg.setMinimumSize(QSize(0, 50))
#         self.contentTopBg.setMaximumSize(QSize(16777215, 50))
#         self.contentTopBg.setFrameShape(QFrame.NoFrame)
#         self.contentTopBg.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout = QHBoxLayout(self.contentTopBg)
#         self.horizontalLayout.setSpacing(0)
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
#         self.leftBox = QFrame(self.contentTopBg)
#         self.leftBox.setObjectName(u"leftBox")
#         sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
#         sizePolicy1.setHorizontalStretch(0)
#         sizePolicy1.setVerticalStretch(0)
#         sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
#         self.leftBox.setSizePolicy(sizePolicy1)
#         self.leftBox.setFrameShape(QFrame.NoFrame)
#         self.leftBox.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
#         self.horizontalLayout_3.setSpacing(0)
#         self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.titleRightInfo = QLabel(self.leftBox)
#         self.titleRightInfo.setObjectName(u"titleRightInfo")
#         sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#         sizePolicy2.setHorizontalStretch(0)
#         sizePolicy2.setVerticalStretch(0)
#         sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
#         self.titleRightInfo.setSizePolicy(sizePolicy2)
#         self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
#         self.titleRightInfo.setFont(font)
#         self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

#         self.horizontalLayout_3.addWidget(self.titleRightInfo)


#         self.horizontalLayout.addWidget(self.leftBox)

#         self.rightButtons = QFrame(self.contentTopBg)
#         self.rightButtons.setObjectName(u"rightButtons")
#         self.rightButtons.setMinimumSize(QSize(0, 28))
#         self.rightButtons.setFrameShape(QFrame.NoFrame)
#         self.rightButtons.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
#         self.horizontalLayout_2.setSpacing(5)
#         self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
#         self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.settingsTopBtn = QPushButton(self.rightButtons)
#         self.settingsTopBtn.setObjectName(u"settingsTopBtn")
#         self.settingsTopBtn.setMinimumSize(QSize(28, 28))
#         self.settingsTopBtn.setMaximumSize(QSize(28, 28))
#         self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
#         icon1 = QIcon()
#         icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.settingsTopBtn.setIcon(icon1)
#         self.settingsTopBtn.setIconSize(QSize(20, 20))

#         self.horizontalLayout_2.addWidget(self.settingsTopBtn)

#         self.minimizeAppBtn = QPushButton(self.rightButtons)
#         self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
#         self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
#         self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
#         self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
#         icon2 = QIcon()
#         icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.minimizeAppBtn.setIcon(icon2)
#         self.minimizeAppBtn.setIconSize(QSize(20, 20))

#         self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

#         self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
#         self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
#         self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
#         self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
#         font3 = QFont()
#         font3.setFamilies([u"Segoe UI"])
#         font3.setPointSize(10)
#         font3.setBold(False)
#         font3.setItalic(False)
#         font3.setStyleStrategy(QFont.PreferDefault)
#         self.maximizeRestoreAppBtn.setFont(font3)
#         self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
#         icon3 = QIcon()
#         icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.maximizeRestoreAppBtn.setIcon(icon3)
#         self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

#         self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

#         self.closeAppBtn = QPushButton(self.rightButtons)
#         self.closeAppBtn.setObjectName(u"closeAppBtn")
#         self.closeAppBtn.setMinimumSize(QSize(28, 28))
#         self.closeAppBtn.setMaximumSize(QSize(28, 28))
#         self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
#         self.closeAppBtn.setIcon(icon)
#         self.closeAppBtn.setIconSize(QSize(20, 20))

#         self.horizontalLayout_2.addWidget(self.closeAppBtn)


#         self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


#         self.verticalLayout_2.addWidget(self.contentTopBg)

#         self.contentBottom = QFrame(self.contentBox)
#         self.contentBottom.setObjectName(u"contentBottom")
#         self.contentBottom.setFrameShape(QFrame.NoFrame)
#         self.contentBottom.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
#         self.verticalLayout_6.setSpacing(0)
#         self.verticalLayout_6.setObjectName(u"verticalLayout_6")
#         self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.content = QFrame(self.contentBottom)
#         self.content.setObjectName(u"content")
#         self.content.setFrameShape(QFrame.NoFrame)
#         self.content.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_4 = QHBoxLayout(self.content)
#         self.horizontalLayout_4.setSpacing(0)
#         self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
#         self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.pagesContainer = QFrame(self.content)
#         self.pagesContainer.setObjectName(u"pagesContainer")
#         self.pagesContainer.setStyleSheet(u"")
#         self.pagesContainer.setFrameShape(QFrame.NoFrame)
#         self.pagesContainer.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
#         self.verticalLayout_15.setSpacing(0)
#         self.verticalLayout_15.setObjectName(u"verticalLayout_15")
#         self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
#         self.stackedWidget = QStackedWidget(self.pagesContainer)
#         self.stackedWidget.setObjectName(u"stackedWidget")
#         self.stackedWidget.setStyleSheet(u"background-color: rgb(7, 7, 7);")
#         self.home = QWidget()
#         self.home.setObjectName(u"home")
#         self.home.setStyleSheet(u"")
#         self.label_2 = QLabel(self.home)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(480, 150, 261, 311))
#         self.label_2.setStyleSheet(u"")
#         self.label_2.setPixmap(QPixmap(u"download.png"))
#         self.stackedWidget.addWidget(self.home)
#         self.page_3 = QWidget()
#         self.page_3.setObjectName(u"page_3")
#         self.stackedWidget.addWidget(self.page_3)
#         self.widgets = QWidget()
#         self.widgets.setObjectName(u"widgets")
#         self.widgets.setStyleSheet(u"b")
#         self.verticalLayout = QVBoxLayout(self.widgets)
#         self.verticalLayout.setSpacing(10)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.verticalLayout.setContentsMargins(10, 10, 10, 10)
#         self.frame = QFrame(self.widgets)
#         self.frame.setObjectName(u"frame")
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setFrameShadow(QFrame.Raised)
#         self.label_3 = QLabel(self.frame)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(48, 47, 131, 61))
#         self.label_4 = QLabel(self.frame)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setGeometry(QRect(50, 140, 131, 61))
#         self.label_5 = QLabel(self.frame)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setGeometry(QRect(50, 220, 131, 61))
#         self.textEdit_2 = QTextEdit(self.frame)
#         self.textEdit_2.setObjectName(u"textEdit_2")
#         self.textEdit_2.setGeometry(QRect(170, 60, 231, 31))
#         palette = QPalette()
#         brush = QBrush(QColor(221, 221, 221, 255))
#         brush.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         brush1 = QBrush(QColor(7, 7, 7, 255))
#         brush1.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.Button, brush1)
#         brush2 = QBrush(QColor(0, 0, 0, 255))
#         brush2.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.Light, brush2)
#         palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
#         palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
#         palette.setBrush(QPalette.Active, QPalette.Mid, brush2)
#         palette.setBrush(QPalette.Active, QPalette.Text, brush)
#         brush3 = QBrush(QColor(255, 255, 255, 255))
#         brush3.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.BrightText, brush3)
#         palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#         palette.setBrush(QPalette.Active, QPalette.Shadow, brush2)
#         palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#         brush4 = QBrush(QColor(255, 255, 220, 255))
#         brush4.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
#         palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
#         brush5 = QBrush(QColor(221, 221, 221, 128))
#         brush5.setStyle(Qt.SolidPattern)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
#         palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#         palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#         palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
#         palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
#         palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#         palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
#         palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
#         palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_2.setPalette(palette)
#         self.textEdit_3 = QTextEdit(self.frame)
#         self.textEdit_3.setObjectName(u"textEdit_3")
#         self.textEdit_3.setGeometry(QRect(170, 150, 231, 31))
#         palette1 = QPalette()
#         palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette1.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_3.setPalette(palette1)
#         self.textEdit_4 = QTextEdit(self.frame)
#         self.textEdit_4.setObjectName(u"textEdit_4")
#         self.textEdit_4.setGeometry(QRect(170, 380, 221, 91))
#         palette2 = QPalette()
#         palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette2.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_4.setPalette(palette2)
#         self.insert_btn = QPushButton(self.frame)
#         self.insert_btn.setObjectName(u"insert_btn")
#         self.insert_btn.setGeometry(QRect(320, 550, 75, 24))
#         self.insert_btn.setStyleSheet(u"\n"
# "background-color: rgb(85, 0, 127);")
#         self.tableWidget = QTableWidget(self.frame)
#         if (self.tableWidget.columnCount() < 5):
#             self.tableWidget.setColumnCount(5)
#         if (self.tableWidget.rowCount() < 2000):
#             self.tableWidget.setRowCount(2000)
#         self.tableWidget.setObjectName(u"tableWidget")
#         self.tableWidget.setGeometry(QRect(430, 10, 721, 501))
#         self.tableWidget.setStyleSheet(u"border-top-color: rgb(85, 0, 127);")
#         self.tableWidget.setInputMethodHints(Qt.ImhNone)
#         self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setRowCount(2000)
#         self.tableWidget.setColumnCount(5)
#         self.tableWidget.horizontalHeader().setVisible(True)
#         self.tableWidget.horizontalHeader().setStretchLastSection(True)
#         self.tableWidget.verticalHeader().setVisible(False)
#         self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
#         self.remove_btn = QPushButton(self.frame)
#         self.remove_btn.setObjectName(u"remove_btn")
#         self.remove_btn.setGeometry(QRect(520, 540, 101, 24))
#         self.remove_btn.setStyleSheet(u"\n"
# "background-color: rgb(85, 0, 127);")
#         self.textEdit_5 = QTextEdit(self.frame)
#         self.textEdit_5.setObjectName(u"textEdit_5")
#         self.textEdit_5.setGeometry(QRect(30, 500, 361, 31))
#         palette3 = QPalette()
#         palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette3.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_5.setPalette(palette3)
#         def updateTextEdit():
#                 items = self.listWidget.selectedItems()
#                 selected_items_text = [str(item.text()) for item in items]
#                 current_text = self.textEdit_4.toPlainText()
#                 new_text = "\n".join(selected_items_text)
#                 if current_text:
#                         self.textEdit_4.setPlainText(current_text + ", " + new_text)
#                 else:
#                         self.textEdit_4.setPlainText(new_text)
#         self.listWidget = QListWidget(self.frame)
#         self.listWidget.setObjectName(u"listWidget")
#         self.listWidget.setGeometry(QRect(170, 230, 231, 121))
#         self.listWidget.setSelectionMode(

#             QAbstractItemView.SelectionMode.ExtendedSelection
#         )
#         # item = QListWidgetItem("Nausea")
#         # self.listWidget.addItem(item)
#         # # self.listWidget.itemSelectionChanged.connect(updateTextEdit)
        
#         # for i in range(10):
#         #     item = QListWidgetItem("Item %i" % i)
#         #     self.listWidget.addItem(item)

#         with open("project file 2.csv", 'r') as file:
#                 symptoms_file = csv.reader(file)
#                 next(symptoms_file)
#                 for symptoms,priority in symptoms_file:
#                         self.listWidget.addItem(symptoms)
#         self.listWidget.itemSelectionChanged.connect(updateTextEdit)

        

#         self.verticalLayout.addWidget(self.frame)

#         self.stackedWidget.addWidget(self.widgets)
#         self.new_page = QWidget()
#         self.new_page.setObjectName(u"new_page")
#         self.verticalLayout_20 = QVBoxLayout(self.new_page)
#         self.verticalLayout_20.setObjectName(u"verticalLayout_20")
#         self.frame_3 = QFrame(self.new_page)
#         self.frame_3.setObjectName(u"frame_3")
#         self.frame_3.setFrameShape(QFrame.StyledPanel)
#         self.frame_3.setFrameShadow(QFrame.Raised)
#         self.edit_btn_2 = QPushButton(self.frame_3)
#         self.edit_btn_2.setObjectName(u"edit_btn_2")
#         self.edit_btn_2.setGeometry(QRect(230, 540, 75, 24))
#         self.edit_btn_2.setStyleSheet(u"\n"
# "background-color: rgb(85, 0, 127);")
#         self.textEdit_9 = QTextEdit(self.frame_3)
#         self.textEdit_9.setObjectName(u"textEdit_9")
#         self.textEdit_9.setGeometry(QRect(150, 360, 231, 31))
#         palette4 = QPalette()
#         palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette4.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_9.setPalette(palette4)
#         self.label_10 = QLabel(self.frame_3)
#         self.label_10.setObjectName(u"label_10")
#         self.label_10.setGeometry(QRect(30, 350, 131, 61))
#         self.textEdit_10 = QTextEdit(self.frame_3)
#         self.textEdit_10.setObjectName(u"textEdit_10")
#         self.textEdit_10.setGeometry(QRect(150, 450, 231, 31))
#         palette5 = QPalette()
#         palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette5.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_10.setPalette(palette5)
#         self.tableWidget_3 = QTableWidget(self.frame_3)
#         if (self.tableWidget_3.columnCount() < 5):
#             self.tableWidget_3.setColumnCount(5)
#         if (self.tableWidget_3.rowCount() < 2000):
#             self.tableWidget_3.setRowCount(2000)
#         self.tableWidget_3.setObjectName(u"tableWidget_3")
#         self.tableWidget_3.setGeometry(QRect(470, 10, 691, 501))
#         self.tableWidget_3.setStyleSheet(u"border-top-color: rgb(85, 0, 127);")
#         self.tableWidget_3.setInputMethodHints(Qt.ImhNone)
#         self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.tableWidget_3.setAlternatingRowColors(False)
#         self.tableWidget_3.setRowCount(2000)
#         self.tableWidget_3.setColumnCount(5)
#         self.tableWidget_3.horizontalHeader().setVisible(True)
#         self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
#         self.tableWidget_3.verticalHeader().setVisible(False)
#         self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
#         self.label_11 = QLabel(self.frame_3)
#         self.label_11.setObjectName(u"label_11")
#         self.label_11.setGeometry(QRect(30, 260, 131, 61))
#         self.search_btn_2 = QPushButton(self.frame_3)
#         self.search_btn_2.setObjectName(u"search_btn_2")
#         self.search_btn_2.setGeometry(QRect(240, 140, 75, 24))
#         self.search_btn_2.setStyleSheet(u"\n"
# "background-color: rgb(85, 0, 127);")
#         self.textEdit_11 = QTextEdit(self.frame_3)
#         self.textEdit_11.setObjectName(u"textEdit_11")
#         self.textEdit_11.setGeometry(QRect(200, 70, 231, 31))
#         palette6 = QPalette()
#         palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette6.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_11.setPalette(palette6)
#         self.label_12 = QLabel(self.frame_3)
#         self.label_12.setObjectName(u"label_12")
#         self.label_12.setGeometry(QRect(20, 50, 171, 61))
#         self.label_13 = QLabel(self.frame_3)
#         self.label_13.setObjectName(u"label_13")
#         self.label_13.setGeometry(QRect(30, 440, 131, 61))
#         self.restet_btn = QPushButton(self.frame_3)
#         self.restet_btn.setObjectName(u"reset_btn")
#         self.restet_btn.setGeometry(QRect(330, 140, 75, 24))
#         self.restet_btn.setStyleSheet(u"\n"
# "background-color: rgb(85, 0, 127);")
#         self.textEdit_12 = QTextEdit(self.frame_3)
#         self.textEdit_12.setObjectName(u"textEdit_12")
#         self.textEdit_12.setGeometry(QRect(160, 280, 231, 31))
#         palette7 = QPalette()
#         palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
#         palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
#         palette7.setBrush(QPalette.Active, QPalette.Text, brush)
#         palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#         palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
#         palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
# #endif
#         palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#         palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
#         palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
#         palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#         palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
#         palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
# #endif
#         palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
#         palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
#         palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
#         palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#         palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
#         palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#         palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# #endif
#         self.textEdit_12.setPalette(palette7)

#         self.verticalLayout_20.addWidget(self.frame_3)

#         self.stackedWidget.addWidget(self.new_page)

#         self.verticalLayout_15.addWidget(self.stackedWidget)


#         self.horizontalLayout_4.addWidget(self.pagesContainer)

#         self.extraRightBox = QFrame(self.content)
#         self.extraRightBox.setObjectName(u"extraRightBox")
#         self.extraRightBox.setMinimumSize(QSize(0, 0))
#         self.extraRightBox.setMaximumSize(QSize(0, 16777215))
#         self.extraRightBox.setFrameShape(QFrame.NoFrame)
#         self.extraRightBox.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
#         self.verticalLayout_7.setSpacing(0)
#         self.verticalLayout_7.setObjectName(u"verticalLayout_7")
#         self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
#         self.themeSettingsTopDetail = QFrame(self.extraRightBox)
#         self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
#         self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
#         self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
#         self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

#         self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

#         self.contentSettings = QFrame(self.extraRightBox)
#         self.contentSettings.setObjectName(u"contentSettings")
#         self.contentSettings.setFrameShape(QFrame.NoFrame)
#         self.contentSettings.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
#         self.verticalLayout_13.setSpacing(0)
#         self.verticalLayout_13.setObjectName(u"verticalLayout_13")
#         self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
#         self.topMenus = QFrame(self.contentSettings)
#         self.topMenus.setObjectName(u"topMenus")
#         self.topMenus.setFrameShape(QFrame.NoFrame)
#         self.topMenus.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_14 = QVBoxLayout(self.topMenus)
#         self.verticalLayout_14.setSpacing(0)
#         self.verticalLayout_14.setObjectName(u"verticalLayout_14")
#         self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
#         self.btn_message = QPushButton(self.topMenus)
#         self.btn_message.setObjectName(u"btn_message")
#         sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
#         self.btn_message.setSizePolicy(sizePolicy)
#         self.btn_message.setMinimumSize(QSize(0, 45))
#         self.btn_message.setFont(font)
#         self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_message.setLayoutDirection(Qt.LeftToRight)
#         self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

#         self.verticalLayout_14.addWidget(self.btn_message)

#         self.btn_print = QPushButton(self.topMenus)
#         self.btn_print.setObjectName(u"btn_print")
#         sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
#         self.btn_print.setSizePolicy(sizePolicy)
#         self.btn_print.setMinimumSize(QSize(0, 45))
#         self.btn_print.setFont(font)
#         self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_print.setLayoutDirection(Qt.LeftToRight)
#         self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

#         self.verticalLayout_14.addWidget(self.btn_print)

#         self.btn_logout = QPushButton(self.topMenus)
#         self.btn_logout.setObjectName(u"btn_logout")
#         sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
#         self.btn_logout.setSizePolicy(sizePolicy)
#         self.btn_logout.setMinimumSize(QSize(0, 45))
#         self.btn_logout.setFont(font)
#         self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_logout.setLayoutDirection(Qt.LeftToRight)
#         self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

#         self.verticalLayout_14.addWidget(self.btn_logout)


#         self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


#         self.verticalLayout_7.addWidget(self.contentSettings)


#         self.horizontalLayout_4.addWidget(self.extraRightBox)


#         self.verticalLayout_6.addWidget(self.content)

#         self.bottomBar = QFrame(self.contentBottom)
#         self.bottomBar.setObjectName(u"bottomBar")
#         self.bottomBar.setMinimumSize(QSize(0, 22))
#         self.bottomBar.setMaximumSize(QSize(16777215, 22))
#         self.bottomBar.setFrameShape(QFrame.NoFrame)
#         self.bottomBar.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
#         self.horizontalLayout_5.setSpacing(0)
#         self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
#         self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.version = QLabel(self.bottomBar)
#         self.version.setObjectName(u"version")
#         self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

#         self.horizontalLayout_5.addWidget(self.version)

#         self.frame_size_grip = QFrame(self.bottomBar)
#         self.frame_size_grip.setObjectName(u"frame_size_grip")
#         self.frame_size_grip.setMinimumSize(QSize(20, 0))
#         self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
#         self.frame_size_grip.setFrameShape(QFrame.NoFrame)
#         self.frame_size_grip.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_5.addWidget(self.frame_size_grip)


#         self.verticalLayout_6.addWidget(self.bottomBar)


#         self.verticalLayout_2.addWidget(self.contentBottom)


#         self.appLayout.addWidget(self.contentBox)


#         self.appMargins.addWidget(self.bgApp)

#         MainWindow.setCentralWidget(self.styleSheet)

#         self.retranslateUi(MainWindow)

#         self.stackedWidget.setCurrentIndex(2)


#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
#         self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
#         self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#         self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#         self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
#         self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
#         self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
# #if QT_CONFIG(tooltip)
#         self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
# #endif // QT_CONFIG(tooltip)
#         self.extraCloseColumnBtn.setText("")
#         self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
#         self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
#         self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
#         self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
#                         "o Rocha.</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
#                         "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
# "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
#         self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Medical Triage System-DSII Project", None))
# #if QT_CONFIG(tooltip)
#         self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
# #endif // QT_CONFIG(tooltip)
#         self.settingsTopBtn.setText("")
# #if QT_CONFIG(tooltip)
#         self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
# #endif // QT_CONFIG(tooltip)
#         self.minimizeAppBtn.setText("")
# #if QT_CONFIG(tooltip)
#         self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
# #endif // QT_CONFIG(tooltip)
#         self.maximizeRestoreAppBtn.setText("")
# #if QT_CONFIG(tooltip)
#         self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
# #endif // QT_CONFIG(tooltip)
#         self.closeAppBtn.setText("")
#         self.label_2.setText("")
#         self.label_3.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
#         self.label_4.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
#         self.label_5.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None))
#         self.insert_btn.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
#         self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Admit Patient", None))
#         self.edit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
#         self.label_10.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
#         self.label_11.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
#         self.search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#         self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter Patient ID to search", None))
#         self.label_13.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None))
#         self.restet_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#         self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
#         self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#         self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#         self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
#     # retranslateUi

