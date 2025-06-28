from typing import Callable
import ast
from PyQt5.QtGui import QIntValidator, QValidator, QDoubleValidator, QBrush, QColor, QFont, QPixmap

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLineEdit, QListWidgetItem, QMessageBox, \
    QAbstractItemView, QHeaderView, QTableWidgetItem, QLabel, QPushButton, QDialogButtonBox, QFormLayout, QVBoxLayout, \
    QDialog

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication, QSize
from PyQt5 import QtGui
from DataClass.Result import Result, Item, LvResult
from DataClass.InputData import InputData
from DataClass.Job import Job
from Config  import JobID,Version
from QtUI.uic5 import Ui_widget
from QtUI import images_rc #  不要删除这个导入
from PyQt5.QtWidgets import QLineEdit,QCheckBox,QRadioButton
class LValidator(QValidator):
    def __init__(self,max_,min_=1):
        super().__init__()
        self.min_value,self.max_value=min_,max_
    '''
    def validate(self, text:str, pos):
        if text =='':
            return QValidator.Acceptable, '1', pos
        elif text.isdigit() and self.min <=int(text) <=  self.max:
            return QValidator.Acceptable, text, pos
        elif (text[0] == '+' or text[0] == '-') and (text[1:].isdigit() or not text[1:]):
            return QValidator.Acceptable, text, pos
        return QValidator.Invalid, text, pos
    '''

    def validate(self, input_str, pos):
        # 检查是否为空
        if not input_str:
            return QValidator.Acceptable,input_str, pos

        # 检查是否为数字
        if  input_str.isdigit():
            if self.min_value <=int(input_str) <=  self.max_value:
                return QValidator.Acceptable, input_str, pos
            else:
                return QValidator.Intermediate, input_str, pos
        return  QValidator.Invalid, input_str, pos

    def fixup(self, input_str):
        try:
            value = int(input_str)
            if value < self.min_value:
                return str(self.min_value)
            if value > self.max_value:
                return str(self.max_value)
        except ValueError:
            return str(self.min_value)
class PValidator(QValidator):
    def validate(self, text: str, pos):
        text = text.replace('。', '.').replace(' ', '').replace('，', ',').replace(',,', ',')
        try:
            _ = [float(item) for item in text.split(',') if item]
        except ValueError:
            return QValidator.Invalid, text, pos

        return QValidator.Acceptable, text, pos

class CpArm:
    def __init__(self,check_box:QCheckBox):
        self._check_box=check_box
        self.__base_value =False
    @property
    def textEdited(self):
        return self
    def placeholderText(self):
        return self.__base_value
    def text(self):
        return self._check_box.isChecked()

    def connect(self,callback:callable):
        self._check_box.clicked.connect(lambda:callback(self._check_box.isChecked()))

    def setText(self,bl:str):
        if bl:
            self._check_box.setChecked(bl=='True')
        else:
            self._check_box.setChecked(self.__base_value)

    def setPlaceholderText(self,bl):
        self.__base_value= bl=='True'
        self._check_box.setChecked(self.__base_value)

class Percentage:
    def __init__(self, linedit: QLineEdit):
        self._linedit = linedit
        self.__base_value = []

    @property
    def textEdited(self):
        return self

    def placeholderText(self):
        return self.__base_value

    def text(self):
        return self._to_list()

    def _to_list(self):
        val = self._linedit.text()
        if val != '':
            return [float(i) for i in val.split(",") if i] if val else []
        return []

    def connect(self,callback):
        self._linedit.textEdited.connect(lambda :callback(self._to_list()))

    def setText(self, ls:str):
        self._linedit.setText(ls[1: -1].replace(" ", ""))

    def setPlaceholderText(self, ls):
        self.__base_value=ast.literal_eval(ls)
        self._linedit.setPlaceholderText(ls[1: -1].replace(" ", ""))

class TY3:
    def __init__(self, rb1:QRadioButton,rb2: QRadioButton):
        self.rb1,self.rb2=rb1,rb2
        self.__base_value=True

    @property
    def textEdited(self):
        return self
    def placeholderText(self):
        return self.__base_value

    def text(self):
        return self.rb1.isChecked()

    def connect(self,callback):
        self.rb1.clicked.connect(lambda :callback(self.rb1.isChecked()))
        self.rb2.clicked.connect(lambda :callback(self.rb1.isChecked()))

    def setText(self, bl):
        if bl:
            if bl=='True':
                self.rb1.setChecked(True)
            elif bl=='False':
                self.rb1.setChecked(False)
        else:
            self.rb1.setChecked(self.__base_value)
    def setPlaceholderText(self, bl):
        self.__base_value=bl=='True'
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

