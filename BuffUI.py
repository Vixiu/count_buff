import random
from sys import argv

from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLineEdit, QInputDialog, QListWidgetItem

from UI import Ui_widget
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton
from PyQt5.QtCore import Qt, QCoreApplication, QRegExp
from PyQt5 import QtGui


class BuffUI(Ui_widget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.input_data = {
            "ty_intellect": self.ty_zhili,
            "in_intellect": self.jt_zhili,
            "buff_amount": self.buff_liang,
            "out_intellect": self.zj_zhili,
            "out_lv": self.zj_lv,
            "add": self.add,
            "in_lv": self.jt_lv,
            "ty_lv": self.ty_lv,
            "ty3_lv": self.ty3_lv,
            "halo_amount": self.buff_gh,
            "pet_amount": self.buff_cw,
            "jade_amount": self.buff_bxy,
            "fixed_attack": self.sg_guding,
            "fixed_intellect": self.lz_guding,
            "percentage_attack": self.sg_bfb,
            "percentage_intellect": self.lz_bfb,
            "ty_fixed": self.ty_lz,
            "ty_percentage": self.ty_bfb,
            "out_medal": self.zj_xz,
            "out_earp": self.zj_eh,
            "out_passive": self.zj_bd,
            "out_guild": self.zj_gh,
            "nai_ba_guardian": self.naiba_sh,
            "nai_ba_ssp": self.naiba_ej,
            "cp_arm": self.cp_arm,
            "ty3_true": self.radioButton,
            "c_attack": self.c_sg,
            "c_intellect": self.c_lz
        }
        self.__init()

        """
        scrollArea_widget = QWidget()
        scrollArea_widget.setStyleSheet("border-bottom: 1px solid #dadce0")
        h_layout = QHBoxLayout()
        scrollArea_widget.setLayout(h_layout)
        UI.scrollArea.setWidget(scrollArea_widget)
        UI.scrollArea.setStyleSheet("QScrollBar:vertical { height: 10px; }")
        """
        #########################
        """
               self.cp_arm = None
        self.fixed_attack = None
        self.jade_amount = None
        self.fixed_intellect = None
        self.percentage_attack = None
        self.percentage_intellect = None
        self.ty_fixed = None
        self.ty_percentage = None
        self.out_medal = None
        self.out_earp = None
        self.out_passive = None
        self.out_guild = None
        self.nai_ba_guardian = None
        self.nai_ba_ssp = None
        self.pet_amount = None
        self.halo_amount = None
        self.ty3_lv = None
        self.ty_lv = None
        self.in_lv = None
        self.add = None
        self.out_lv = None
        self.out_intellect = None
        self.buff_amount = None
        self.ty_intellect = None
        self.in_intellect = None
        """

    def add_config(self, config_id):
        message, ok = QInputDialog.getText(self, "", "请输入配置名")
        if ok:
            item = QListWidgetItem(message)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter)
            item.setData(1, config_id)
            self.config_list.addItem(item)

    def del_config(self, item):
        self.config_list.removeItemWidget(item)

    def get_value(self, name):
        if name not in self.input_data:
            raise print(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            val = self.input_data[name].text()
            if val == '':
                val = self.input_data[name].placeholderText()
            return [float(i) for i in val.split(",") if i] if val else []
        elif name in ("pet_amount", "halo_amount", "jade_amount"):
            val = self.input_data[name].text()
            if val == '':
                val = self.input_data[name].placeholderText()
            return float(val) if val else 0.0
        elif name == "cp_arm":
            return self.input_data[name].isChecked()
        elif name == "ty3_true":
            return self.input_data[name].isChecked()
        else:
            val = self.input_data[name].text()
            if val == '':
                val = self.input_data[name].placeholderText()
            return int(float(val)) if val else 0

    def get_values(self) -> dict:
        return {name: self.get_value(name) for name in self.input_data}

    def set_value(self, name, value):
        if name not in self.input_data:
            raise print(f"{name} is not in UI")
        try:
            if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
                self.input_data[name].setText(",".join([str(i) for i in value]))
            elif name == "cp_arm":
                self.input_data[name].setChecked(value)
            elif name == 'ty3_true':
                if value:
                    self.radioButton.clicked()
                else:
                    self.radioButton_2.clicked()
            else:
                self.input_data[name].setText(str(value))
        except Exception as e:
            print(e, name, value)

    def set_values(self, values: dict):
        for name, value in values.items():
            self.set_value(name, value)

    def set_placeholder_text(self, name, text):
        if name not in self.input_data:
            raise print(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            self.input_data[name].setPlaceholderText(",".join([str(i) for i in text]))
            self.input_data[name].setText('')
        elif name in ("cp_arm", "ty3_true"):
            return
        else:
            self.input_data[name].setPlaceholderText(str(text))
            self.input_data[name].setText('')

    def set_placeholder_texts(self, values: dict):
        for name, value in values.items():
            self.set_placeholder_text(name, value)

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        """鼠标弹起事件"""
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.move(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

    def clear_left_button_style(self):
        self.nailuo_button.setStyleSheet('')
        self.naiba_button.setStyleSheet('')
        self.naima_button.setStyleSheet('')
        self.naigong_button.setStyleSheet('')

    def clear_input_text(self):
        pass

    def clear_show_text(self):
        self.buff_sg.setText('')
        self.buff_lz.setText('')
        self.b1_lz.setText('')
        self.b1_sg.setText('')
        self.b2_lz.setText('')
        self.b2_sg.setText('')
        self.b3_sg.setText('')
        self.b3_lz.setText('')
        self.yijue_lz.setText('')
        self.sanjue_lz_1.setText('')

        self.add.setText('')

    def clear_show_hold_text(self):
        self.buff_sg_cj.setText('')
        self.buff_lz_cj.setText('')
        self.b1_lz_cj.setText('')
        self.b1_sg_cj.setText('')
        self.b2_lz_cj.setText('')
        self.b2_sg_cj.setText('')
        self.b3_sg_cj.setText('')
        self.b3_lz_cj.setText('')
        self.yijue_cj.setText('')
        self.sanjue_lz_1_cj.setText('')

    def clear_all_text(self):
        self.clear_show_hold_text()
        self.clear_show_text()
        self.clear_input_text()

    def __init(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)  # 默认置顶
        self.setWindowTitle(' 奶量计算器')
        self.setStyleSheet("color: rgb(0, 0, 0);\n")
        # 无边框标题设置
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 默认按钮绑定事件
        self.button_close.clicked.connect(lambda: QCoreApplication.instance().quit())  # 关闭
        self.button_top.clicked.connect(self._window_top)  # 置顶
        self.button_min.clicked.connect(lambda: self.showMinimized())  # 最小化
        self.config_list.itemClicked.connect(lambda s: print(s.data(1)))
        self.config_list.itemChanged.connect(lambda s: print(s.text()))
        self.button_add.clicked.connect(self.add_config)
        self.naima_button.clicked.connect(self.__naima_setting)
        self.naiba_button.clicked.connect(self.__naiba_setting)
        self.nailuo_button.clicked.connect(self.__nailuo_setting)
        self.naigong_button.clicked.connect(self.__naigong_setting)
        # 绑定
        self.zj_lv.textEdited.connect(self.__lv_to)
        self.zj_xz.textEdited.connect(self.__intellect_to)
        self.zj_zhili.textEdited.connect(self.__intellect_to)
        self.zj_gh.textEdited.connect(self.__intellect_to)
        self.zj_eh.textEdited.connect(self.__intellect_to)
        self.zj_bd.textEdited.connect(self.__intellect_to)

        self.__set_validator()

        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(10)  # 范围
        effect.setOffset(0, 0)  # 横纵,偏移量
        effect.setColor(Qt.black)  # 颜色
        self.setGraphicsEffect(effect)

    def __intellect_to(self):
        intellect = 0
        for le in ('out_medal', 'out_earp', 'out_passive', 'out_guild', 'out_intellect'):
            text = self.get_value(le)
            intellect += int(text)
        self.jt_zhili.setText(str(intellect))
        self.ty_zhili.setText(str(intellect))

    def __lv_to(self):
        lv_text = self.zj_lv.text()
        if lv_text:
            value = int(lv_text) + 14
            if value <= 40:
                self.jt_lv.setText(str(value))

    def __naima_setting(self):
        self.clear_all_text()
        self.clear_left_button_style()
        self.tabWidget.removeTab(2)
        self.setWindowIcon(QIcon(":/png/84.PNG"))
        self.label_6.setText('智力加减:')
        self.label_3.setText('智力:')
        self.label_17.setText('智力:')
        self.label_15.setText('智力:')
        self.naima_button.setStyleSheet('border:0px; border-radius: 0px;'
                                        ' padding-top:8px;'
                                        'padding-bottom:8px;'
                                        'border-left: 5px solid rgb(5, 229, 254);'
                                        'background-color:rgb(217, 217, 217);')
        self.yijue.setText('圣光天启')
        self.sanjue.setText('祈愿·天使赞歌')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/23.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/350.PNG"))
        self.buff_name.setText('勇气祝福')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/84.PNG"))
        self.buff_gain.setText('勇气+颂歌')

    def __nailuo_setting(self):
        self.clear_all_text()
        self.clear_left_button_style()
        self.tabWidget.removeTab(2)
        self.setWindowIcon(QIcon(":/png/719.PNG"))
        self.label_6.setText('智力加减:')
        self.label_3.setText('智力:')
        self.label_17.setText('智力:')
        self.label_15.setText('智力:')
        self.yijue.setText('开幕！人偶剧场')
        self.sanjue.setText('终幕！人偶剧场')
        self.nailuo_button.setStyleSheet('border:0px; border-radius: 0px;'
                                         ' padding-top:8px;'
                                         'padding-bottom:8px;'
                                         'border-left: 5px solid rgb(5, 229, 254);'
                                         'background-color:rgb(217, 217, 217);')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/757.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/838.PNG"))
        self.buff_name.setText('禁忌诅咒')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/719.PNG"))
        self.buff_gain.setText('禁忌诅咒+疯狂召唤')

    def __naiba_setting(self):
        self.clear_all_text()
        self.clear_left_button_style()
        self.tabWidget.insertTab(2, self.tab3, '奶爸二觉')
        self.setWindowIcon(QIcon(":/png/111.PNG"))
        self.label_6.setText('体精加减:')
        self.label_3.setText('体精:')
        self.label_17.setText('体精:')
        self.label_15.setText('体精:')
        self.naiba_button.setStyleSheet('border:0px; border-radius: 0px;'
                                        ' padding-top:8px;'
                                        'padding-bottom:8px;'
                                        'border-left: 5px solid rgb(5, 229, 254);'
                                        'background-color:rgb(217, 217, 217);')
        self.yijue.setText('天启之珠')
        self.sanjue.setText('生命礼赞:神威')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/158.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/548.PNG"))
        self.buff_name.setText('荣誉祝福')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/111.PNG"))

        self.buff_gain.setText('守护+荣誉祝福(24层)')

    def __naigong_setting(self):
        self.clear_all_text()
        self.clear_left_button_style()
        self.tabWidget.removeTab(2)
        self.setWindowIcon(QIcon(":/png/14.PNG"))
        self.label_6.setText('精神加减:')
        self.label_3.setText('精神:')
        self.label_17.setText('精神:')
        self.label_15.setText('精神:')
        self.naigong_button.setStyleSheet('border:0px; border-radius: 0px;'
                                          ' padding-top:8px;'
                                          'padding-bottom:8px;'
                                          'border-left: 5px solid rgb(5, 229, 254);'
                                          'background-color:rgb(217, 217, 217);')
        self.yijue.setText('梦想的舞台')
        self.sanjue.setText('终曲:霓虹蝶梦')
        self.yijue_icon.setPixmap(QtGui.QPixmap(":/png/88.PNG"))
        self.sanjue_icon.setPixmap(QtGui.QPixmap(":/png/34.PNG"))
        self.buff_name.setText('可爱节拍')
        self.buff_icon.setPixmap(QtGui.QPixmap(":/png/14.PNG"))

        self.buff_gain.setText('可爱节拍+燃情狂想曲')

    def __set_validator(self):
        def float_validator(input_box: QLineEdit):
            text = input_box.text().replace('。', '.').replace(' ', '')
            try:
                float(text)
                input_box.setText(text)
            except ValueError:
                input_box.setText(text[:-1])

        def percent_sign_validator(input_box: QLineEdit):
            text = input_box.text().replace('。', '.').replace(' ', '').replace('，', ',').replace(',,', ',')
            for _ in text.split(','):
                try:
                    if _:
                        float(_)
                except ValueError:
                    input_box.setText(text[:-1])
                    return
            input_box.setText(text)

        def lv_validator(input_box: QLineEdit):
            text = input_box.text().replace(' ', '')
            try:
                num = int(text)
                if num <= 40:
                    input_box.setText(text)
                else:
                    input_box.setText('40')
                if num == 0:
                    input_box.setText('1')
            except ValueError:
                input_box.setText(text[:-1])

        # 整数类型
        self.zj_zhili.setValidator(QtGui.QIntValidator())

        self.zj_xz.setValidator(QtGui.QIntValidator())
        self.zj_bd.setValidator(QtGui.QIntValidator())
        self.zj_eh.setValidator(QtGui.QIntValidator())
        self.zj_gh.setValidator(QtGui.QIntValidator())
        self.naiba_ej.setValidator(QtGui.QIntValidator())
        self.naiba_sh.setValidator(QtGui.QIntValidator())

        self.jt_zhili.setValidator(QtGui.QIntValidator())

        self.ty_zhili.setValidator(QtGui.QIntValidator())
        self.ty3_lv.setValidator(QtGui.QIntValidator())
        self.sg_guding.setValidator(QtGui.QIntValidator())
        self.lz_guding.setValidator(QtGui.QIntValidator())
        self.ty_lz.setValidator(QtGui.QIntValidator())
        self.c_sg.setValidator(QtGui.QIntValidator())
        self.c_lz.setValidator(QtGui.QIntValidator())
        # 浮点数
        self.buff_gh.textEdited.connect(lambda: float_validator(self.buff_gh))
        self.buff_cw.textEdited.connect(lambda: float_validator(self.buff_cw))
        self.buff_bxy.textEdited.connect(lambda: float_validator(self.buff_bxy))
        # 等级
        self.jt_lv.textEdited.connect(lambda: lv_validator(self.jt_lv))
        self.ty_lv.textEdited.connect(lambda: lv_validator(self.ty_lv))
        self.zj_lv.textEdited.connect(lambda: lv_validator(self.zj_lv))
        # 百分比
        self.lz_bfb.textEdited.connect(lambda: percent_sign_validator(self.lz_bfb))
        self.sg_bfb.textEdited.connect(lambda: percent_sign_validator(self.sg_bfb))
        self.ty_bfb.textEdited.connect(lambda: percent_sign_validator(self.ty_bfb))
        # buff量与智力增加

    def _window_top(self):
        if not bool(self.windowHandle().flags() & Qt.WindowStaysOnTopHint):
            self.windowHandle().setFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
            self.button_top.setStyleSheet("background:rgb(212, 218, 230);")
        else:
            self.windowHandle().setFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.button_top.setStyleSheet("")
            print('F')
        self.repaint()


app = QApplication(argv)
ui = BuffUI()

print(ui.get_values())
ui.show()
app.exec_()
