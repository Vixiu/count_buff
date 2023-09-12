import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class SlidingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 200, 100)
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: lightblue;")

        self.expanded = False
        self.animation_duration = 300

        self.button = QPushButton("Toggle")
        self.button.clicked.connect(self.toggle_animation)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def toggle_animation(self):
        if not self.expanded:
            self.expand()
        else:
            self.collapse()

    def expand(self):
        self.expanded = True
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(QRect(0, 0, 200, 50))
        self.anim.setEndValue(QRect(0, 0, 200, 200))
        self.anim.start()

    def collapse(self):
        self.expanded = False
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(QRect(0, 0, 200, 200))
        self.anim.setEndValue(QRect(0, 0, 200, 50))
        self.anim.start()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Sliding Widget Example")

        self.sliding_widget = SlidingWidget()
        self.setCentralWidget(self.sliding_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
