# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_dialog_form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_NewDialog(object):
    def setupUi(self, NewDialog):
        if not NewDialog.objectName():
            NewDialog.setObjectName(u"NewDialog")
        NewDialog.setWindowModality(Qt.WindowModality.NonModal)
        NewDialog.resize(550, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewDialog.sizePolicy().hasHeightForWidth())
        NewDialog.setSizePolicy(sizePolicy)
        NewDialog.setMinimumSize(QSize(550, 200))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(222, 221, 218, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(238, 238, 236, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(111, 110, 109, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(148, 147, 145, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(239, 239, 239, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        brush9 = QBrush(QColor(202, 202, 202, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        brush10 = QBrush(QColor(159, 159, 159, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush10)
        brush11 = QBrush(QColor(184, 184, 184, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush12 = QBrush(QColor(118, 118, 118, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush12)
        brush13 = QBrush(QColor(247, 247, 247, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush15 = QBrush(QColor(177, 177, 177, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        NewDialog.setPalette(palette)
        self.verticalLayout = QVBoxLayout(NewDialog)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label2 = QLabel(NewDialog)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.label1 = QLabel(NewDialog)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.new_var_entry = QLineEdit(NewDialog)
        self.new_var_entry.setObjectName(u"new_var_entry")
        self.new_var_entry.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.gridLayout.addWidget(self.new_var_entry, 0, 1, 1, 1)

        self.new_values_entry = QLineEdit(NewDialog)
        self.new_values_entry.setObjectName(u"new_values_entry")
        self.new_values_entry.setToolTipDuration(3)

        self.gridLayout.addWidget(self.new_values_entry, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_browse_dir = QPushButton(NewDialog)
        self.btn_browse_dir.setObjectName(u"btn_browse_dir")
        self.btn_browse_dir.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_3.addWidget(self.btn_browse_dir)

        self.btn_browse_file = QPushButton(NewDialog)
        self.btn_browse_file.setObjectName(u"btn_browse_file")
        self.btn_browse_file.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_3.addWidget(self.btn_browse_file)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(NewDialog)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_cancel = QPushButton(NewDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_3.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(NewDialog)

        QMetaObject.connectSlotsByName(NewDialog)
    # setupUi

    def retranslateUi(self, NewDialog):
        NewDialog.setWindowTitle(QCoreApplication.translate("NewDialog", u"Add New Variable", None))
        self.label2.setText(QCoreApplication.translate("NewDialog", u"Value(s)", None))
        self.label1.setText(QCoreApplication.translate("NewDialog", u"Variable", None))
#if QT_CONFIG(tooltip)
        self.new_values_entry.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_browse_dir.setText(QCoreApplication.translate("NewDialog", u"Browse folder", None))
        self.btn_browse_file.setText(QCoreApplication.translate("NewDialog", u"Browse file", None))
        self.btn_add.setText(QCoreApplication.translate("NewDialog", u"Add", None))
        self.btn_cancel.setText(QCoreApplication.translate("NewDialog", u"Cancel", None))
    # retranslateUi

