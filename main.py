import sys
from typing import Optional

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

import math


from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt #design.py
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QGridLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                    "                color: white;\n"
                                    "                background-color: #121212;\n"
                                    "                font-family: Rubik;\n"
                                    "                font-size: 16pt;\n"
                                    "                font-weight: 600;\n"
                                    "                }\n"
                                    "\n"
                                    "                QPushButton {\n"
                                    "                background-color: transparent;\n"
                                    "                border: none;\n"
                                    "                }\n"
                                    "\n"
                                    "                QPushButton:hover {\n"
                                    "                background-color: #666;\n"
                                    "                }\n"
                                    "\n"
                                    "                QPushButton:pressed {\n"
                                    "                background-color: #888;\n"
                                    "                }\n"
                                    "            ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = CustomLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
                                    "                                border: none;\n"
                                    "                            ")
        self.le_entry.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy2)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_calc, 4, 3, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy2)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"kuryator", None))
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"Внос", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"Вынос", None))
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"√", None))
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, # design_ui
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)


def setupUi(self, MainWindow):
    if not MainWindow.objectName():
        MainWindow.setObjectName(u"MainWindow")
    MainWindow.resize(300, 500)
    MainWindow.setMinimumSize(QSize(300, 500))
    MainWindow.setStyleSheet(u"QWidget {\n"
"                color: white;\n"
"                background-color: #121212;\n"
"                font-family: Rubik;\n"
"                font-size: 16pt;\n"
"                font-weight: 600;\n"
"                }\n"
"\n"
"                QPushButton {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                }\n"
"\n"
"                QPushButton:hover {\n"
"                background-color: #666;\n"
"                }\n"
"\n"
"                QPushButton:pressed {\n"
"                background-color: #888;\n"
"                }\n"
"            ")
    self.centralwidget = QWidget(MainWindow)
    self.centralwidget.setObjectName(u"centralwidget")
    self.verticalLayout = QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(u"verticalLayout")
    self.lbl_temp = QLabel(self.centralwidget)
    self.lbl_temp.setObjectName(u"lbl_temp")
    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
    self.lbl_temp.setSizePolicy(sizePolicy)
    self.lbl_temp.setStyleSheet(u"color: #888;")
    self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

    self.verticalLayout.addWidget(self.lbl_temp)

    self.le_entry = QLineEdit(self.centralwidget)
    self.le_entry.setObjectName(u"le_entry")
    sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
    self.le_entry.setSizePolicy(sizePolicy1)
    self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"                                border: none;\n"
