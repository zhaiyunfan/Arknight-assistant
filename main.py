import sys
from functools import partial

from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

import Window

# def cal():

def init(ui):
    ui.spinBoxHead.maximum = ui.spinBoxMax.value()
    input = ui.spinBoxHead.value()
    timeLeft = (ui.spinBoxMax.value() - input) * 6
    hourLeft = timeLeft // 60
    minuiteLeft = timeLeft - 60 * hourLeft

    ui.lcdNumberHour.display(hourLeft)
    ui.lcdNumberMin.display(minuiteLeft)

    # timer.start(60000)
    # time = QTime.currentTime()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.spinBoxHead.maximum = ui.spinBoxMax.value()
    
    #timer = QTimer()
    #timer.timeout.connect(cal)
    
    ui.pushButton.clicked.connect(partial(init, ui))
    # ui.actionExit.triggered.connect(partial(clickExit, app))
    sys.exit(app.exec_())