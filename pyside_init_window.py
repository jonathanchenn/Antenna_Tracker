#creating a popup for ground station init using PySide.
#First attempt at making initilization slightly less terrible
#6/6/2019
#Michael Valentino-Manno
#first attempt

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
   
class fun(QWidget):

   def __init__(self, parent = None):
      super(fun, self).__init__(parent)

      #create the necessary buttons prompting the user
      layout = QHBoxLayout()              
      self.button1 = QCheckBox("1. Plug in USBs")
      layout.addWidget(self.button1)
		
      self.button2 = QCheckBox("2. Move antenna to center")     
      layout.addWidget(self.button2)

      self.button3 = QCheckBox("3. Enter IMEI number")     
      layout.addWidget(self.button3)

      self.button4 = QCheckBox("4. Search")     
      layout.addWidget(self.button4)

      self.button5 = QCheckBox("5. Move antenna to center")     
      layout.addWidget(self.button5)

      self.button6 = QCheckBox("6. Update settings")     
      layout.addWidget(self.button6)

      self.button7 = QCheckBox("7. Move IMU")     
      layout.addWidget(self.button7)

      self.button8 = QCheckBox("8. Select iriduim")     
      layout.addWidget(self.button8)

      self.button9 = QCheckBox("9. Start auto-tracking")     
      layout.addWidget(self.button9)

      button = QPushButton("Done Initializing")
      layout.addWidget(button)
      button.clicked.connect(lambda:self.isDone(self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9))
      button.show()
      
      self.setLayout(layout)
      self.setWindowTitle("Ground Station Initialization Steps")

   #when the push button is pressed, checks if each box is checked. If so, close the init window
   def isDone(self,b1,b2,b3,b4,b5,b6,b7,b8,b9):
      if (b1.isChecked() == True and b2.isChecked() == True and b3.isChecked() == True and b4.isChecked() == True and b5.isChecked() == True
      and b6.isChecked() == True and b7.isChecked() == True and b8.isChecked() == True and b9.isChecked() == True):
         self.close()
			

app = QApplication(sys.argv)
ex = fun()
ex.show()
