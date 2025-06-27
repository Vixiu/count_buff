import random
import time
import traceback

from sys import argv
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog
from Buff import Buff2 as Buff
from DataClass.SaveData import save
from DataClass.InputData import InputData
from UI import  BuffUI


def interact_with_backend(key,value):
    buff[key]=value
    print(key,value)
    UI.set_show_text(*buff())


def close_clicked():
    QCoreApplication.instance().quit()
    save()

def baseline_clicked():
    buff.set_baseline()
    UI.clear_quick_calc_text()
    UI.set_show_text(*buff())
    UI.set_input_placeholder_text(buff.data)

def job_clicked(job_name):
    save.set_job(job_name)
    buff.init_job(JobData[job_name],save.get_data())
    UI.set_job(JobData[job_name],save.get_data(),save.get_names(), save.last_record)
    UI.set_show_text(*buff())



def config_clicked(index=None):
    buff.init_data(save.get_data(index=index))
    UI.set_input_text(buff.data)
    UI.set_show_text(*buff())
    UI.clear_quick_calc_text()

def offset_edited(value):
    try:
        if value:
            buff.set_offset_intellect(int(value))
        else:
            buff.set_offset_intellect(0)
        UI.set_show_text(*buff())
    except ValueError:
        pass

def add_lv_clicked():
    try:
        UI.show_lv_window(buff.add_lv(
            int(UI.add_1.text()),
            int(UI.add_2.text()),
            int(UI.add_3.text())
        ))
        UI.set_show_text(*buff())
    except ValueError:
        pass

def skill_clicked():
    buff.set_base_skill()
    UI.set_show_text(*buff())
    skill=buff.data.passive_skill
    for  index ,lv in enumerate(skill):
        UI.passive_skill_map[index][2].setPlaceholderText(str(lv))
        UI.passive_skill_map[index][2].setText('')

def del_config_clicked():
    res,info=save.del_item()
    if res:
        UI.set_config_names(save.get_names(),save.last_record)
        UI.config_combobox.setCurrentIndex(save.last_record)
        config_clicked()
    else:
        QMessageBox.information(UI, '奶量计算器', info)

def save_config_clicked():
    _,info= save.set_config(buff.data)
    QMessageBox.information(UI, '奶量计算器', info)


def add_config_clicked(*arg,data=None):
    name, ok = QInputDialog.getText(UI, "奶量计算器", "请输入配置名")
    if ok and name.strip():
        data = InputData() if data is None else data
        save.add_config(name,data)
        UI.set_config_names(save.get_names(),save.last_record)
        config_clicked()


def as_config_clicked():
    add_config_clicked(data=buff.data)

def speculation_clicked():
    skill,value=buff.passive_skill(50)
    sata,val=UI.show_input(skill.name,value)
    if sata:
        val+=buff.data.buff_intellect_out_map
        buff.data.buff_intellect_in_map=val
        buff.data.ty_intellect=val
        UI.buff_intellect_in.setText(str(val))
        UI.ty_intellect.setText(str(val))
        UI.set_show_text(*buff())


def reset_clicked():
    UI.clear_input_text()
    buff.init_data(UI.input_data)
    UI.set_show_text(*buff())




def handle_exception(exc_type, exc_value, exc_traceback):
    # 将异常信息格式化成字符串，方便显示喵！
    error_message = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    # 创建一个消息框，用来展示错误信息哦~ (ฅ>ω<*ฅ)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)  # 设置消息框的图标为“错误”类型喵~

    # 给弹窗加个温柔又实用的标题呢~
    msg_box.setWindowTitle('喵！出错啦~ 或许可以到右上角帮助里的群号反馈')

    # 展示错误信息，可以让主人自己选择复制哦！( •̀ ω •́ )✧
    msg_box.setText(error_message)
    msg_box.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)  # 支持鼠标和键盘选择喵~

    # 弹出消息框，等用户处理完再继续程序~
    msg_box.exec_()
def start():
    # 初始状态
    job_clicked(save.last_job)
    UI.bing_input(interact_with_backend)
    UI.config_combobox.activated.connect(config_clicked)
    for name, bt in UI.job_button.items():
        bt.clicked.connect(lambda _, n=name: job_clicked(n))
    UI.button_del_config.clicked.connect(del_config_clicked)
    UI.input_offset.textEdited.connect(offset_edited)
    UI.button_close.clicked.connect(close_clicked)
    UI.button_base.clicked.connect(baseline_clicked)
    UI.button_skill.clicked.connect(skill_clicked)
    UI.button_add_lv.clicked.connect(add_lv_clicked)
    UI.button_as_config.clicked.connect(as_config_clicked)
    UI.button_add_config.clicked.connect(add_config_clicked)
    UI.button_save_config.clicked.connect(save_config_clicked)
    UI.button_reset.clicked.connect(reset_clicked)
    UI.pushButton_2.clicked.connect(speculation_clicked)

    if save.is_first_launch:
        UI.show_about()






if __name__ == '__main__':
    #QApplication::setHighDpiScaleFactorRoundingPolicy
    #(Qt::HighDpiScaleFactorRoundingPolicy::PassThrough)
    # 保存当前
  #  sys.excepthook = handle_exception
    app = QApplication(argv)
    UI = BuffUI(InputData())
    UI.show()
    from Data import JobData
    buff = Buff(JobData['ma'])
    start()
    app.exec_()