"                            ")
    self.le_entry.setMaxLength(16)
    self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
    self.le_entry.setReadOnly(True)

    self.verticalLayout.addWidget(self.le_entry)

    self.layout_buttons = QGridLayout()
    self.layout_buttons.setObjectName(u"layout_buttons")
    self.btn_clear = QPushButton(self.centralwidget)
    self.btn_clear.setObjectName(u"btn_clear")
    sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
    sizePolicy2.setHorizontalStretch(0)
    sizePolicy2.setVerticalStretch(0)
    sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
    self.btn_clear.setSizePolicy(sizePolicy2)
    self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

    self.btn_7 = QPushButton(self.centralwidget)
    self.btn_7.setObjectName(u"btn_7")
    sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
    self.btn_7.setSizePolicy(sizePolicy2)
    self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

    self.btn_0 = QPushButton(self.centralwidget)
    self.btn_0.setObjectName(u"btn_0")
    sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
    self.btn_0.setSizePolicy(sizePolicy2)
    self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

    self.btn_1 = QPushButton(self.centralwidget)
    self.btn_1.setObjectName(u"btn_1")
    sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
    self.btn_1.setSizePolicy(sizePolicy2)
    self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

    self.btn_neg = QPushButton(self.centralwidget)
    self.btn_neg.setObjectName(u"btn_neg")
    sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
    self.btn_neg.setSizePolicy(sizePolicy2)
    self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_neg, 4, 0, 1, 1)

    self.btn_4 = QPushButton(self.centralwidget)
    self.btn_4.setObjectName(u"btn_4")
    sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
    self.btn_4.setSizePolicy(sizePolicy2)
    self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

    self.btn_point = QPushButton(self.centralwidget)
    self.btn_point.setObjectName(u"btn_point")
    sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
    self.btn_point.setSizePolicy(sizePolicy2)
    self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

    self.btn_calc = QPushButton(self.centralwidget)
    self.btn_calc.setObjectName(u"btn_calc")
    sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
    self.btn_calc.setSizePolicy(sizePolicy2)
    self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_calc, 4, 3, 1, 1)

    self.btn_add = QPushButton(self.centralwidget)
    self.btn_add.setObjectName(u"btn_add")
    sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
    self.btn_add.setSizePolicy(sizePolicy2)
    self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_add, 3, 3, 1, 1)

    self.btn_sub = QPushButton(self.centralwidget)
    self.btn_sub.setObjectName(u"btn_sub")
    sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
    self.btn_sub.setSizePolicy(sizePolicy2)
    self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_sub, 2, 3, 1, 1)

    self.btn_mul = QPushButton(self.centralwidget)
    self.btn_mul.setObjectName(u"btn_mul")
    sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
    self.btn_mul.setSizePolicy(sizePolicy2)
    self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_mul, 1, 3, 1, 1)

    self.btn_div = QPushButton(self.centralwidget)
    self.btn_div.setObjectName(u"btn_div")
    sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
    self.btn_div.setSizePolicy(sizePolicy2)
    self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_div, 0, 3, 1, 1)

    self.btn_backspace = QPushButton(self.centralwidget)
    self.btn_backspace.setObjectName(u"btn_backspace")
    sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
    self.btn_backspace.setSizePolicy(sizePolicy2)
    self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
    self.btn_backspace.setIconSize(QSize(24, 24))

    self.layout_buttons.addWidget(self.btn_backspace, 0, 2, 1, 1)

    self.btn_ce = QPushButton(self.centralwidget)
    self.btn_ce.setObjectName(u"btn_ce")
    sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
    self.btn_ce.setSizePolicy(sizePolicy2)
    self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)

    self.btn_8 = QPushButton(self.centralwidget)
    self.btn_8.setObjectName(u"btn_8")
    sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
    self.btn_8.setSizePolicy(sizePolicy2)
    self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

    self.btn_9 = QPushButton(self.centralwidget)
    self.btn_9.setObjectName(u"btn_9")
    sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
    self.btn_9.setSizePolicy(sizePolicy2)
    self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

    self.btn_6 = QPushButton(self.centralwidget)
    self.btn_6.setObjectName(u"btn_6")
    sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
    self.btn_6.setSizePolicy(sizePolicy2)
    self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

    self.btn_5 = QPushButton(self.centralwidget)
    self.btn_5.setObjectName(u"btn_5")
    sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
    self.btn_5.setSizePolicy(sizePolicy2)
    self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

    self.btn_2 = QPushButton(self.centralwidget)
    self.btn_2.setObjectName(u"btn_2")
    sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
    self.btn_2.setSizePolicy(sizePolicy2)
    self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

    self.btn_3 = QPushButton(self.centralwidget)
    self.btn_3.setObjectName(u"btn_3")
    sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
    self.btn_3.setSizePolicy(sizePolicy2)
    self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

    self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)


    self.verticalLayout.addLayout(self.layout_buttons)

    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)

    QMetaObject.connectSlotsByName(MainWindow)
# setupUi

def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"kuryator", None))
    self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
    self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
    self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
    self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
    self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
    self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
    self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
    self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
    self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
    self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
    self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
    self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
    self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
    self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
    self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
    self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
    self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
#if QT_CONFIG(shortcut)
    self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
    self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
    self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
    self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
    self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
    self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
    self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
    self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
    self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
    self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
    self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
    self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
    self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
    self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
    self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
    self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
    self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
    self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
# retranslateUi





