# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptimineExport(object):
    def setupUi(self, OptimineExport):
        OptimineExport.setObjectName("OptimineExport")
        OptimineExport.resize(1286, 1329)
        self.buttonBox = QtWidgets.QDialogButtonBox(OptimineExport)
        self.buttonBox.setGeometry(QtCore.QRect(770, 1180, 471, 121))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.fullScaleLabel = QtWidgets.QLabel(OptimineExport)
        self.fullScaleLabel.setGeometry(QtCore.QRect(20, 1050, 198, 54))
        self.fullScaleLabel.setObjectName("fullScaleLabel")
        self.fullScaleSpinBox = QtWidgets.QDoubleSpinBox(OptimineExport)
        self.fullScaleSpinBox.setGeometry(QtCore.QRect(260, 1050, 281, 50))
        self.fullScaleSpinBox.setToolTip("")
        self.fullScaleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fullScaleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fullScaleSpinBox.setDecimals(3)
        self.fullScaleSpinBox.setSingleStep(0.01)
        self.fullScaleSpinBox.setProperty("value", 10.013)
        self.fullScaleSpinBox.setObjectName("fullScaleSpinBox")
        self.zeroBalanceSpinBox = QtWidgets.QDoubleSpinBox(OptimineExport)
        self.zeroBalanceSpinBox.setGeometry(QtCore.QRect(260, 1130, 281, 50))
        self.zeroBalanceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.zeroBalanceSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.zeroBalanceSpinBox.setDecimals(3)
        self.zeroBalanceSpinBox.setMinimum(-99.0)
        self.zeroBalanceSpinBox.setSingleStep(0.01)
        self.zeroBalanceSpinBox.setProperty("value", 0.013)
        self.zeroBalanceSpinBox.setObjectName("zeroBalanceSpinBox")
        self.layoutWidget = QtWidgets.QWidget(OptimineExport)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 1021, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pressureFileLabel = QtWidgets.QLabel(self.layoutWidget)
        self.pressureFileLabel.setObjectName("pressureFileLabel")
        self.gridLayout.addWidget(self.pressureFileLabel, 0, 0, 1, 1)
        self.pressureFileButton = QtWidgets.QToolButton(self.layoutWidget)
        self.pressureFileButton.setObjectName("pressureFileButton")
        self.gridLayout.addWidget(self.pressureFileButton, 0, 3, 1, 1)
        self.acousticsFileLabel = QtWidgets.QLabel(self.layoutWidget)
        self.acousticsFileLabel.setEnabled(False)
        self.acousticsFileLabel.setObjectName("acousticsFileLabel")
        self.gridLayout.addWidget(self.acousticsFileLabel, 1, 0, 1, 1)
        self.acousticsFileButton = QtWidgets.QToolButton(self.layoutWidget)
        self.acousticsFileButton.setEnabled(False)
        self.acousticsFileButton.setObjectName("acousticsFileButton")
        self.gridLayout.addWidget(self.acousticsFileButton, 1, 3, 1, 1)
        self.pressureLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pressureLineEdit.setObjectName("pressureLineEdit")
        self.gridLayout.addWidget(self.pressureLineEdit, 0, 1, 1, 2)
        self.acousticsLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.acousticsLineEdit.setEnabled(False)
        self.acousticsLineEdit.setObjectName("acousticsLineEdit")
        self.gridLayout.addWidget(self.acousticsLineEdit, 1, 1, 1, 2)
        self.zeroBalanceLabel = QtWidgets.QLabel(OptimineExport)
        self.zeroBalanceLabel.setGeometry(QtCore.QRect(20, 1130, 198, 52))
        self.zeroBalanceLabel.setObjectName("zeroBalanceLabel")
        self.scaleBalanceHelp = QtWidgets.QLabel(OptimineExport)
        self.scaleBalanceHelp.setGeometry(QtCore.QRect(640, 980, 528, 267))
        self.scaleBalanceHelp.setObjectName("scaleBalanceHelp")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(OptimineExport)
        self.dateTimeEdit.setGeometry(QtCore.QRect(400, 520, 351, 50))
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(OptimineExport)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(400, 580, 341, 50))
        self.dateTimeEdit_2.setReadOnly(True)
        self.dateTimeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit_2.setCalendarPopup(False)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.startTimeLabel = QtWidgets.QLabel(OptimineExport)
        self.startTimeLabel.setGeometry(QtCore.QRect(40, 530, 129, 38))
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.endTimeLabel = QtWidgets.QLabel(OptimineExport)
        self.endTimeLabel.setGeometry(QtCore.QRect(40, 600, 129, 38))
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.pressureUnitLabel = QtWidgets.QLabel(OptimineExport)
        self.pressureUnitLabel.setGeometry(QtCore.QRect(40, 750, 221, 38))
        self.pressureUnitLabel.setObjectName("pressureUnitLabel")
        self.pressureUnit = QtWidgets.QLabel(OptimineExport)
        self.pressureUnit.setGeometry(QtCore.QRect(400, 750, 129, 38))
        self.pressureUnit.setObjectName("pressureUnit")
        self.durationLabel = QtWidgets.QLabel(OptimineExport)
        self.durationLabel.setGeometry(QtCore.QRect(40, 660, 129, 38))
        self.durationLabel.setObjectName("durationLabel")
        self.duration = QtWidgets.QLabel(OptimineExport)
        self.duration.setGeometry(QtCore.QRect(400, 660, 129, 38))
        self.duration.setObjectName("duration")
        self.fullScaleLabel.setBuddy(self.fullScaleSpinBox)
        self.pressureFileLabel.setBuddy(self.pressureLineEdit)
        self.acousticsFileLabel.setBuddy(self.acousticsLineEdit)
        self.zeroBalanceLabel.setBuddy(self.zeroBalanceSpinBox)
        self.startTimeLabel.setBuddy(self.dateTimeEdit)
        self.endTimeLabel.setBuddy(self.dateTimeEdit_2)
        self.durationLabel.setBuddy(self.dateTimeEdit_2)

        self.retranslateUi(OptimineExport)
        self.buttonBox.accepted.connect(OptimineExport.accept)
        self.buttonBox.rejected.connect(OptimineExport.reject)
        QtCore.QMetaObject.connectSlotsByName(OptimineExport)

    def retranslateUi(self, OptimineExport):
        _translate = QtCore.QCoreApplication.translate
        OptimineExport.setWindowTitle(_translate("OptimineExport", "Optimine DAT Exporter"))
        self.fullScaleLabel.setText(_translate("OptimineExport", "&Full Scale:"))
        self.pressureFileLabel.setText(_translate("OptimineExport", "&Pressure Data:"))
        self.pressureFileButton.setText(_translate("OptimineExport", "..."))
        self.acousticsFileLabel.setText(_translate("OptimineExport", "&Acoustics Data:"))
        self.acousticsFileButton.setText(_translate("OptimineExport", "..."))
        self.zeroBalanceLabel.setText(_translate("OptimineExport", "&Zero Balance:"))
        self.scaleBalanceHelp.setText(_translate("OptimineExport", "Use same values here that you will when\n"
"importing with the \"Acoustic Reader\"\n"
"LabVIEW program"))
        self.dateTimeEdit.setDisplayFormat(_translate("OptimineExport", "M/d/yyyy hh:mm AP"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("OptimineExport", "M/d/yyyy hh:mm AP"))
        self.startTimeLabel.setText(_translate("OptimineExport", "&Start Time:"))
        self.endTimeLabel.setText(_translate("OptimineExport", "&End Time:"))
        self.pressureUnitLabel.setText(_translate("OptimineExport", "Pressure Unit:"))
        self.pressureUnit.setText(_translate("OptimineExport", "mpa"))
        self.durationLabel.setText(_translate("OptimineExport", "Duration: "))
        self.duration.setText(_translate("OptimineExport", "Duration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptimineExport = QtWidgets.QDialog()
    ui = Ui_OptimineExport()
    ui.setupUi(OptimineExport)
    OptimineExport.show()
    sys.exit(app.exec_())

