import sys
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class SlidingMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("滑动展开页面示例")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.expanded = False
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)

        self.toggle_button = QPushButton("展开/收起")
        self.toggle_button.clicked.connect(self.toggle_expand)

        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        self.central_layout.addWidget(self.toggle_button)

        # Create a content widget for your main content.
        self.content_widget = QWidget()
        self.central_layout.addWidget(self.content_widget)

        # Define the geometry for the expanded and collapsed states.
        self.collapsed_geometry = self.geometry()
        self.expanded_geometry = self.geometry()
        self.expanded_geometry.setHeight(400)  # Customize the expanded height as needed

    def toggle_expand(self):
        if self.expanded:
            self.animation.setStartValue(self.expanded_geometry)
            self.animation.setEndValue(self.collapsed_geometry)
        else:
            self.animation.setStartValue(self.collapsed_geometry)
            self.animation.setEndValue(self.expanded_geometry)

        self.animation.start()
        self.expanded = not self.expanded


def main():
    app = QApplication(sys.argv)
    main_window = SlidingMainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