class CustomLabel(QLabel): # custom_label.py
    textChanged = Signal()

    def setText(self, text):
        super().setText(text)
        self.textChanged.emit()




ERROR_ZERO_DIV = 'Division by zero' #config.py
ERROR_UNDEFINED = 'Result is undefined'

DEFAULT_FONT_SIZE = 16
DEFAULT_ENTRY_FONT_SIZE = 40

DIGIT_BUTTONS = [f'btn_{num}' for num in range(10)]
MATH_OPERATIONS = ['btn_add', 'btn_sub', 'btn_mul', 'btn_div']
BUTTONS_TO_DISABLE = [
    'btn_calc', 'btn_add', 'btn_sub',
    'btn_mul', 'btn_div', 'btn_neg', 'btn_point'
]




ch = 1

def vynos_celogo_chisla(number): # выносит целое число
    global ch
    number2 = math.sqrt(number)
    if str(number2).find(".") == len(str(number2))-2 and ch == 1:
        ch = 1
        return int(str(number2)[:-2]), 0
    number2 = 10
    while number2**2 < number:
        number2 += 10
    for i in range(number2-10, number2+1):
        for k in range(number2-10, number2+1):
            if i*k == number:
                for l in range(1, k):
                    if l*l == k:
                        ch = 1
                        return l, i
    ch = 1
    return 0, 0

