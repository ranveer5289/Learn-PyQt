import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

    def __init__(self,fruit,parent=None):
        super(Form,self).__init__(parent)
        self.qListWidget = QListWidget()
        self.qListWidget.addItems(fruit)

        button1 = QPushButton("Add")
        button2 = QPushButton("Remove")
        button3 = QPushButton("Edit")
        button4 = QPushButton("Up")
        button6 = QPushButton("Sort")
        button7 = QPushButton("Close")
        

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)
        buttonLayout.addWidget(button6)
        buttonLayout.addWidget(button7)


        layout = QHBoxLayout()
        layout.addWidget(self.qListWidget)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.setWindowTitle("QListWidget")

        self.connect(button1,SIGNAL("clicked()"),self.Add)
        self.connect(button2,SIGNAL("clicked()"),self.Remove)
        self.connect(button3,SIGNAL("clicked()"),self.Edit)
        self.connect(button4,SIGNAL("clicked()"),self.Up)
        self.connect(button6,SIGNAL("clicked()"),self.Sort)
        self.connect(button7,SIGNAL("clicked()"),self.accept)
        


    def Add(self):

        self.text,ok = QInputDialog.getText(self,'Input Dialog','Enter Value')

        if ok:
                  print self.text  
                  self.qListWidget.addItem(self.text)


    def Remove(self):
        row = self.qListWidget.currentRow()
        item = self.qListWidget.takeItem(row)
        del item
            
    
    def Edit(self):
        
        text_replace,ok = QInputDialog.getText(self,'Input Dialog','Enter Value')
        current_item_row = self.qListWidget.currentRow()
        current_item_text = self.qListWidget.item(current_item_row)
        current_item_text.setText(text_replace)




    def Up(self):
       
        current_item_row = self.qListWidget.currentRow()
        if current_item_row > 0:
            current_item_text = self.qListWidget.item(current_item_row)
            print str(current_item_text.text())

            up_item_row = current_item_row - 1
            up_item_text = self.qListWidget.item(up_item_row)
            print str(up_item_text.text())

            self.qListWidget.takeItem(current_item_row)
            self.qListWidget.insertItem(current_item_row,up_item_text.text())
            self.qListWidget.takeItem(up_item_row)
            self.qListWidget.insertItem(up_item_row,current_item_text.text())
        else:
              print "Already at top of list."

    def Sort(self):
        self.qListWidget.sortItems()


    def reject(self):
        self.accept()

    def accept(self):
        QDialog.done(self,0)

        
         


app = QApplication(sys.argv)
fruit = ["Apple","Banana","Guave","Grape","Papaya","Mango"]
form = Form(fruit)
form.show()
app.exec_()
