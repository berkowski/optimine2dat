from optimine2dat import Optimine

from PyQt5 import (QtCore, QtWidgets, uic)

import os
import traceback


TXT_TEMPLATE = \
"""
WHOI P-Test {test_name}
Operator Name: {operator_name}

Client Name: {client_name}
Client Group: {client_group}
Item P/N(s): {part_number}
Item S/N(s): {serial_number}

Description:
{description}
"""

class ExportDialog(QtWidgets.QDialog):
    """

    """

    def __init__(self, parent=None):
        """

        :param parent:
        """

        QtWidgets.QDialog.__init__(self, parent=parent)
        uic.loadUi(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'export.ui'), self)

        self.__data = None

        # Button Connections
        self.importButton.clicked.connect(
            lambda: self.load_data(self.pressureFileLineEdit.text(), self.acousticsFileLineEdit.text()))

        self.pressureFileButton.clicked.connect(self.load_pressure_json_dialog)
        self.acousticsFileButton.clicked.connect(self.load_acoustics_data_dialog)

        self.closeButton.clicked.connect(self.reject)
        self.exportButton.clicked.connect(self.export_clicked)


    @QtCore.pyqtSlot()
    def load_pressure_json_dialog(self):
        """
        Open a file explorer dialog to select a pressure json file.
        :return:
        """

        # We dont' care about the returned active filter
        json_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, caption="Optimine JSON File", filter="JSON *.json (*.json);; Any *.* (*.*)")

        if len(json_file) == 0:
            return

        # Now set the text edit box
        self.pressureFileLineEdit.setText(json_file)

    @QtCore.pyqtSlot()
    def load_acoustics_data_dialog(self):
        """
        Open a file explorer dialog to select an acoustics data file
        :return:
        """

        # We dont' care about the returned active filter
        acoustics_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, caption="Acoustics Data File", filter="Any *.* (*.*)")

        if len(acoustics_file) == 0:
            return

        # Now set the text edit box
        self.acousticsFileLineEdit.setText(acoustics_file)

    @QtCore.pyqtSlot(str, str)
    def load_data(self, pressure_json, acoustics_data):
        """

        :param pressure_json:
        :param acoustics_data:
        :return:
        """

        opt = Optimine()
        try:
            opt.read_json(pressure_json)
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Error reading pressure JSON file",
                "Error reading file: %s\n\n%s" % (pressure_json, traceback.format_exc())
            )
            return False

        # Add acoustics read hook here
        # try:
        #     opt.read_json(pressure_json)
        # except Exception as e:
        #     QtWidgets.QMessageBox.critical(
        #         self,
        #         "Error reading pressure JSON file",
        #         "Error reading file: %s\n\n%s" % (pressure_json, traceback.format_exc())
        #     )
        #     return False

        self.updateDialog(opt)
        self.__data = opt

        return True

    def updateDialog(self, data):
        """

        :return:
        """

        self.testReportLineEdit.setText(data.test_report)
        self.operatorLineEdit.setText(data.operator)
        self.pressureVesselLineEdit.setText(data.pressure_vessel)
        self.pressureTransducerLineEdit.setText(data.pressure_transducer_serial_number)
        self.startTimeEdit.setDateTime(data.start_time)
        self.endTimeEdit.setDateTime(data.end_time)
        self.duration.setText(str(data.end_time - data.start_time))
        self.pressureUnit.setText(data.pressure_unit)
        self.scaleFactorSpinBox.setValue(data.pressure_scale_factor)
        self.partNumberLineEdit.setText(data.test_part_number)
        self.serialNumberLineEdit.setText(data.test_serial_number)

        if data.pressure_unit.lower().strip() not in ['mpa', 'msw', 'psi', 'bar']:
            QtWidgets.QMessageBox.warning(
                self,
                "Unknown Pressure Unit",
                "Unknown pressure unit '%s'.  Please enter the required scale factor to convert to PSI." % (data.pressure_unit,)
            )

    def write_txt(self, filename):
        """

        :param filename:
        :return:
        """

        text = TXT_TEMPLATE.format(
            test_name=self.reportGroup.findChild(QtWidgets.QLineEdit, 'testReportLineEdit').text(),
            operator_name=self.reportGroup.findChild(QtWidgets.QLineEdit, 'operatorLineEdit').text(),
            client_name=self.testGroup.findChild(QtWidgets.QLineEdit, 'clientNameLineEdit').text(),
            client_group=self.testGroup.findChild(QtWidgets.QLineEdit, 'clientGroupLineEdit').text(),
            part_number=self.testGroup.findChild(QtWidgets.QLineEdit, 'partNumberLineEdit').text(),
            serial_number=self.testGroup.findChild(QtWidgets.QLineEdit, 'serialNumberLineEdit').text(),
            description=self.testGroup.findChild(QtWidgets.QPlainTextEdit, 'descriptionTextEdit').toPlainText()
        )

        if filename is None:
            return text

        with open(filename, 'w') as fid:
            fid.write(text)

    @QtCore.pyqtSlot()
    def export_clicked(self):
        """

        :return:
        """

        if self.__data is None:
            QtWidgets.QMessageBox.critical(self, "Error Exporting Data", "Need to import data first.")
            return

        # Don't care about the filter
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save File",
            "Pressure_Test_%s_%s.dat" % (self.testReportLineEdit.text(), self.startTimeEdit.dateTime().toString("yyyy-MM-dd_HH-mm"))
        )

        if len(filename) == 0:
            return


        # Update scale factors
        self.__data.pressure_full_scale = self.fullScaleSpinBox.value()
        self.__data.pressure_zero_bias = self.zeroBalanceSpinBox.value()

        # Write data file
        self.__data.to_dat(filename)

        txt_filename = os.path.splitext(filename)[0] + ".txt"
        self.write_txt(txt_filename)

        QtWidgets.QMessageBox.information(
            self,
            "Export Complete",
            "Created files:\n  %s\n  %s\nIn directory:\n  %s" % (
                os.path.basename(filename),
                os.path.basename(txt_filename),
                os.path.dirname(filename))
        )


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = ExportDialog(None)
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

