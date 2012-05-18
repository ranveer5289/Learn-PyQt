import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

        def __init__(self, parent=None):
                super(Form,self).__init__(parent)

                button1 = QPushButton("One")
                button2 = QPushButton("Two")
                button3 = QPushButton("Three")

                self.label = QLabel()
                layout = QHBoxLayout()

                layout.addWidget(button1)
                layout.addWidget(button2)
                layout.addWidget(button3)
                layout.addWidget(self.label)

                self.setLayout(layout)

                self.connect(button1,SIGNAL("clicked()"),self.one)
                self.connect(button2,SIGNAL("clicked()"),self.clicked)
                self.connect(button3,SIGNAL("clicked()"),self.clicked)
                self.setWindowTitle("Connections")

        def one(self):
                self.label.setText("You clicked button 'One'")
                
        def clicked(self):
                button = self.sender()

                if button is None or not isinstance(button,QPushButton):
                        return
                self.label.setText("You clicked button {0}".format(button.text()))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()









