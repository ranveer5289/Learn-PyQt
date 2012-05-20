import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NumberFormatDlg(QDialog):

    def __init__(self,parent=None):
        super(NumberFormatDlg,self).__init__(parent)
        self.format = dict(thousandsseperator=",",decimalmarker=".",decimalplaces=2,rednegatives=False)

        thousandsLabel = QLabel("&Thousands Seperator")
        self.thousandsEdit = QLineEdit(self.format["thousandsseperator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        
        decimalMarkerLabel = QLabel("Decimal &Marker")
        self.decimalMarkerEdit = QLineEdit(self.format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)

        decimalPlacesLabel = QLabel("&Decimal Places")
        self.decimalPlacesSpinBox  = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)

        self.decimalPlacesSpinBox.setRange(0,6)
        self.decimalPlacesSpinBox.setValue(self.format["decimalplaces"])

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(self.format["rednegatives"])

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)


        grid = QGridLayout()
        grid.addWidget(thousandsLabel,0,0)
        grid.addWidget(self.thousandsEdit,0,1)
        grid.addWidget(decimalMarkerLabel,1,0)
        grid.addWidget(self.decimalMarkerEdit,1,1)
        grid.addWidget(decimalPlacesLabel,2,0)
        grid.addWidget(self.decimalPlacesSpinBox,2,1)
        grid.addWidget(self.redNegativesCheckBox,3,0,1,2)
        grid.addWidget(buttonBox,4,0,1,2)
        self.setLayout(grid)

        self.connect(buttonBox,SIGNAL("accepted()"),self,SLOT("accept()"))
        self.connect(buttonBox,SIGNAL("rejected()"),self,SLOT("reject()"))
        
        self.setWindowTitle("Set Number Format (Modal)")




    def numberFormat(self):
        return self.format


    def setNumberFormat1(self):
        #dialog = numberformatdlg1.NumberFormatDlg(self.format,self)
        dialog = NumberFormatDlg()
        if dialog.exec_():
            self.format = dialog.numberFormat()
            self.refreshTable()


    def refreshTable(self):
        print "refereshed"




app = QApplication(sys.argv)
numberfmtdlg = NumberFormatDlg()
numberfmtdlg.show()
numberfmtdlg.setNumberFormat1()
