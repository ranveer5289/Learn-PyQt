import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

        def __init__(self,parent=None):
                super(Form,self).__init__(parent)

                date = self.getdata()
                rates = sorted(self.rates.keys())

                dataLabel = QLabel(date)
                self.fromComboBox = QComboBox()
                self.fromComboBox.addItems(rates)
                self.fromSpinBox = QDoubleSpinBox()
                self.fromSpinBox.setRange(0.01,10000000.00)
                self.fromSpinBox.setValue(1.00)
                self.toComboBox = QComboBox()
                self.toComboBox.addItems(rates)
                self.toLabel = QLabel("1.00")

                qgrid = QGridLayout()
                qgrid.addWidget(dataLabel,0,0)
                qgrid.addWidget(self.fromComboBox,1,0)
                qgrid.addWidget(self.fromSpinBox,1,1)
                qgrid.addWidget(self.toComboBox,2,0)
                qgrid.addWidget(self.toLabel,2,1)
                self.setLayout(qgrid)


                self.connect(self.fromComboBox,SIGNAL("currentIndexChanged(int)"),self.updateUi)
                self.connect(self.toComboBox,SIGNAL("currentIndexChanged(int)"),self.updateUi)
                self.connect(self.fromSpinBox,SIGNAL("valueChanged(double)"),self.updateUi)
                self.setWindowTitle("Currency")

        def updateUi(self):
        
                to = unicode(self.toComboBox.currentText())
                print to
                from_ = unicode(self.fromComboBox.currentText())
                print from_
        
                amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
                print amount
        
                self.toLabel.setText(str(amount))
        
        def getdata(self): 
                self.rates = {}
                try:
                        date = "Unknown"
                        fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
                        for line in fh:
                                if not line or line.startswith(("#", "Closing ")):
                                        continue
                                fields = line.split(",")
                                if line.startswith("Date "):
                                        date = fields[-1]
                                else:
                                        try:
                                                value = float(fields[-1])
                                                self.rates[unicode(fields[0])] = value
                                        except ValueError:
                                                                pass
                        return "Exchange Rates Date: " + date
                except Exception, e:
                                return "Failed to download:\n%s" % e

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
