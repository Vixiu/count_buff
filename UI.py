from PyQt5.QtGui import QIntValidator, QValidator,QDoubleValidator
from sys import argv

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLineEdit, QListWidgetItem, QMessageBox

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication
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

def text_color(value:int)->str:
    if value>0:
        return f"<font color='#FF8C00'>+{value}<font>"
    elif value<0:
        return f"<font color='#f40c0c'>{value}<font>"
    else:
        return ''
def set_color(dt:dict):
    for key in dt:
        if isinstance(dt[key],dict):
            dt[key]={k:text_color(v) for k ,v in dt[key].items()}
        elif isinstance(dt[key],list):
            dt[key]=[{k:text_color(v) for k,v in item.items()} for item in dt[key]]
        else:
            dt[key]=text_color(dt[key])
    return dt

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
        self._validator()

    def clear_quick_calc_text(self):
        self.add_1.setText('')
        self.add_2.setText('')
        self.add_3.setText('')
        self.input_offset.setText('')

    def setting(self,job):
        data=CLASS[job]
        self.tabWidget.setTabVisible(1, True)
        self.clear_quick_calc_text()
        self.attribute_1.setText(data['attribute'])
        self.attribute_2.setText(data['attribute'])
        self.attribute_3.setText(data['attribute'])
        self.attribute_4.setText(data['attribute']+'加减')
        self.buff_name_1.setText(data['buff']['name'])
        self.buff_name_2.setText(data['buff']['name'])
        self.buff_name_3.setText(data['skill_form'][0]['name'])
        if  len(data['skill_form']) >1:
            self.widget_9.show()
            self.buff_name_4.setText(data['skill_form'][1]['name'])
        else:
            self.widget_9.hide()

        self.ty1_name.setText(data['ty1']['name'])
        self.ty3_name.setText(data['ty3']['name'])

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
        res,diff=result['result'],set_color(result['diff'])
        self.show_buff_attact1.setText(str(res['out_map']['attack']))
        self.show_buff_intellect1.setText(str(res['out_map']['intellect']))
        self.show_buff_attact1_df.setText(diff['out_map']['attack'])
        self.show_buff_intellect1_df.setText(diff['out_map']['intellect'])
        in_map=res['in_map']
        self.show_buff_attack2.setText(str(in_map[0]['attack']))
        self.show_buff_attack3.setText(str(in_map[1]['attack']))
        self.show_buff_intellect2.setText(str(in_map[0]['intellect']))
        self.show_buff_intellect3.setText(str(in_map[1]['intellect']))
        self.show_buff_mp1.setText(str(in_map[0]['multiplier']))
        self.show_buff_mp2.setText(str(in_map[1]['multiplier']))
        in_map=diff['in_map']
        self.show_buff_attack2_df.setText(in_map[0]['attack'])
        self.show_buff_attack3_df.setText(in_map[1]['attack'])
        self.show_buff_intellect2_df.setText(in_map[0]['intellect'])
        self.show_buff_intellect3_df.setText(in_map[1]['intellect'])
        if len(in_map)>2:
            self.show_buff_intellect4_df.setText(in_map[2]['intellect'])
            self.show_buff_attack4_df.setText(in_map[2]['attack'])
            self.show_buff_intellect4.setText(str(res['in_map'][2]['intellect']))
            self.show_buff_attack4.setText(str(res['in_map'][2]['attack']))
            self.show_buff_mp3.setText(str(res['in_map'][2]['multiplier']))

        self.show_ty1.setText(str(res['ty1']))
        self.show_ty3.setText(str(res['ty3']))
        self.show_mp1.setText(str(res['multiplier']['ty1_buff']))
        self.show_mp2.setText(str(res['multiplier']['ty3_buff']))

        self.show_ty1_df.setText(diff['ty1'])
        self.show_ty3_df.setText(diff['ty3'])
        self.show_mp1_df.setText(diff['multiplier']['ty1_buff'])
        self.show_mp2_df.setText(diff['multiplier']['ty3_buff'])

    def set_config(self,names:list[str]):
        self.config_combobox.clear()
        for n in names:
            self.config_combobox.addItem(n)
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
