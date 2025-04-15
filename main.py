import json




from sys import argv
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QGraphicsDropShadowEffect
from Buff import Buff, UIData
from Data import JobData
from DataClass.SaveData import save
from DataClass.InputData import InputData
from UI import  RoundedWindow,BuffUI



def close_clicked():
    QCoreApplication.instance().quit()
    save()

def base_clicked():
    buff.set_base()
    UI.clear_quick_calc_text()
    UI.set_show_text(*buff())

def job_clicked(job_name):
    UI.set_job(JobData[job_name])
    save.set_job(job_name)
    UI.set_config_names(save.get_names())
    buff.set_job_data(JobData[job_name])

    buff.update(save.get_data())

    buff.set_skill_base()
    buff.set_base()
    UI.set_show_text(*buff())
    UI.clear_quick_calc_text()


def config_clicked(index=None):
    buff.update(save.get_data(index=index))
    UI.set_show_text(*buff())
    UI.clear_quick_calc_text()

def offset_edited(value):
    try:
        if value:
            buff.set_offset(int(value))
        else:
            buff.set_offset(0)
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
    buff.set_skill_base()
    UI.set_show_text(*buff())
def del_config_clicked():
    res,info=save.del_item()
    if res:
        UI.set_config_names(save.get_names())
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
        UI.set_config_names(save.get_names())
        UI.config_combobox.setCurrentIndex(save.last_record)
        config_clicked()
    else:
        QMessageBox.critical(UI, '失败', '配置名为空')

def as_config_clicked():
    add_config_clicked(data=buff.data)
def start():
    # 初始状态
    input_data=UIData()
    for k, v in UI.input_map.items():
        input_data.bing_input(k, v,lambda :UI.set_show_text(*buff()))
    buff.init(input_data)
    job_clicked(save.last_job)
    #
    for name, bt in UI.job_button.items():
        bt.clicked.connect(lambda _, n=name: job_clicked(n))
    UI.config_combobox.activated.connect(config_clicked)
    UI.input_offset.textEdited.connect(offset_edited)
    UI.button_close.clicked.connect(close_clicked)
    UI.button_base.clicked.connect(base_clicked)
    UI.button_skill.clicked.connect(skill_clicked)
    UI.button_add_lv.clicked.connect(add_lv_clicked)
    UI.button_del_config.clicked.connect(del_config_clicked)
    UI.button_as_config.clicked.connect(as_config_clicked)
    UI.button_add_config.clicked.connect(add_config_clicked)
    UI.button_save_config.clicked.connect(save_config_clicked)
    UI.pushButton_2.clicked.connect(lambda :QMessageBox.critical(UI, 'test', '未实现'))
if __name__ == '__main__':
    #QApplication::setHighDpiScaleFactorRoundingPolicy
    #(Qt::HighDpiScaleFactorRoundingPolicy::PassThrough)
    app = QApplication(argv)
    UI = BuffUI()
    UI.show()
    buff = Buff()
    start()
    app.exec_()
