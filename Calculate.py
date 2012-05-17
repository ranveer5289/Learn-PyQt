import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
        def __init__(self,parent=None):
                super(Form,self).__init__(parent)
                self.browser = QTextBrowser()
                self.linedit = QLineEdit("type an expression and press enter")
                self.linedit.selectAll()

                #Line up widget vertically.
                layout = QVBoxLayout()

                layout.addWidget(self.browser)
                layout.addWidget(self.linedit)

                #Inherited from QWidget.
                self.setLayout(layout)

                self.linedit.setFocus()
                self.connect(self.linedit,SIGNAL("returnPressed()"),self.updateUi)
                self.setWindowTitle("Calculate")

        def updateUi(self):
                try:
                        text = unicode(self.linedit.text())
                        self.browser.append("{0} = <b>{1}</b>".format(text,eval(text)))
                except:
                        self.browser.append("<font color=red>{0} is invalid!</font>".format(text))




app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
