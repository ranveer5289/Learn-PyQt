import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PenPropertiesDlg(QDialog):

        def __init__(self,parent=None):
                super(PenPropertiesDlg,self).__init__(parent)
                

                widthLabel = QLabel("&Width:")
                self.widthSpinBox = QSpinBox()
                #When users presses Alt+W the keyboard focus will be swicthed to widthSpinBox.
                widthLabel.setBuddy(self.widthSpinBox)
                self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignCenter)
                self.widthSpinBox.setRange(0,24)
                self.beveledCheckBox = QCheckBox("&Beveled edges")
                styleLabel = QLabel("&Style:")
                self.styleComboBox = QComboBox()
                styleLabel.setBuddy(self.styleComboBox)
                self.styleComboBox.addItems(["Solid","Dashed","Dotted","DashDotted","DashDotDotted"])

                okButton = QPushButton("&OK")
                cancelButton = QPushButton("Cancel")

                buttonLayout = QHBoxLayout()
                buttonLayout.addStretch()
                buttonLayout.addWidget(okButton)
                buttonLayout.addWidget(cancelButton)

                layout = QGridLayout()
                layout.addWidget(widthLabel,0,0)
                layout.addWidget(self.widthSpinBox,0,1)
                layout.addWidget(self.beveledCheckBox,0,2)
                layout.addWidget(styleLabel,1,0)
                layout.addWidget(self.styleComboBox,1,1,2,2)
                layout.addLayout(buttonLayout,3,0,1,3)
                self.setLayout(layout)


                self.connect(okButton,SIGNAL("clicked()"),self,SLOT("accept()"))
                self.connect(cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))

                self.setWindowTitle("Pen Properties")


        def setPenProperties(self):
                dialog = PenPropertiesDlg(self)
                self.width = 1
                self.beveled = False
                self.style = "Solid"
                dialog.widthSpinBox.setValue(self.width)
                dialog.beveledCheckBox.setChecked(self.beveled)
                dialog.styleComboBox.setCurrentIndex(dialog.styleComboBox.findText(self.style))

                #When called on dialog it is shown modally.
                if dialog.exec_():
                        self.width = dialog.widthSpinBox.value()
                        self.beveled = dialog.beveledCheckBox.isChecked()
                        self.style = unicode(dialog.styleComboBox.currentText())
                        self.updateData()

        def updateData(self):

                print self.width,self.beveled,self.style

app = QApplication(sys.argv)
PPD = PenPropertiesDlg()
PPD.show()
PPD.setPenProperties()
