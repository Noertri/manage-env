# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog_form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        if not EditDialog.objectName():
            EditDialog.setObjectName(u"EditDialog")
        EditDialog.resize(650, 500)
        EditDialog.setMinimumSize(QSize(650, 500))
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
        EditDialog.setPalette(palette)
        EditDialog.setAutoFillBackground(True)
        self.verticalLayout_2 = QVBoxLayout(EditDialog)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.label = QLabel(EditDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.var_entry = QLineEdit(EditDialog)
        self.var_entry.setObjectName(u"var_entry")
        self.var_entry.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.var_entry)

        self.label_2 = QLabel(EditDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.values_list = QListWidget(EditDialog)
        self.values_list.setObjectName(u"values_list")
        self.values_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.values_list.setProperty(u"showDropIndicator", False)
        self.values_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.values_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.values_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.values_list.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.values_list.setSpacing(1)
        self.values_list.setViewMode(QListView.ViewMode.ListMode)
        self.values_list.setUniformItemSizes(True)
        self.values_list.setWordWrap(False)
        self.values_list.setSelectionRectVisible(True)
        self.values_list.setItemAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.values_list)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_new2 = QPushButton(EditDialog)
        self.btn_new2.setObjectName(u"btn_new2")

        self.verticalLayout.addWidget(self.btn_new2)

        self.btn_edit2 = QPushButton(EditDialog)
        self.btn_edit2.setObjectName(u"btn_edit2")

        self.verticalLayout.addWidget(self.btn_edit2)

        self.btn_delete2 = QPushButton(EditDialog)
        self.btn_delete2.setObjectName(u"btn_delete2")

        self.verticalLayout.addWidget(self.btn_delete2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_browse_dir2 = QPushButton(EditDialog)
        self.btn_browse_dir2.setObjectName(u"btn_browse_dir2")
        self.btn_browse_dir2.setMinimumSize(QSize(110, 0))

        self.verticalLayout.addWidget(self.btn_browse_dir2)

        self.btn_browse_file2 = QPushButton(EditDialog)
        self.btn_browse_file2.setObjectName(u"btn_browse_file2")

        self.verticalLayout.addWidget(self.btn_browse_file2)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_ok2 = QPushButton(EditDialog)
        self.btn_ok2.setObjectName(u"btn_ok2")

        self.verticalLayout.addWidget(self.btn_ok2)

        self.btn_cancel2 = QPushButton(EditDialog)
        self.btn_cancel2.setObjectName(u"btn_cancel2")

        self.verticalLayout.addWidget(self.btn_cancel2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditDialog)

        QMetaObject.connectSlotsByName(EditDialog)
    # setupUi

    def retranslateUi(self, EditDialog):
        EditDialog.setWindowTitle(QCoreApplication.translate("EditDialog", u"Edit Variable", None))
        self.label.setText(QCoreApplication.translate("EditDialog", u"Variable:", None))
        self.label_2.setText(QCoreApplication.translate("EditDialog", u"Value(s):", None))
        self.btn_new2.setText(QCoreApplication.translate("EditDialog", u"New", None))
        self.btn_edit2.setText(QCoreApplication.translate("EditDialog", u"Edit", None))
        self.btn_delete2.setText(QCoreApplication.translate("EditDialog", u"Delete", None))
        self.btn_browse_dir2.setText(QCoreApplication.translate("EditDialog", u"Browse folder", None))
        self.btn_browse_file2.setText(QCoreApplication.translate("EditDialog", u"Browse file", None))
        self.btn_ok2.setText(QCoreApplication.translate("EditDialog", u"OK", None))
        self.btn_cancel2.setText(QCoreApplication.translate("EditDialog", u"Cancel", None))
    # retranslateUi
