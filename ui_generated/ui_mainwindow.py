# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowaccvsM.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 448)
        icon = QIcon(QIcon.fromTheme(u"help-browser"))
        MainWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.title_button = QPushButton(MainWindow)
        self.title_button.setObjectName(u"title_button")
        font = QFont()
        font.setPointSize(22)
        self.title_button.setFont(font)
        self.title_button.setStyleSheet(u"background: transparent; border-radius: 1px; border-color: transparent;")
        self.title_button.setIcon(icon)
        self.title_button.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.title_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.envvars_button = QPushButton(MainWindow)
        self.envvars_button.setObjectName(u"envvars_button")
        self.envvars_button.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.envvars_button, 1, 0, 1, 1)

        self.remove_lockfile_button = QPushButton(MainWindow)
        self.remove_lockfile_button.setObjectName(u"remove_lockfile_button")
        self.remove_lockfile_button.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.remove_lockfile_button, 0, 0, 1, 1)

        self.bootloader_settings_button = QPushButton(MainWindow)
        self.bootloader_settings_button.setObjectName(u"bootloader_settings_button")
        self.bootloader_settings_button.setMinimumSize(QSize(0, 50))
        self.bootloader_settings_button.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.bootloader_settings_button, 2, 0, 1, 1)

        self.quit_button = QPushButton(MainWindow)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setMinimumSize(QSize(0, 50))
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.quit_button.setIcon(icon1)

        self.gridLayout.addWidget(self.quit_button, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GDL Helper", None))
        self.title_button.setText(QCoreApplication.translate("MainWindow", u" GDL Helper", None))
        self.envvars_button.setText(QCoreApplication.translate("MainWindow", u" Environment variables", None))
        self.remove_lockfile_button.setText(QCoreApplication.translate("MainWindow", u"Remove pacman lockfile", None))
        self.bootloader_settings_button.setText(QCoreApplication.translate("MainWindow", u" Bootloader settings", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u" Quit", None))
    # retranslateUi