def vynos_NeCelogo_chisla(number): # выносит не целое число
    number2 = number
    decrease = "1"
    global ch
    for i in range(len(str(number2))-1, 0, -1):
        if str(number2)[i] == "e":
            decrease += "0"*int(str(number2)[i+2:])
            break
    number2 *= float(decrease)
    decrease = 1/int(decrease)
    dlina = len(str(number2)[(str(number2).find("."))+1:])
    while str(number2)[-1] != "0" or str(number2)[-2] != ".":
        number2 *= 10
        decrease /= 10
        dlina -= 1
        number2 = round(number2, dlina)
    number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 == 0 and number3 != 0:
        if len(str(number)[str(number).find(".")+1:])%2 == 0:
            number3 /= int("1"+("0"*((len(str(decrease))-1)//2)))
        else:
            ch = 2
            number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 != 0 and number3 != 0:
        flag = True
        for t in range(0, len(str(decrease))): # Смотрим длину после точки у первого числа
            for i in range(0, len(str(decrease))): # Смотрим длину после точки у второго числа
                if round(round(((number3/int("1"+"0"*t))**2), t*2)*round((number4/int("1"+"0"*i)), i*2), i*2+t*2) == number:
                    number3 = number3/int("1"+"0"*t)
                    number4 = number4/int("1"+"0"*i)
                    if i == 0:
                        number4 = int(number4)
                    if t == 0:
                        number3 = int(number3)
                    flag = False
                    break
            if flag == False:
                break
        if flag == True:
            number3, number4 = 0, 0
    return number3, number4

def proverka_dlin_chisla(number):
    flag = True
    number = str(number)
    tochka = str(number).find(".")
    for t in range(tochka+2, len(str(number[tochka+1:]))): # Смотрим длину после точки у первого числа
        if t != len(number)-2:
            if  number[t+1] == number[t]:
                for i in range(t+2, len(str(number[tochka+1:]))):
                    if number[i] == number[t+2]:
                        if i-t >= 3:
                            if int(number[t+2]) > 5:
                                number = number[:t-1]+str(int(number[t-1])+1)
                                flag = False
                            else:
                                number = number[:t]
                                flag = False
                            break
                    else:
                        break
        if flag == False:
            break
    if number[-1] == "0" and number[-2] == ".":
        number = number[:-2]
    return number

class Calculator(QMainWindow):
    def VynosIzPodKoren(self): #вынос из под корня
            koren = self.entry.text().replace(" ", "")
            c = 0 # проверка правильно ли стоит знак корня в строке
            f = 0 # проверка правильно ли стоит знак деления
            g = 0 # проверка правильно ли стоят числа с плавающей запятой
            f2 = 0 # проверка не стоит ли знак деления в конце или в начале
            g2 = 0 # проверка не стоит ли точка в конце или в начале  
            c2 = 0 # проверка не стоит ли знак корня в конце 
            for i in range(0, len(koren)-1):
                if koren[i] == "√":
                    c += 1
                if koren[i] == "/":
                    f += 1
                if koren[i] == ".":
                    g += 1
                if koren[i] == "√" and i == len(koren):
                    c2 += 1
                if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                    g2 += 1
                if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                    f2 += 1
            if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
                return "Некорректный ввод"
            elif len(koren) == 1:
                return "Некорректный ввод"
            else:
                a = str(koren).find("√")
                NeKPL = True # проверяет есть ли число с плавающей запятой вне корня
                KPL = True # проверяет есть ли число с плавающей запятой под корнем
                KDR = True # проверяет есть ли дробь под корняем
                NeKDR = True # проверяет есть ли дробь вне корня
                Drob_Ne = 0
                Drob_V = 0
                for i in range(a+1, len(koren)):
                    if koren[i] == ".":
                        KPL = False  
                for i in range(a):
                    if koren[i] ==".":
                        NeKPL = False
                for i in range(a+1, len(koren)):
                    if koren[i] == "/":
                        KDR = False
                        Drob_V = i
                for i in range(a):
                    if koren[i] == "/":
                        NeKDR = False
                        Drob_Ne = i
                if KDR == True and (KPL == True or KPL == False):
                    if str(koren[a+1:]).find(".") == -1:
                        number, number2 = vynos_celogo_chisla(int(koren[a+1:]))
                    else:
                        number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:]))
                    if NeKDR == True and (NeKPL == True or NeKPL == False): # если вне корня либо целое число, либо числа нету
                        if number == 0 and number2 == 0: 
                            return f"Число иррациональное"
                        else:
                            if a != 0:
                                if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                    numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                                else: # если число вне корня не целое
                                    if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                        numerator = str(number*float(koren[:a]))[:-2]
                                    else:
                                        numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                            else:
                                numerator = number
                            if number2 == 0: # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}"
                            elif number2 != 0: # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}√{number2}"
                            else:
                                if number2 == 0:
                                    return f"{number}"
                                else:
                                    return f"{number}√{number2}"
                    elif NeKDR == False and (NeKPL == True or NeKPL == False): # если вне корня дробь
                        if number == 0 and number2 == 0:
                            return f"Число иррациональное"
                        else:
                            if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                            else: # если число вне корня не целое
                                if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                    numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                                else:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                            if koren[:a] != "" and number2 == 0: # если вне дроби нету числа и число расскладывается нацело
                                return f"{numerator}/{koren[Drob_Ne+1:a]}"
                            elif koren[:a] != "" and number2 != 0 : # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}√{number2}/{koren[Drob_Ne+1:a]}"
                elif KDR == False and (KPL == False or KPL == True):
                    if koren[a+1:Drob_V].find(".") == -1:
                        number, number2 = vynos_celogo_chisla(int(koren[a+1:Drob_V]))
                    else:
                        number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:Drob_V]))
                    if koren[Drob_V+1:].find(".") == -1:
                        number3, number4 = vynos_celogo_chisla(int(koren[Drob_V+1:]))
                    else:
                        number3, number4 = vynos_NeCelogo_chisla(float(koren[Drob_V+1:]))
                    if NeKDR == True and (NeKPL == True or NeKPL == False):  # если вне корня либо целое число, либо числа нету
                        if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                            return f"Число иррациональное"
                        else:
                            if a != 0:
                                if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                    numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                                else: # если число вне корня не целое
                                    if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                        numerator = str(number*float(koren[:a]))[:-2]
                                    else:
                                        numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                            else:
                                numerator = number
                            if number2 == 0 and number4 == 0: # если исло расскладывается нацело и знаменатель расскадывается нацело
                                return f"{numerator}/{number3}" 
                            elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                                return f"{numerator}/{number3}√{number4}" 
                            elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                                return f"{numerator}√{number2}/{number3}"
                            elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                                return f"{numerator}√{number2}/{number3}√{number4}"
                    elif NeKDR == False and (NeKPL == False or NeKPL == True): # если вне корня либо дробь с целыми числами, либо дробь с числа с плавающей запятой, либо смешаная дробь
                        if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                            return f"Число иррациональное"
                        else:
                            if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                            else: # если число вне корня не целое
                                if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                    numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                                else:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                            if str(koren[Drob_Ne+1:a]).isdigit() == True: # если число в корне целое
                                denominator = proverka_dlin_chisla(float(number3*int(koren[Drob_Ne+1:a])))
                            else: # если число в корне не целое
                                if str(number3*float(koren[Drob_Ne+1:a]))[-1] == "0" and str(number3*float(koren[Drob_Ne+1:a]))[-2] == ".":
                                    denominator = str(number3*float(koren[Drob_Ne+1:a]))[:-2]
                                else:
                                    denominator = proverka_dlin_chisla(float(number3*float(koren[Drob_Ne+1:a])))
                            if number2 == 0 and number4 == 0: # если число расскладывается нацело и знаменатель расскадывается нацело
                                return f"{numerator}/{denominator}" 
                            elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                                return f"{numerator}/{denominator}√{number4}" 
                            elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                                return f"{numerator}√{number2}/{denominator}"
                            elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                                return f"{numerator}√{number2}/{denominator}√{number4}"
        
    def VnosPodKoren(self):
        koren = self.entry.text().replace(" ", "")
        c = 0
        f = 0
        g = 0
        f2 = 0
        g2 = 0
        c2 = 0
        for i in range(0, len(koren)-1):
            if koren[i] == "√":
                c += 1
            if koren[i] == "/":
                f += 1
            if koren[i] == ".":
                g += 1
            if koren[i] == "√" and i == 0:
                c2 += 1
            if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                g2 += 1
            if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                f2 += 1
        if koren[len(koren)-1] == "√":
            c += 1
        if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
            return "Некорректный ввод"
        elif len(koren) == 1:
            return "Некорректный ввод"
        else:
            a = str(koren).find("√")
            Drob_Ne = a
            Drob_V = len(koren)
            number2 = 0
            for i in range(a+1, len(koren)):
                if koren[i] == "/":
                    Drob_V = i
            for i in range(a):
                if koren[i] == "/":
                    Drob_Ne = i
            if str(koren[:Drob_Ne]).isdigit() == True:
                number = int(koren[:Drob_Ne])**2
            else:
                number = float(koren[:Drob_Ne])**2
            if Drob_Ne != a:
                if str(koren[Drob_Ne+1:a]).isdigit() == True:
                    number2 = int(koren[Drob_Ne+1:a])**2
                else:
                    number2 = float(koren[Drob_Ne+1:a])**2
            if str(koren[a+1:Drob_V]).isdigit() == True and len(koren[a+1:Drob_V]) != 0:
                number *= int(koren[a+1:Drob_V])
            elif str(koren[a+1:Drob_V]).isdigit() != True and len(koren[a+1:Drob_V]) != 0:
                number *= float(koren[a+1:Drob_V])
            if Drob_V != len(koren):
                if number2 == 0:
                    number2 = 1
                if str(koren[Drob_V+1:]).isdigit() == True and len(koren[Drob_V+1:]) != 0:
                    number2 *= int(koren[Drob_V+1:])
                elif str(koren[Drob_V+1:]).isdigit() != True and len(koren[Drob_V+1:]) != 0:
                    number2 *= float(koren[Drob_V+1:])
            if type(number) == float:
                if str(number)[-1] == "0" and str(number)[-2] == ".":
                    number = int(str(number)[:-2])
            if type(number2) == float:
                if str(number2)[-1] == "0" and str(number2)[-2] == ".":
                    number2 = int(str(number2)[:-2])
            if number2 == 0:
                return f"√{number}"
            else:
                return f"√{number}/{number2}"

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.le_entry
        self.temp = self.ui.lbl_temp
        self.entry_max_len = self.entry.maxLength()

        QFontDatabase.addApplicationFont("ui/fonts/Rubik-Regular.ttf")

        self.connect_digit_buttons()
        self.connect_math_operations()
        self.connect_other_buttons()

        self.entry.textChanged.connect(self.adjust_entry_font_size)
        self.temp.textChanged.connect(self.adjust_temp_font_size)

    def connect_digit_buttons(self) -> None:
        for btn in DIGIT_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)

    def connect_math_operations(self) -> None:
        self.ui.btn_calc.clicked.connect(self.calculate)
        for btn in MATH_OPERATIONS:
            getattr(self.ui, btn).clicked.connect(self.math_operation)

    def connect_other_buttons(self) -> None: 
        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_neg.clicked.connect(self.negate)
        self.ui.btn_backspace.clicked.connect(self.backspace)

    def add_digit(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        if btn.objectName() in DIGIT_BUTTONS:
            self.temp.setText("")
            if self.entry.text() == '0' or self.entry.text() == "Некорректный ввод" or self.entry.text() == "Число иррациональное":
                self.entry.setText(btn.text())
                self.temp.setText("") 
            else:
                self.entry.setText(self.entry.text() + btn.text())

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        self.entry.setText(self.entry.text() + '.')

    def negate(self) -> None:
        self.temp.setText("")
        self.temp.setText(self.entry.text() + ' =')
        self.entry.setText(self.VnosPodKoren())

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            self.entry.setText(entry[:-1])
        else:
            self.entry.setText('0')

    def clear_all(self) -> None:
        self.remove_error()
        self.entry.setText('0')
        self.temp.clear()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.entry.clear()

    @staticmethod
    def remove_trailing_zeros(number) -> str:
        return number

    def add_temp(self) -> None:
        btn = self.sender()
        if self.entry.text() == '0':
             self.entry.setText(btn.text())
        elif self.entry.text() == "Некорректный ввод" or self.entry.text() == "Число иррациональное":
            self.entry.setText(btn.text())
            self.temp.setText("")
        else:
            self.entry.setText(self.entry.text() + btn.text())

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().strip('.').split()[-1]

    def get_entry_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width()

    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()

    def calculate(self) -> Optional[str]:
        try:
            result = self.remove_trailing_zeros(self.VynosIzPodKoren())
            self.temp.setText("")

            self.temp.setText(self.temp.text() +
                              self.remove_trailing_zeros(self.entry.text()) + ' =')

            self.entry.setText(result)

            return result

        except KeyError:
            pass
        except ZeroDivisionError:
            self.show_zero_division_error()

    def show_zero_division_error(self) -> None:
        if self.get_temp_num() == 0:
            self.show_error(ERROR_UNDEFINED)
        else:
            self.show_error(ERROR_ZERO_DIV)

    def math_operation(self) -> None:
        btn = self.sender()
        if btn.text() == "+" or btn.text() == "\u2212":
            self.temp.setText("Скоро будте;)")
        elif not self.temp.text():
            self.add_temp()
        elif btn.text() == "√":
            self.temp.setText("")
            self.entry.setText("√")

    def replace_temp_sign(self) -> None:
        btn = self.sender()
        self.temp.setText(self.temp.text()[:-2] + f'{btn.text()} ')

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (ERROR_UNDEFINED, ERROR_ZERO_DIV):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        for btn in BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        for btn in BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = DEFAULT_ENTRY_FONT_SIZE
        while self.get_entry_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

        font_size = 1
        while self.get_entry_text_width() < self.entry.width() - 60:
            font_size += 1

            if font_size > DEFAULT_ENTRY_FONT_SIZE:
                break

            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = DEFAULT_FONT_SIZE
        while self.get_temp_text_width() > self.temp.width() - 10:
            font_size -= 1
            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 60:
            font_size += 1

            if font_size > DEFAULT_FONT_SIZE:
                break

            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
