# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(501, 392)
        SettingsDialog.setMinimumSize(QtCore.QSize(501, 392))
        SettingsDialog.setMaximumSize(QtCore.QSize(501, 392))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 117))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 117))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_OpenTargets_appName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_OpenTargets_appName.setText("")
        self.lineEdit_OpenTargets_appName.setObjectName("lineEdit_OpenTargets_appName")
        self.verticalLayout_2.addWidget(self.lineEdit_OpenTargets_appName)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_OpenTargets_secret = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_OpenTargets_secret.setText("")
        self.lineEdit_OpenTargets_secret.setObjectName("lineEdit_OpenTargets_secret")
        self.verticalLayout_2.addWidget(self.lineEdit_OpenTargets_secret)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 71))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 71))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_FDA_key = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_FDA_key.setObjectName("lineEdit_FDA_key")
        self.verticalLayout.addWidget(self.lineEdit_FDA_key)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 72))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lineEdit_biogrid_key = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_biogrid_key.setObjectName("lineEdit_biogrid_key")
        self.verticalLayout_4.addWidget(self.lineEdit_biogrid_key)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 59))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_seq_similarity = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_seq_similarity.setMinimumSize(QtCore.QSize(41, 20))
        self.lineEdit_seq_similarity.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEdit_seq_similarity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_seq_similarity.setObjectName("lineEdit_seq_similarity")
        self.horizontalLayout.addWidget(self.lineEdit_seq_similarity)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setMinimumSize(QtCore.QSize(21, 16))
        self.label_4.setMaximumSize(QtCore.QSize(21, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(483, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "OpenTargets"))
        self.label_2.setText(_translate("SettingsDialog", "App name (http://blog.opentargets.org/api-getting-started-1/)"))
        self.label_3.setText(_translate("SettingsDialog", "Secret"))
        self.groupBox.setTitle(_translate("SettingsDialog", "FDA"))
        self.label.setText(_translate("SettingsDialog", "API key (https://open.fda.gov/api/reference/)"))
        self.groupBox_4.setTitle(_translate("SettingsDialog", "BioGRID"))
        self.label_6.setText(_translate("SettingsDialog", "API key (https://wiki.thebiogrid.org/doku.php/biogridrest)"))
        self.groupBox_3.setTitle(_translate("SettingsDialog", "Sequence similarity threshold"))
        self.label_4.setText(_translate("SettingsDialog", "%"))
        self.label_5.setText(_translate("SettingsDialog", "When looking for similar targets with indications of druggability, search genes with at least this much protein sequence identity"))

