# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BucketingHelp(object):
    def setupUi(self, BucketingHelp):
        BucketingHelp.setObjectName("BucketingHelp")
        BucketingHelp.resize(1124, 940)
        self.verticalLayout = QtWidgets.QVBoxLayout(BucketingHelp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(BucketingHelp)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(BucketingHelp)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_druggability = QtWidgets.QWidget()
        self.tab_druggability.setObjectName("tab_druggability")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_druggability)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolBox_druggability = QtWidgets.QToolBox(self.tab_druggability)
        self.toolBox_druggability.setObjectName("toolBox_druggability")
        self.page_druggability_criteria = QtWidgets.QWidget()
        self.page_druggability_criteria.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_druggability_criteria.setObjectName("page_druggability_criteria")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_druggability_criteria)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_druggability_image_criteria = QtWidgets.QLabel(self.page_druggability_criteria)
        self.label_druggability_image_criteria.setText("")
        self.label_druggability_image_criteria.setScaledContents(False)
        self.label_druggability_image_criteria.setObjectName("label_druggability_image_criteria")
        self.verticalLayout_6.addWidget(self.label_druggability_image_criteria)
        self.toolBox_druggability.addItem(self.page_druggability_criteria, "")
        self.page_druggability_tree = QtWidgets.QWidget()
        self.page_druggability_tree.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_druggability_tree.setObjectName("page_druggability_tree")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_druggability_tree)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_druggability_image_tree = QtWidgets.QLabel(self.page_druggability_tree)
        self.label_druggability_image_tree.setText("")
        self.label_druggability_image_tree.setScaledContents(False)
        self.label_druggability_image_tree.setObjectName("label_druggability_image_tree")
        self.verticalLayout_8.addWidget(self.label_druggability_image_tree)
        self.toolBox_druggability.addItem(self.page_druggability_tree, "")
        self.verticalLayout_2.addWidget(self.toolBox_druggability)
        self.tabWidget.addTab(self.tab_druggability, "")
        self.tab_safety = QtWidgets.QWidget()
        self.tab_safety.setObjectName("tab_safety")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_safety)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox_safety = QtWidgets.QToolBox(self.tab_safety)
        self.toolBox_safety.setObjectName("toolBox_safety")
        self.page_safety_criteria = QtWidgets.QWidget()
        self.page_safety_criteria.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_safety_criteria.setObjectName("page_safety_criteria")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_safety_criteria)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_safety_image_criteria = QtWidgets.QLabel(self.page_safety_criteria)
        self.label_safety_image_criteria.setText("")
        self.label_safety_image_criteria.setScaledContents(False)
        self.label_safety_image_criteria.setObjectName("label_safety_image_criteria")
        self.verticalLayout_7.addWidget(self.label_safety_image_criteria)
        self.toolBox_safety.addItem(self.page_safety_criteria, "")
        self.page_safety_tree = QtWidgets.QWidget()
        self.page_safety_tree.setGeometry(QtCore.QRect(0, 0, 1094, 597))
        self.page_safety_tree.setObjectName("page_safety_tree")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_safety_tree)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_safety_image_tree = QtWidgets.QLabel(self.page_safety_tree)
        self.label_safety_image_tree.setText("")
        self.label_safety_image_tree.setScaledContents(False)
        self.label_safety_image_tree.setObjectName("label_safety_image_tree")
        self.verticalLayout_9.addWidget(self.label_safety_image_tree)
        self.toolBox_safety.addItem(self.page_safety_tree, "")
        self.verticalLayout_3.addWidget(self.toolBox_safety)
        self.tabWidget.addTab(self.tab_safety, "")
        self.tab_feasibility = QtWidgets.QWidget()
        self.tab_feasibility.setObjectName("tab_feasibility")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_feasibility)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox_feasibility = QtWidgets.QToolBox(self.tab_feasibility)
        self.toolBox_feasibility.setObjectName("toolBox_feasibility")
        self.page_feasibility_criteria = QtWidgets.QWidget()
        self.page_feasibility_criteria.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_feasibility_criteria.setObjectName("page_feasibility_criteria")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_feasibility_criteria)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_feasibility_image_criteria = QtWidgets.QLabel(self.page_feasibility_criteria)
        self.label_feasibility_image_criteria.setText("")
        self.label_feasibility_image_criteria.setScaledContents(False)
        self.label_feasibility_image_criteria.setObjectName("label_feasibility_image_criteria")
        self.verticalLayout_10.addWidget(self.label_feasibility_image_criteria)
        self.toolBox_feasibility.addItem(self.page_feasibility_criteria, "")
        self.page_feasibility_tree = QtWidgets.QWidget()
        self.page_feasibility_tree.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_feasibility_tree.setObjectName("page_feasibility_tree")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_feasibility_tree)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_feasibility_image_tree = QtWidgets.QLabel(self.page_feasibility_tree)
        self.label_feasibility_image_tree.setText("")
        self.label_feasibility_image_tree.setScaledContents(False)
        self.label_feasibility_image_tree.setObjectName("label_feasibility_image_tree")
        self.verticalLayout_11.addWidget(self.label_feasibility_image_tree)
        self.toolBox_feasibility.addItem(self.page_feasibility_tree, "")
        self.verticalLayout_4.addWidget(self.toolBox_feasibility)
        self.tabWidget.addTab(self.tab_feasibility, "")
        self.tab_antibodyability = QtWidgets.QWidget()
        self.tab_antibodyability.setObjectName("tab_antibodyability")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_antibodyability)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolBox_antibodyability = QtWidgets.QToolBox(self.tab_antibodyability)
        self.toolBox_antibodyability.setObjectName("toolBox_antibodyability")
        self.page_antibodyability_criteria = QtWidgets.QWidget()
        self.page_antibodyability_criteria.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_antibodyability_criteria.setObjectName("page_antibodyability_criteria")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_antibodyability_criteria)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_antibodyability_image_criteria = QtWidgets.QLabel(self.page_antibodyability_criteria)
        self.label_antibodyability_image_criteria.setText("")
        self.label_antibodyability_image_criteria.setScaledContents(False)
        self.label_antibodyability_image_criteria.setObjectName("label_antibodyability_image_criteria")
        self.verticalLayout_12.addWidget(self.label_antibodyability_image_criteria)
        self.toolBox_antibodyability.addItem(self.page_antibodyability_criteria, "")
        self.page_antibodyability_tree = QtWidgets.QWidget()
        self.page_antibodyability_tree.setGeometry(QtCore.QRect(0, 0, 1094, 597))
        self.page_antibodyability_tree.setObjectName("page_antibodyability_tree")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_antibodyability_tree)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_antibodyability_image_tree = QtWidgets.QLabel(self.page_antibodyability_tree)
        self.label_antibodyability_image_tree.setText("")
        self.label_antibodyability_image_tree.setScaledContents(False)
        self.label_antibodyability_image_tree.setObjectName("label_antibodyability_image_tree")
        self.verticalLayout_13.addWidget(self.label_antibodyability_image_tree)
        self.toolBox_antibodyability.addItem(self.page_antibodyability_tree, "")
        self.verticalLayout_5.addWidget(self.toolBox_antibodyability)
        self.tabWidget.addTab(self.tab_antibodyability, "")
        self.tab_modality = QtWidgets.QWidget()
        self.tab_modality.setObjectName("tab_modality")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_modality)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.toolBox_modality = QtWidgets.QToolBox(self.tab_modality)
        self.toolBox_modality.setObjectName("toolBox_modality")
        self.page_modality_criteria = QtWidgets.QWidget()
        self.page_modality_criteria.setGeometry(QtCore.QRect(0, 0, 1082, 776))
        self.page_modality_criteria.setObjectName("page_modality_criteria")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_modality_criteria)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_modality_image_criteria = QtWidgets.QLabel(self.page_modality_criteria)
        self.label_modality_image_criteria.setText("")
        self.label_modality_image_criteria.setScaledContents(False)
        self.label_modality_image_criteria.setObjectName("label_modality_image_criteria")
        self.verticalLayout_14.addWidget(self.label_modality_image_criteria)
        self.toolBox_modality.addItem(self.page_modality_criteria, "")
        self.page_modality_tree = QtWidgets.QWidget()
        self.page_modality_tree.setGeometry(QtCore.QRect(0, 0, 1094, 597))
        self.page_modality_tree.setObjectName("page_modality_tree")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_modality_tree)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_modality_image_tree = QtWidgets.QLabel(self.page_modality_tree)
        self.label_modality_image_tree.setText("")
        self.label_modality_image_tree.setScaledContents(False)
        self.label_modality_image_tree.setObjectName("label_modality_image_tree")
        self.verticalLayout_15.addWidget(self.label_modality_image_tree)
        self.toolBox_modality.addItem(self.page_modality_tree, "")
        self.verticalLayout_16.addWidget(self.toolBox_modality)
        self.tabWidget.addTab(self.tab_modality, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(BucketingHelp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BucketingHelp)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox_druggability.setCurrentIndex(0)
        self.toolBox_safety.setCurrentIndex(0)
        self.toolBox_feasibility.setCurrentIndex(0)
        self.toolBox_antibodyability.setCurrentIndex(0)
        self.toolBox_modality.setCurrentIndex(0)
        self.buttonBox.accepted.connect(BucketingHelp.accept)
        self.buttonBox.rejected.connect(BucketingHelp.reject)
        QtCore.QMetaObject.connectSlotsByName(BucketingHelp)

    def retranslateUi(self, BucketingHelp):
        _translate = QtCore.QCoreApplication.translate
        BucketingHelp.setWindowTitle(_translate("BucketingHelp", "Help - target scoring"))
        self.label.setText(_translate("BucketingHelp", "See scoring procedure based on..."))
        self.toolBox_druggability.setItemText(self.toolBox_druggability.indexOf(self.page_druggability_criteria), _translate("BucketingHelp", "Criteria"))
        self.toolBox_druggability.setItemText(self.toolBox_druggability.indexOf(self.page_druggability_tree), _translate("BucketingHelp", "Decision process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_druggability), _translate("BucketingHelp", "SM Druggability"))
        self.toolBox_safety.setItemText(self.toolBox_safety.indexOf(self.page_safety_criteria), _translate("BucketingHelp", "Criteria"))
        self.toolBox_safety.setItemText(self.toolBox_safety.indexOf(self.page_safety_tree), _translate("BucketingHelp", "Decision process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_safety), _translate("BucketingHelp", "Safety"))
        self.toolBox_feasibility.setItemText(self.toolBox_feasibility.indexOf(self.page_feasibility_criteria), _translate("BucketingHelp", "Criteria"))
        self.toolBox_feasibility.setItemText(self.toolBox_feasibility.indexOf(self.page_feasibility_tree), _translate("BucketingHelp", "Decision process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feasibility), _translate("BucketingHelp", "Feasibility"))
        self.toolBox_antibodyability.setItemText(self.toolBox_antibodyability.indexOf(self.page_antibodyability_criteria), _translate("BucketingHelp", "Criteria"))
        self.toolBox_antibodyability.setItemText(self.toolBox_antibodyability.indexOf(self.page_antibodyability_tree), _translate("BucketingHelp", "Decision process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_antibodyability), _translate("BucketingHelp", "AB-ability"))
        self.toolBox_modality.setItemText(self.toolBox_modality.indexOf(self.page_modality_criteria), _translate("BucketingHelp", "Criteria"))
        self.toolBox_modality.setItemText(self.toolBox_modality.indexOf(self.page_modality_tree), _translate("BucketingHelp", "Decision process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_modality), _translate("BucketingHelp", "Modality"))

