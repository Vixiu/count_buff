import json
from os import getenv, path, makedirs
from sys import argv
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QGraphicsDropShadowEffect
from Buff import Buff
from UI import  RoundedWindow,BuffUI
from PyQt5.QtCore import Qt
from Config import *
from  copy import deepcopy

#FILE_PATH = r'{}'.format(path.join(getenv("APPDATA", ""), "count_buff", "config.json"))
FILE_PATH =r'C:\Users\xt\Desktop\json.txt'
save_data=deepcopy(CONFIG_TEMPLATE)

def transport_layer(*keys):
    def transport(value):
        buff.set_value(value,*keys)
        UI.set_show_text(buff())
    return transport

def init_config():
    for key in CLASS:
        CLASS[key]['buff']['max_lv']=min(len(CLASS[key]['buff']['attack']),len(CLASS[key]['buff']['intellect']))
        CLASS[key]['ty1']['max_lv'] =len(CLASS[key]['ty1']['intellect'] )
        CLASS[key]['ty3']['max_lv'] = 999
        for item in  CLASS[key]['passive_skill']:
            item['max_lv']=len(item['data'])

def window_top():
    if bool(widget.windowHandle().flags() & Qt.WindowStaysOnTopHint):
        widget.window_top(False)
        UI.button_top.setStyleSheet("")
    else:
        widget.window_top(True)
        UI.button_top.setStyleSheet("background:rgb(212, 218, 230);")

def window_close():
    QCoreApplication.instance().quit()
    save()
def bing_input(dt: dict, ls=None):
    if ls is None:
        ls = []
    for k, v in dt.items():
        ls.append(k)
        if isinstance(v, dict):
            bing_input(v, ls)
        else:
            v.textEdited.connect(transport_layer(*ls))
        ls.pop()

def set_base():
    buff.set_base()
    UI.set_placeholder_text(buff.data)
    UI.set_show_text(buff())
    UI.clear_quick_calc_text()


def set_config(index,update_base=False):
    save_data['record'][buff.job] = index
    data=save_data[buff.job][index]['data']
    buff.set_data(data)
    if update_base:
        set_base()
    else:
        UI.set_input_text(data)
        UI.set_show_text(buff())
    UI.config_combobox.setCurrentIndex(index)



def set_job(job):
    UI.setting(job)
    UI.set_config([key['name'] for key in save_data[job]])
    buff.set_job(job)
    buff.set_offset(0)
    save_data['last'] = job
    set_config(save_data['record'][job],True)


def class_config(job):
    def config():
        set_job(job)
    return config



def offset_value(value:str):
    try:
        value= 0 if value=='' else int(value)
        buff.set_offset(value)
        UI.set_show_text(buff())
    except ValueError:
        pass

