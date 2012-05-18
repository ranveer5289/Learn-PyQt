import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

        def __init__(self, parent=None):
                super(Form, self).__init__(parent)

                self.dial = QDial()
                self.dial.setNotchesVisible(True)
                
                self.spinbox = QSpinBox()
                
                layout = QHBoxLayout()
                layout.addWidget(self.dial)
                layout.addWidget(self.spinbox)
                self.setLayout(layout)


                self.connect(self.dial, SIGNAL("valueChanged(int)"),self.spinbox.setValue)
                self.connect(self.dial, SIGNAL("valueChanged(int)"),self.getValue_dial)
                self.connect(self.spinbox, SIGNAL("valueChanged(int)"),self.dial.setValue)
                self.connect(self.spinbox, SIGNAL("valueChanged(int)"),self.getValue_spinbox)

                self.setWindowTitle("Signals and Slots")


        def getValue_dial(self):
                 print self.dial.value()

        def getValue_spinbox(self):
                 print self.dial.value()


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
