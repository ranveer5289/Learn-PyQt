import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TaxRate(QObject):


       def __init__(self):
                super(TaxRate,self).__init__()
                self.__rate = 17.5


       def rate(self):
               return self.__rate

       def setRate(self,rate):
               if rate != self.__rate:
                       self.__rate = rate
                       #Signal without paranthesis(no args) is called Short-circuit signal.
                       self.emit(SIGNAL("rateChanged"), self.__rate)



def rateChanged(value):
                print "value changed {0}".format(value)

app = QApplication(sys.argv)
vat = TaxRate()
vat.connect(vat,SIGNAL("rateChanged"),rateChanged)
vat.setRate(17.5)
vat.setRate(7.5)
vat.setRate(117.5)
app.exec_()
