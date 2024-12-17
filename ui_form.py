# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMaximumSize(QSize(600, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.table_frame = QFrame(MainWindow)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.table_lo = QVBoxLayout(self.table_frame)
        self.table_lo.setSpacing(20)
        self.table_lo.setObjectName(u"table_lo")
        self.table_lo.setContentsMargins(20, 20, 20, 20)
        self.table = QTableWidget(self.table_frame)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(222, 221, 218));
        __qtablewidgetitem.setForeground(brush);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(222, 221, 218));
        __qtablewidgetitem1.setForeground(brush);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(98, 160, 234);")
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setWordWrap(False)
        self.table.setCornerButtonEnabled(False)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setMinimumSectionSize(200)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.table_lo.addWidget(self.table)

        self.btn_lo2 = QHBoxLayout()
        self.btn_lo2.setSpacing(10)
        self.btn_lo2.setObjectName(u"btn_lo2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btn_lo2.addItem(self.horizontalSpacer_2)

        self.btn_new = QPushButton(self.table_frame)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")

        self.btn_lo2.addWidget(self.btn_new)

        self.btn_edit = QPushButton(self.table_frame)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")

        self.btn_lo2.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.table_frame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")

        self.btn_lo2.addWidget(self.btn_delete)


        self.table_lo.addLayout(self.btn_lo2)


        self.verticalLayout.addWidget(self.table_frame)

        self.btn_lo1 = QHBoxLayout()
        self.btn_lo1.setSpacing(10)
        self.btn_lo1.setObjectName(u"btn_lo1")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btn_lo1.addItem(self.horizontalSpacer)

        self.btn_ok = QPushButton(MainWindow)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setAutoFillBackground(False)
        self.btn_ok.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")

        self.btn_lo1.addWidget(self.btn_ok)

        self.btn_close = QPushButton(MainWindow)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")

        self.btn_lo1.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.btn_lo1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Environment Variables", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