class InputDialog(QDialog):
    def __init__(self, parent,lv50_name,value):
        super().__init__(parent)
        self.setWindowTitle("进图推算")
        # 去掉问号按钮
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # 创建布局
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # 设置标签靠右对齐
        form_layout.setLabelAlignment(Qt.AlignRight)

        # 添加输入框
        self.input1 = QLineEdit(self)
        self.input3 = QLineEdit(self)

        # 设置默认值
        self.input1.setText("80")
        self.input3.setText(str(value))
        #
        self.input1.setValidator(QIntValidator())
        self.input3.setValidator(QIntValidator())
        # 设置输入框标签
        form_layout.addRow(QLabel("基于buff(站街)推算"))
        form_layout.addRow("公会Buff(训练教官):", self.input1)
        form_layout.addRow(f"Lv50 {lv50_name}(四维):", self.input3)

        # 添加表单布局到主布局
        layout.addLayout(form_layout)

        # 添加按钮（只保留“确定”按钮）
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok, self)
        self.button_box.accepted.connect(self.accept)
        layout.addWidget(self.button_box)

    def get_inputs(self):
        """返回用户输入的内容"""
        try:
            return int(self.input1.text())+int(self.input3.text())
        except ValueError:
            return 0

def value_convert(value):
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return 0

def linedit_convert(linedit:QLineEdit):
    value=linedit.text()
    if not isinstance(value, str):
        return value
    if value == '':
        return value_convert(linedit.placeholderText())
    # 如果以 '+' 或 '-' 开头，进行加减操作
    if value[0] == '+' or value[0] == '-':
        return value_convert(linedit.placeholderText())+value_convert(value[1:])
    return value_convert(value)


