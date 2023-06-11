from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout


class ShakeInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def shake(self):
        # 创建动画
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(100)

        # 设置动画路径
        pos1 = QPoint(self.pos().x() - 5, self.pos().y())
        pos2 = QPoint(self.pos().x() + 5, self.pos().y())
        animation.setKeyValueAt(0.1, pos1)
        animation.setKeyValueAt(0.2, pos2)
        animation.setKeyValueAt(0.3, pos1)
        animation.setKeyValueAt(0.4, pos2)
        animation.setKeyValueAt(0.5, pos1)
        animation.setKeyValueAt(0.6, pos2)
        animation.setKeyValueAt(0.7, pos1)
        animation.setKeyValueAt(0.8, pos2)
        animation.setKeyValueAt(0.9, pos1)
        animation.setEndValue(self.pos())

        # 开始动画
        animation.start(animation.DeleteWhenStopped)


if __name__ == '__main__':
    app = QApplication([])

    widget = QWidget()
    input = ShakeInput(widget)
    input.setPlaceholderText("请输入内容")


    # 按钮点击事件
    def on_button_clicked():
            input.shake()


    button = QPushButton("提交", widget)
    button.clicked.connect(on_button_clicked)

    # 设置布局
    layout = QVBoxLayout(widget)
    layout.addWidget(input)
    layout.addWidget(button)
    widget.show()

    app.exec_()
