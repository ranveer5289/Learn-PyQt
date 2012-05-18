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


                #Here changed "value" is passed as a parameter with valueChanged SIGNAL.
                self.connect(self.dial, SIGNAL("valueChanged(int)"),self.dial_value_changed)
                self.connect(self.spinbox, SIGNAL("valueChanged(int)"),self.spinbox_value_changed)

                self.setWindowTitle("Signals and Slots")


        #Accessing value passed as a parameter and printing it.

        def dial_value_changed(self, value):
                print "value={0}".format(value)
                self.spinbox.setValue(value)
        
        def spinbox_value_changed(self, value):
                print "value={0}".format(value)
                self.dial.setValue(value)



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

