from PyQt5.QtGui import QIntValidator, QValidator, QDoubleValidator, QBrush, QColor, QFont, QPixmap

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLineEdit, QListWidgetItem, QMessageBox, \
    QAbstractItemView, QHeaderView, QTableWidgetItem, QLabel

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication, QSize
from PyQt5 import QtGui


from QtUI.uic5 import Ui_widget
from Config import CLASS
from PyQt5.QtWidgets import QLineEdit,QCheckBox,QRadioButton
class LValidator(QValidator):
    def __init__(self,min_,max_):
        super().__init__()
        self.min,self.max=min_,max_
    def validate(self, text:str, pos):
        if text =='':
            return QValidator.Acceptable, '1', pos
        elif text.isdigit() and self.min <=int(text) <=  self.max:
            return QValidator.Acceptable, text, pos
        elif (text[0] == '+' or text[0] == '-') and (text[1:].isdigit() or not text[1:]):
            return QValidator.Acceptable, text, pos
        return QValidator.Invalid, text, pos

class PValidator(QValidator):
    def validate(self, text: str, pos):
        text = text.replace('。', '.').replace(' ', '').replace('，', ',').replace(',,', ',')
        try:
            _ = [float(item) for item in text.split(',') if item]
        except ValueError:
            return QValidator.Invalid, text, pos

        return QValidator.Acceptable, text, pos

class CpArms:
    def __init__(self,check_box:QCheckBox):
        self._check_box=check_box
    @property
    def textEdited(self):
        return self

    def connect(self,callback:callable):
        self._check_box.clicked.connect(lambda:callback(self._check_box.isChecked()))

    def setText(self,bl:str):
        if bl:
            self._check_box.setChecked(bl=='True')

    def setPlaceholderText(self,bl):
        self.setText(bl)

class Percentage:
    def __init__(self, linedit: QLineEdit):
        self._linedit = linedit

    @property
    def textEdited(self):
        return self
    def _to_list(self):
        val = self._linedit.text()
        if val != '':
            return [float(i) for i in val.split(",") if i] if val else []
        return val
    def connect(self,callback):
        self._linedit.textEdited.connect(lambda :callback(self._to_list()))

    def setText(self, ls:str):
        self._linedit.setText(ls[1: -1].replace(" ", ""))

    def setPlaceholderText(self, ls):
        self._linedit.setPlaceholderText(ls[1: -1].replace(" ", ""))

class TY3:
    def __init__(self, rb1:QRadioButton,rb2: QRadioButton):
        self.rb1,self.rb2=rb1,rb2

    @property
    def textEdited(self):
        return self

    def connect(self,callback):
        self.rb1.clicked.connect(lambda :callback(self.rb1.isChecked()))
        self.rb2.clicked.connect(lambda :callback(self.rb1.isChecked()))

    def setText(self, bl):
        if bl:
            if bl=='True':
                self.rb1.setChecked(True)
            else:
                self.rb1.setChecked(False)

    def setPlaceholderText(self, bl):
        self.setText(bl)




class RoundedWindow(QWidget):
    def __init__(self):
        super(RoundedWindow, self).__init__()
      #  self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

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
        try:
            if event.buttons() == Qt.LeftButton and self.mPos:
                self.move(self.mapToGlobal(event.pos() - self.mPos))
            event.accept()
        except AttributeError as e:
            print(e)
    def window_top(self, flag):
        if flag:
            self.windowHandle().setFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        else:
            self.windowHandle().setFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.repaint()



