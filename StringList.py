import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        fruit = ["Apple","Banana","Guave","Grape","Papaya","Mango"]
        self.qListWidget = QListWidget()
        self.qListWidget.addItems(fruit)

        button1 = QPushButton("Add")
        button2 = QPushButton("Remove")
        button3 = QPushButton("Edit")
        button4 = QPushButton("Up")
        button5 = QPushButton("Down")
        button6 = QPushButton("Sort")
        button7 = QPushButton("Close")
        

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)
        buttonLayout.addWidget(button5)
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
        


    def Add(self):

        self.text,ok = QInputDialog.getText(self,'Input Dialog','Enter Value')

        if ok:
                  print self.text  
                  self.qListWidget.addItem(self.text)


    def Remove(self):
        row = self.qListWidget.currentRow()
        self.qListWidget.takeItem(row)
            
    
    def Edit(self):
        
        text_replace,ok = QInputDialog.getText(self,'Input Dialog','Enter Value')
        current_item_row = self.qListWidget.currentRow()
        current_item_text = self.qListWidget.item(current_item_row)
        current_item_text.setText(text_replace)

    def Up(self):

        
        current_item_row = self.qListWidget.currentRow()
        current_item_text = self.qListWidget.currentItem()

        up_item_text = self.qListWidget.item(current_item_row+1)
        up_item_row = current_item_row + 1

        self.qListWidget.insertItem(current_item_row,up_item_text)
        self.qListWidget.insertItem(up_item_row,current_item_text)

    def Sort(self):
        self.qListWidget.sortItems()

        
         


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
            




