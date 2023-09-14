import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class RenameButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('重命名按钮示例')
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('原始名称', self)
        self.button.clicked.connect(self.renameButton)

    def renameButton(self):
        if self.button.text() == '原始名称':
            self.button.setText('新名称')
        else:
            self.button.setText('原始名称')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RenameButtonApp()
    window.show()
    sys.exit(app.exec_())
