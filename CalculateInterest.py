import sys
import math
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

        def __init__(self,parent=None):
                super(Form,self).__init__(parent)

                self.qspinbox_amount = QSpinBox()
                self.qspinbox_rate = QSpinBox()
                self.qcombobox_year = QComboBox()
                self.qspinbox_amount.setMinimum(0.0)
                self.qspinbox_rate.setMinimum(0.0)

                years = ["1","2","3","4","5"]
                self.qcombobox_year.addItems(years)

                self.label = QLabel()
                
                layout = QVBoxLayout()
                layout.addWidget(self.qspinbox_amount)
                layout.addWidget(self.qspinbox_rate)
                layout.addWidget(self.qcombobox_year)
                layout.addWidget(self.label)
                self.setLayout(layout)


                self.connect(self.qspinbox_amount,SIGNAL("valueChanged(int)"),self.calculateInterest)
                self.connect(self.qspinbox_rate,SIGNAL("valueChanged(int)"),self.calculateInterest)
                self.connect(self.qcombobox_year,SIGNAL("currentIndexChanged(int)"),self.calculateInterest)


        def calculateInterest(self):
                amount = self.qspinbox_amount.value()
                rate = self.qspinbox_rate.value()
                year = int(self.qcombobox_year.currentText())

                CI = amount * (1 + rate/100.0) ** year
                self.label.setText("Amount after compund interest is <b>{0}</b>".format(str(CI)))


app = QApplication(sys.argv)
form = Form()
form.show()
form.resize(250,50)
app.exec_()