def add_lv():
    try:
        result=buff.add_lv(
            int(UI.add_1.text()),
            int(UI.add_2.text()),
            int(UI.add_3.text())
        )

        # 设置input_text
        UI.set_input_text(result['data'])
        UI.set_show_text(buff())


        for item in result['result']:
            print(item)
        html="""
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
        for item in sorted(result['result'], key=lambda x: x['lv']):
            total+= item['increase'] if isinstance(item['increase'],int) else 0
            html+=("<tr>"
                   f"<td align='right'>Lv{item['lv']}  {item['name']}:</td>"
                   f"<td align='center'>{item['old_lv']}</td>"
                   f"<td align='center'>-></td>"
                    f"<td align='center'>{item['new_lv']}</td>"
                   f"<td align='center'>{item['increase']}</td>"
                "</tr>")
        html+=('</table>'
               f'<p style="font-size: 14px; margin-top: 12px;" ><b>四维共:{total},新的等级已应用到计算器内</></p>')
            #'lv': 35, 'name': '禁忌诅咒(图外)', 'old_lv': 21, 'new_lv': 40, 'increase': ''
        QMessageBox.about(widget, '奶量计算器', html)
    except:
        pass
def about():
    html=(
    f'<p>当前版本:{Version}</p>'
    '<p>Bug,意见反馈群:<a href="https://qm.qq.com/cgi-bin/qm/qr?k=RsvjlH8mGFVAFRGL9CvhGnV5q4WDagvw&jump_from=webapi&authKey=/G2wLNZPUbLOO/nUj/faWQgVSGcad9SVjAuOIOlfxlJ2CWiAp9vGD6LxFFDZOkUB">134490967</a></p>'
    '<p>Github开源地址:<a href="https://github.com/Vixiu/count_buff">https://github.com/Vixiu/count_buff</a></p>'
          )
    QMessageBox.about(widget, '奶量计算器', html)

def save():
    if not path.exists(path.dirname(FILE_PATH)):
        makedirs(path.dirname(FILE_PATH))
    save_=deepcopy(save_data)
    job_list = list(CLASS.keys())
    for job,ls in CONFIG_TEMPLATE.items():
        if job in job_list:
            del save_[job][0:len(ls)]
    with open(FILE_PATH,'w+')as f:
        json.dump(save_, f,indent=4 )


def save_config():
    index = save_data['record'][buff.job]
    if index > len(CONFIG_TEMPLATE[buff.job])-1:
        save_data[buff.job][index]['data'] = deepcopy(buff.data)
        set_base()
        save()
    else:
        QMessageBox.information(widget, '奶量计算器', '默认配置不可修改,请另存为!')




def load_config():
    try:
        with open(FILE_PATH,'r') as f:
            data=json.load(f)
        job_list=list(CLASS.keys())
        for job,ls in data.items():
            if job in job_list:
              # save_data[job]=save_data[job]+ls
                for dt in ls:
                    skill={int(k):v for k,v in dt['data']['skill'].items()}
                    dt['data']['skill']=skill
                save_data[job] = save_data[job] + ls

        save_data['last']=data['last']
        save_data['record']=data['record']
    except :
        pass

def del_config():
    index=save_data['record'][buff.job]
    if index>len(CONFIG_TEMPLATE[buff.job])-1:
        save_data[buff.job].pop(index)
        index=max(0,min(index+1,len(save_data[buff.job])-1))
        UI.set_config([key['name'] for key in save_data[buff.job]])
        save()
        set_config(index)
    else:
        QMessageBox.information(widget, '奶量计算器', '默认配置不可删除!')

def add_config(data=None):
    name, ok = QInputDialog.getText(widget, "奶量计算器", "请输入配置名")
    if ok and name.strip():
        data= deepcopy(DEFAULT_INPUT_DATA) if data is None else deepcopy(buff.data)
        save_data[buff.job].append({'name':name,'data':data})
        UI.set_config([key['name'] for key in save_data[buff.job]])
        index=len(save_data[buff.job])-1
        set_config(index)
        save()
    else:
        QMessageBox.critical(widget, '添加失败', '配置名为空')

def as_config():
    add_config(buff.data)
    set_base()

def start():
    # 初始化状态
    init_config()
    load_config()
    set_job(save_data['last'])
    # 顶部按钮绑定
    UI.button_min.clicked.connect(lambda: widget.showMinimized())
    UI.button_top.clicked.connect(window_top)
    UI.button_close.clicked.connect(window_close)
    UI.button_about.clicked.connect(about)
    # 绑定所有输入对象到transport_layer
    bing_input(UI.input_map)
    # 绑定切换职业按钮
    for job,bt in UI.job_button.items():
       bt.clicked.connect(class_config(job))
    # 别的按钮绑定
    UI.button_base.clicked.connect(lambda :set_base())
    UI.input_offset.textEdited.connect(offset_value)
    UI.button_add_lv.clicked.connect(add_lv)
    UI.config_combobox.activated.connect(set_config)
    UI.button_save_config.clicked.connect(save_config)
    UI.button_del_config.clicked.connect(del_config)
    UI.button_add_config.clicked.connect(add_config)
    UI.button_as_config.clicked.connect(as_config)


if __name__ == '__main__':
    #QApplication::setHighDpiScaleFactorRoundingPolicy
    #(Qt::HighDpiScaleFactorRoundingPolicy::PassThrough);

    app = QApplication(argv)
    widget = RoundedWindow()
    UI = BuffUI(widget)
    buff = Buff()
    widget.show()
    widget.setWindowTitle(' 奶量计算器')
    widget.setStyleSheet("color: rgb(0, 0, 0);\n")
    start()
    app.exec_()
