from sys import argv

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

from UI import Ui_widget
from UIData import UIData
from Widget import RoundedWindow

UI = Ui_widget()
data = UIData()
app = QApplication(argv)
main_window = RoundedWindow()
main_window.setStyleSheet("color: rgb(0, 0, 0);\n")
main_window.setWindowTitle(' 奶量计算器')
UI.setupUi(main_window)
main_window.show()
data.bind_input(UI)
UI.button_close.clicked.connect(lambda: QCoreApplication.instance().quit())
UI.button_count.clicked.connect(lambda: print(data.get_value("ty_lv")))
app.exec_()