class BuffUI(Ui_widget):
        def __init__(self,widget):
            self.setupUi(widget)
            self.job_button = {
                'ma': self.ma_button,
                'ba': self.ba_button,
                'luo': self.luo_button,
                'gong': self.gong_button
            }
            self._skill_list = [
                [self.lv1_name, self.lv1_value],
                [self.lv2_name, self.lv2_value],
                [self.lv3_name, self.lv3_value],
                [self.lv4_name, self.lv4_value],
                [self.lv5_name, self.lv5_value],
                [self.lv6_name, self.lv6_value],
                [self.lv7_name, self.lv7_value],
            ]
            self.input_map={
                'cp_arms': CpArms(self.cp_arm),
                "c_attack": self.c_attack,
                "c_intellect": self.c_intellect,
                'buff_amount': {
                    'in_map':self.buff_amount_in_map,
                    'out_map':self.buff_amount_out_map,
                    'enh':self.buff_amount_enh
                },
                'bxy':{
                    'enh':self.bxy_ehn,
                    'fixed_attack': self.bxy_fixed_attack,
                    'fixed_intellect': self.bxy_fixed_intellect,
                    'fixed_ty': self.bxy_fixed_ty,
                    'percentage_attack': Percentage(self.bxy_percentage_attack),
                    'percentage_intellect': Percentage(self.bxy_percentage_intellect),
                    'percentage_ty': Percentage(self.bxy_percentage_ty),
                },
                'buff':{
                    'intellect_out': self.buff_intellect_out,
                    'lv_out': self.buff_lv_out,
                    'intellect_in': self.buff_intellect_in,
                    'lv_in': self.buff_lv_in,
                },
                'ty':{
                    'ty1_lv': self.ty_lv,
                    'intellect': self.ty_intellect,
                    'ty3_lv': self.ty3_lv,
                    "is_ty1": TY3(self.rb1,self.rb2),
                },
                'skill':{i:item[1] for i,item in enumerate(self._skill_list)}
            }
            # 设置输入校验
            self._validator()
            # 设置阴影
           # self._effect()
            # 设置表格样式
            self._table()

            #-

          #  self.widget_3.setGraphicsEffect(effect)
        def _add_row(self, name, icon=None):
            index = self.tableWidget.rowCount()
            self.tableWidget.insertRow(index)
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                item.setFont(QFont("Arial", 12))
                if col %2==0:
                    item.setTextAlignment(Qt.AlignRight| Qt.AlignVCenter)
                elif col==1:
                    item.setFont(QFont("Arial", 12))
                self.tableWidget.setItem(index, col, item)
            if icon is not None:
                label=QLabel()
                pixmap = QPixmap(f":/png/{icon}")

                label.setPixmap(pixmap)
                label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                label.setContentsMargins(10, 0, 0, 0)
                self.tableWidget.setCellWidget(index,0,label)
                #self.tableWidget.item(index,0).setIcon(QIcon(f":/png/{icon}"))


            self.tableWidget.item(index, 1).setText(name)

        def clear_quick_calc_text(self):
            self.add_1.setText('')
            self.add_2.setText('')
            self.add_3.setText('')
            self.input_offset.setText('')

        def setting(self, job):
            data=CLASS[job]
            self.tabWidget.setTabVisible(1, True)
            self.clear_quick_calc_text()
            self.attribute_1.setText(data['attribute'])
            self.attribute_2.setText(data['attribute'])
            self.attribute_3.setText(data['attribute'])
            self.attribute_4.setText(data['attribute'] + '加减')
            # -
            self.tableWidget.setRowCount(0)
            self._add_row(data['buff']['name'] + '(站街)', data['buff']['icon'])
            self._add_row(data['buff']['name'] + '(进图)', data['buff']['icon'])
            for item in data['skill_form']:
                self._add_row(item['name'], item['icon'])
            self._add_row(data['ty1']['name'], data['ty1']['icon'])
            self._add_row(data['ty3']['name'], data['ty3']['icon'])
            for item in data['total_buff']:
                self._add_row(item['name'], item['icon'])
            #-
            self._clear_left_button_style()
            self.job_button[job].setStyleSheet('border:0px; border-radius: 0px;'
                                                'padding-top:8px;'
                                                'padding-bottom:8px;'
                                                'border-left: 5px solid rgb(5, 229, 254);'
                                                )
            # 技能输入框
            for l1,l2 in self._skill_list:
                l1.hide()
                l2.hide()

            for i, item in enumerate(data['passive_skill']):
                self._skill_list[i][0].setText(f"Lv{item['lv']} {item['name']}:")
                self._skill_list[i][0].show()
                self._skill_list[i][1].show()

        def _set_diff(self,row,col,value):
            item= self.tableWidget.item(row, col)
            if value == '-':
               item.setText('')
            elif value > 0:
                item.setText(f'+{value}')
                item.setForeground(QBrush(QColor("green")))

            elif value < 0:
                item.setText(str(value))
                item.setForeground(QBrush(QColor("red")))
            else:
              item.setText('')


        def _clear_left_button_style(self):
            self.luo_button.setStyleSheet('')
            self.ba_button.setStyleSheet('')
            self.ma_button.setStyleSheet('')
            self.gong_button.setStyleSheet('')

        def set_input_text(self,data:dict,input_map=None):
            if input_map is None:
                input_map = self.input_map
            for k1, v1 in data.items():
                if isinstance(v1, dict):
                    self.set_input_text(v1, input_map[k1])
                else:
                    input_map[k1].setText(str(v1))


        def set_placeholder_text(self,data:dict,input_map=None):
            if input_map is None:
                input_map=self.input_map
            for k1, v1 in data.items():
                if isinstance(v1, dict):
                    self.set_placeholder_text(v1,input_map[k1])
                else:
                    input_map[k1].setText('')
                    input_map[k1].setPlaceholderText(str(v1))

        def set_show_text(self,result):
            for i, (res, diff) in enumerate(zip(result['result'], result['diff'])):
                self.tableWidget.item(i, 2).setText(str(res['attack']))
                self.tableWidget.item(i, 4).setText(str(res['intellect']))
                self.tableWidget.item(i, 6).setText(str(res['multiplier']))
                self._set_diff(i, 3, diff['attack'])
                self._set_diff(i, 5, diff['intellect'])
                self._set_diff(i, 7, diff['multiplier'])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            total_width = sum(self.tableWidget.columnWidth(i) for i in range(self.tableWidget.columnCount()))

            if total_width <=self.tableWidget.width():
                self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
                self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        def set_config(self,names:list[str]):
            self.config_combobox.clear()
            for n in names:
                self.config_combobox.addItem(n)
        def _table(self):
          #  self.tableWidget.setIconSize(QSize(24, 24))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)  # 禁止选中
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 禁止拖动表头
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        def _create_effect(self):
            effect = QGraphicsDropShadowEffect()
            effect.setBlurRadius(15)  # 范围
            effect.setOffset(1, 1)  # 横纵,偏移量
            effect.setColor(QColor("#c3c5c9"))  # 颜色
            return effect
        def _effect(self):
            self.widget_5.setGraphicsEffect(self._create_effect())
            self.widget_3.setGraphicsEffect(self._create_effect())
            self.tableWidget.setGraphicsEffect(self._create_effect())
        def _validator(self):
            self.buff_amount_out_map.setValidator(QIntValidator())
            self.buff_amount_enh.setValidator(QDoubleValidator())
            self.buff_intellect_out.setValidator(QIntValidator())
            self.buff_lv_out.setValidator(QIntValidator())
            self.buff_intellect_in.setValidator(QIntValidator())
            self.buff_lv_in.setValidator(QIntValidator())
            self.ty_lv.setValidator(QIntValidator())
            self.ty_intellect.setValidator(QIntValidator())
            self.ty3_lv.setValidator(QIntValidator())
            self.buff_amount_in_map.setValidator(QIntValidator())
            self.add_1.setValidator(QIntValidator())
            self.add_2.setValidator(QIntValidator())
            self.add_3.setValidator(QIntValidator())
            self.input_offset.setValidator(QIntValidator())
            # -
            self.bxy_fixed_attack.setValidator(QIntValidator())
            self.bxy_fixed_intellect.setValidator(QIntValidator())
            self.bxy_fixed_ty.setValidator(QIntValidator())
            self.bxy_percentage_intellect.setValidator(QIntValidator())
            self.bxy_percentage_attack.setValidator(PValidator())
            self.bxy_percentage_ty.setValidator(QIntValidator())
            self.bxy_ehn.setValidator(QDoubleValidator())
            # -
            self.lv1_value.setValidator(QIntValidator())
            self.lv2_value.setValidator(QIntValidator())
            self.lv3_value.setValidator(QIntValidator())
            self.lv4_value.setValidator(QIntValidator())
            self.lv5_value.setValidator(QIntValidator())
            self.lv6_value.setValidator(QIntValidator())
            self.lv7_value.setValidator(QIntValidator())
            # -
            self.c_attack.setValidator(QIntValidator())
            self.c_intellect.setValidator(QIntValidator())