class BuffUI(Ui_widget,RoundedWindow):
        def __init__(self,data:InputData):
            RoundedWindow.__init__(self)
            self.setupUi(self)
            self.button_min.clicked.connect(lambda: self.showMinimized())
            self.button_top.clicked.connect(self.__window_ontop)
            self.button_about.clicked.connect(self.show_about)
            self.setWindowTitle(' 奶量计算器')
            self.setStyleSheet("color: rgb(0, 0, 0);\n")

            # - 以下需要手动绑定输入对象到变量
            # 左侧职业按钮
            self.job_button :dict[str,QPushButton]= {
                'ma': self.ma_button,
                'ba': self.ba_button,
                'luo': self.luo_button,
                'gong': self.gong_button,
                'qiang':self.qiang_button,
            }
            # 被动技能
            self.passive_skill_map:tuple[tuple[QLabel,QLabel,QLineEdit],...]= (
                (self.lv1_name, self.lv1_icon, self.lv1_value),
                (self.lv2_name, self.lv2_icon, self.lv2_value),
                (self.lv3_name, self.lv3_icon,self.lv3_value),
                (self.lv4_name, self.lv4_icon,self.lv4_value),
                (self.lv5_name, self.lv5_icon, self.lv5_value),
                (self.lv6_name, self.lv6_icon,self.lv6_value),
                (self.lv7_name, self.lv7_icon,self.lv7_value),
            )
            # 输入框与InputData对应
            self.input_map= {
                "c_attack":self.c_attack,
                "c_intellect":self.c_intellect,
                # buff属性
                "buff_intellect_in_map":self.buff_intellect_in,
                "buff_lv_in_map":self.buff_lv_in,
                "buff_intellect_out_map":self.buff_intellect_out,
                "buff_lv_out_map":self.buff_lv_out,
                # 增益量
                "buff_amount_in_map":self.buff_amount_in_map,
                "buff_amount_out_map":self.buff_amount_out_map,
                "buff_amount_amp":self.buff_amount_enh,
                # 避邪玉
                "bxy_amp":self.bxy_ehn,
                "bxy_fixed_attack":self.bxy_fixed_attack,
                "bxy_fixed_intellect":self.bxy_fixed_intellect,
                "bxy_fixed_ty":self.bxy_fixed_ty,
                "bxy_percentage_attack":Percentage(self.bxy_percentage_attack),
                "bxy_percentage_intellect": Percentage(self.bxy_percentage_intellect),
                "bxy_percentage_ty":Percentage(self.bxy_percentage_ty),
                # 觉醒
                "ty_ty1_lv":self.ty_lv,
                "ty_intellect":self.ty_intellect,
                "ty_ty3_lv":self.ty3_lv,
                "ty_is_ty1":TY3(self.rb1,self.rb2),
                # 技能
            }
            self.input_map.update(
                {f'passive_skill_{i}':item[2] for i,item in enumerate(self.passive_skill_map)}
            )

            # 表格隐藏的文本
            self.hide_text='--'
            # 右键菜单
            # window.setContextMenuPolicy(Qt.CustomContextMenu)
            # window.customContextMenuRequested.connect(show_menu)
            self.__hide_grids:set[tuple[int,int]]={(-1,-1)}
            self.__validator()
           # self.__effect()
            self.__init_table()
            self.__check(data)

        @property
        def input_data(self)->InputData:
            return InputData(**{k:linedit_convert(v)for k,v in self.input_map.items()})

        def bing_input(self,func:Callable[[str,str],None]):
            for key, qle in self.input_map.items():
                qle.textEdited.connect(lambda _,q=qle, k=key: func(k, linedit_convert(q)))




        def clear_input_text(self):
            for item in self.input_map.values():
                item.setText('')

        def set_input_text(self,data:InputData):
            for k,v in data:
                self.input_map[k].setText(str(v))

        def set_input_placeholder_text(self,data:InputData):
            self.clear_input_text()
            for k, v in data:
                self.input_map[k].setPlaceholderText(str(v))

        def add_row(self, name, img=None,*show):
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                item.setFont(QFont("Arial", 12))
                if col % 2 == 0:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                else:
                    pass
                self.tableWidget.setItem(row, col, item)

            if img is not None :
                label = QLabel()
                label.setPixmap(img)
                label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                label.setContentsMargins(10, 0, 0, 0)
                self.tableWidget.setCellWidget(row, 0, label)
                # self.tableWidget.item(index,0).setIcon(QIcon(f))
            for i,bl in enumerate(show,start=1):
                if not bl:
                    self.__hide_grids.add((row,i*2))
                    self.tableWidget.item(row,i*2).setText(self.hide_text)
            self.tableWidget.item(row, 1).setText(name)

        def clear_quick_calc_text(self):
            self.add_1.setText('')
            self.add_2.setText('')
            self.add_3.setText('')
            self.input_offset.setText('')

        def set_job(self, job:Job,data:InputData,config_name:list[str],config_index:int):
            self.__hide_grids=set()
            #
            self.setWindowIcon(QIcon(job.img))
            # 切换至基础属性
            self.tabWidget.setCurrentIndex(0)
            # 清除快捷计算的文本
            self.clear_quick_calc_text()
            # 属性设置
            self.attribute_1.setText(job.attribute)
            self.attribute_2.setText(job.attribute)
            self.attribute_3.setText(job.attribute)
            self.attribute_4.setText(job.attribute + '加减(+,-)')
            self.increase.setText(f"属性增伤:{job.increase}")
            # 设置显示文本
            self.tableWidget.setRowCount(0) # 清除所有行
            self.add_row(job.buff.name + '(站街)', job.buff.img,True,True,False)
            self.add_row(job.buff.name + '(进图)', job.buff.img,)
            for item in job.skill_form:
                self.add_row(item.name, item.img,*item.show)
            self.add_row(job.ty1.name, job.ty1.img,False,True,False)
            self.add_row(job.ty3.name, job.ty3.img,False,True,False)
            for item in job.total_buff:
                self.add_row(item.name, item.img)
            # 设置左侧按钮
            for bt in self.job_button.values():
                bt.setStyleSheet('')
            self.job_button[job.id].setStyleSheet('border:0px; border-radius: 0px;'
                                                'padding-top:8px;'
                                                'padding-bottom:8px;'
                                                'border-left: 5px solid rgb(5, 229, 254);'
                                                )
            # 等级规则
            self.buff_lv_out.setValidator(LValidator(job.buff.max_lv))
            self.buff_lv_in.setValidator(LValidator(job.buff.max_lv))
            self.ty_lv.setValidator(LValidator(job.ty1.max_lv))
            self.ty3_lv.setValidator(LValidator(9999))

            # 被动技能设置
            for l1,l2 ,l3 in self.passive_skill_map:
                l1.hide()
                l2.hide()
                l3.hide()

            for i, item in enumerate(job.passive_skill):
                self.passive_skill_map[i][0].setText(f"Lv{item.lv} {item.name}")
                self.passive_skill_map[i][1].setPixmap(item.img)
                self.passive_skill_map[i][2].setValidator(LValidator(item.max_lv))
                self.passive_skill_map[i][0].show()
                self.passive_skill_map[i][1].show()
                self.passive_skill_map[i][2].show()
            self.__adjust_column_widths()
            self.set_config_names(config_name,config_index)
            self.set_input_placeholder_text(data)
        def set_config_names(self, names: list[str],index=0):
            self.config_combobox.clear()
            self.config_combobox.addItems(names)
            self.config_combobox.setCurrentIndex(index)

        def set_show_text(self,res:Result,diff:Result):
            for i, (res, diff) in enumerate(zip(res, diff)):
                self.__set_table_text(i, 2, res.attack,diff.attack)
                self.__set_table_text(i, 4, res.intellect, diff.intellect)
                self.__set_table_text(i, 6, res.multiplier, diff.multiplier)
            self.__adjust_column_widths()
        def show_input(self,lv50_name,value):
            dialog = InputDialog(self,lv50_name,value)
            if dialog.exec_() == QDialog.Accepted:
                return True ,dialog.get_inputs()
            else:
                return False,0
        def show_about(self):
            msg_box = QMessageBox()
            html = (
                f"""
                <h3 id="usage">使用及说明</h3>
                <ol>
                    <li>填写buff(站街)请确保穿戴好换装上的装备。</li>
                    <li><strong>Buff（进图）/一觉/三觉：</strong> 请填写实际多人组队进图时的属性.</li>
                    <li><strong>辟邪玉：</strong> 
                        固定三攻/力智请填写<font color="#FF7F50">身上所有固定三攻的总和</font>；  
                        百分比三攻/力智每项<font color="#FF7F50">使用逗号（,）隔开</font>；
                    </li>
                    <li><font color="#6495ED">辟邪玉上的百分比三攻/力智词条内部为加算，请填写一项（所有词条的总和），不要每项用逗号分隔。</font></li>
                    <li><strong>增益量（图内）：</strong>图内生效的增益量,目前有:黄金乡套装的增益量 等。</li>
                    <li>如果输入带有（+，-）号的数字，软件将以基准数据进行加减计算。</li>
                    <li>理论三攻误差范围为±2,如果超出过多，可能是你填的不对！</li>
                </ol>
                <h4>当前版本：{Version}</h4>
                <h4>如有Bug或建议，欢迎加入交流群反馈：
                    <a href="https://qm.qq.com/cgi-bin/qm/qr?k=RsvjlH8mGFVAFRGL9CvhGnV5q4WDagvw&jump_from=webapi&authKey=/G2wLNZPUbLOO/nUj/faWQgVSGcad9SVjAuOIOlfxlJ2CWiAp9vGD6LxFFDZOkUB">
                        134490967
                    </a>
                </h4>
                <h4>软件免费且开源地址：
                    <a href="https://github.com/Vixiu/count_buff">https://github.com/Vixiu/count_buff</a>
                </h4>
                """
            )
            msg_box.setWindowTitle('奶量计算器')
            msg_box.setText(html)
            msg_box.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard|
                Qt.LinksAccessibleByMouse)  # 支持鼠标和键盘选择喵~
            # 弹出消息框，等用户处理完再继续程序~
            msg_box.exec_()


        def show_lv_window(self,result:LvResult):
            html = """
                 <table cellspacing='5' cellpadding='2' width='100%' style="font-size: 14px;">
                         <tr>
                             <th align='right'>技能</th>
                             <th align='center'>原等级</th>
                             <th align='center'></th>
                             <th align='center'>新等级</th>
                             <th align='center'>四维差距</th>
                         </tr>
                 """
            total=0
            for skill in result:
                total+=skill.attribute
                html += ("<tr>"
                         f"<td align='right'>Lv{skill.lv}  {skill.name}:</td>"
                         f"<td align='center'>{skill.old_lv}</td>"
                         f"<td align='center'>-></td>"
                         f"<td align='center'>{skill.new_lv}</td>"
                         f"<td align='center'>{skill.info}</td>"
                         "</tr>")
            html += ('</table>'
                     f'<p style="font-size: 14px; margin-top: 12px;" ><b>四维共:{total},新的等级已应用到计算器内</></p>')
            QMessageBox.about(self, 'test', html)

        def __adjust_column_widths(self):
            #self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            horizontal=self.tableWidget.horizontalHeader()
            horizontal.setSectionResizeMode(QHeaderView.ResizeToContents)
            total_width=sum(horizontal.sectionSize(col) for col in range(horizontal.count()))
            horizontal.setSectionResizeMode(QHeaderView.Fixed)
            if horizontal.width() > total_width:
                scale=horizontal.width()/total_width
                width_sum = 0
                for col in range(horizontal.count()-1):
                    cell_width=int(horizontal.sectionSize(col)*scale)
                    horizontal.resizeSection(col,cell_width)
                    width_sum+=cell_width
                horizontal.resizeSection(horizontal.count()-1,int(horizontal.width()-width_sum))

        def __set_diff(self, row, col, value):
            item = self.tableWidget.item(row, col)
            if value == 0:
                item.setText('')
            elif value > 0:
                item.setText(f'+{value}')
                item.setForeground(QBrush(QColor("green")))
            elif value < 0:
                item.setText(str(value))
                item.setForeground(QBrush(QColor("red")))



        def __init_table(self):
          #  self.tableWidget.setIconSize(QSize(24, 24))
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)  # 禁止选中
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 禁止拖动表头
           # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        def __effect(self):
            def create_effect():
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(15)  # 范围
                effect.setOffset(1, 1)  # 横纵,偏移量
                effect.setColor(QColor("#c3c5c9"))  # 颜色
                return effect
            self.widget_5.setGraphicsEffect(create_effect())
            self.widget_3.setGraphicsEffect(create_effect())
            self.tableWidget.setGraphicsEffect(create_effect())
        def __validator(self):
            # -
            self.buff_amount_out_map.setValidator(QIntValidator())
            self.buff_amount_enh.setValidator(QDoubleValidator())
            self.buff_intellect_out.setValidator(QIntValidator())
            self.buff_intellect_in.setValidator(QIntValidator())
            self.ty_intellect.setValidator(QIntValidator())

            self.buff_amount_in_map.setValidator(QIntValidator())
            self.add_1.setValidator(QIntValidator())
            self.add_2.setValidator(QIntValidator())
            self.add_3.setValidator(QIntValidator())
            self.input_offset.setValidator(QIntValidator())
            # -
            self.bxy_fixed_attack.setValidator(QIntValidator())
            self.bxy_fixed_intellect.setValidator(QIntValidator())
            self.bxy_fixed_ty.setValidator(QIntValidator())
            self.bxy_percentage_intellect.setValidator(PValidator())
            self.bxy_percentage_attack.setValidator(PValidator())
            self.bxy_percentage_ty.setValidator(PValidator())
            self.bxy_ehn.setValidator(QDoubleValidator())
            # -

            # -
            self.c_attack.setValidator(QIntValidator())
            self.c_intellect.setValidator(QIntValidator())


        def __set_table_text(self, row: int, col: int, v1, v2):
            if (row, col) not in self.__hide_grids:
                self.tableWidget.item(row, col).setText(str(v1))
                self.__set_diff(row, col + 1, v2)

        def __check(self,data:InputData):
            if set(self.job_button.keys()) != set(JobID):
                raise ValueError(f'self.job_button与JobName不一致')

            if set(self.input_map.keys()) != set(data.__dict__.keys()):
                raise ValueError(f'错误:InputData与BuffUI.input_map不一致'
                                 f'缺少:{set(data.__dict__.keys())-set(self.input_map.keys())}'
                                 f'多出:{set(self.input_map.keys())-set(data.__dict__.keys())}')
            for key, qle in self.input_map.items():
                qle.setPlaceholderText(str(data.__dict__[key]))

        def __window_ontop(self):
            if bool(self.windowHandle().flags() & Qt.WindowStaysOnTopHint):
                self.window_top(False)
                self.button_top.setStyleSheet("")
            else:
                self.window_top(True)
                self.button_top.setStyleSheet("background:rgb(212, 218, 230);")

