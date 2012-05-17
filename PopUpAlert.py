#To access command line arguments.
import sys

#Sleep function required.
import time

#Needed for GUI and QTime class.
from PyQt4.QtCore import *
from PyQt4.QtGui import *


#Every PyQt app must have a QApplication object.
app = QApplication(sys.argv)

try:
        #Get current system time.
        due = QTime.currentTime()
        message = "Alert"

        if len(sys.argv) < 2:
                raise ValueError

        hours,minutes = sys.argv[1].split(':')

        due = QTime(int(hours),int(minutes))
        print type(due)
        
        if not due.isValid():
                raise ValueError

        if len(sys.argv)>2:
                message = "".join(sys.argv[2:])
                print message

        while QTime.currentTime() < due:
                #Suspend execution or processing for 20 seconds.
                time.sleep(20)

        label = QLabel("<font color=red size=72><b>" + message + "</b></font>")

        #We don't require a title bar so windowflag set to splashscreen.
        label.setWindowFlags(Qt.SplashScreen)

#Shows widget and its child widgets. It is equivalent to java's setVisible(true).At this point, the label window is not shown!The call to show() merely schedules a paint event, that is, it adds a new event to the QApplication objects event queue thats a request to paint the specified widget 

        label.show()

        #Time-out set for 1 sec and after time-out call quit method. These type of methods are called SLOT.
        QTimer.singleShot(1000,app.quit)


        # Start QApplication objects event loop. The first event it gets is
        # paint event and than a timer time-out event i,e, exactly after 1 sec.
        app.exec_()


except ValueError:
        print "Valid format 'python PopUpAlert.py hh:mm message' in #24 clock format required."


