import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout



class IntegerValidatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('限制输入大于0的整数示例')

        layout = QVBoxLayout()

        label = QLabel("输入大于0的整数:")
        self.lineEdit = QLineEdit()

        # 创建一个整数验证器
        validator = QIntValidator(1, 2147483647)  # 1 是下限，2147483647 是 int 的最大值
        self.lineEdit.setValidator(validator)

        layout.addWidget(label)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IntegerValidatorApp()
    sys.exit(app.exec_())
