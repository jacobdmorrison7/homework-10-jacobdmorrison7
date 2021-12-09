
import sys
import time
import RPi.GPIO as GPIO

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt 

GPIO.setmode(GPIO.BCM)

pin = 18
GPIO.setup(pin, GPIO.OUT)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
    
        self.setFixedHeight(400)
        self.setFixedWidth(400)

        info = QLabel("Press the button to light the LED\nThe text will change when the circuit is connected")
        # insert indicator and text
        self.button = QPushButton("Light LED")
        self.indicator = QLabel('Not Connected')

        
        bottom = QHBoxLayout()
        bottom.addWidget(self.button)
        bottom.addWidget(self.indicator)

        final = QVBoxLayout()
        final.addWidget(info)
        final.addLayout(bottom)

        central = QWidget()
        central.setLayout(final)
        self.setCentralWidget(central)
        self.button.clicked.connect(self.light_LED)
        self.i = True
        
	# couldn't include because can't set an event and read
	# a pin that is set as a pin to write to 
        #  GPIO.add_event_detect(pin, GPIO.RISING)
        #  GPIO.add_event_callback(pin, self.my_callback)

        
    def my_callback(self, channel):
        self.indicator.setText('Is Connected')
    
    def light_LED(self):
       #  if self.i == True:
        GPIO.output(pin,not GPIO.INPUT(pin))
       #     self.i = False
       # else:
       #     GPIO.output(pin, GPIO.LOW)
       #     self.i == True

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

