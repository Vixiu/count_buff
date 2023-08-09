import subprocess
import keyboard


def on_key(event):
    if event.name == 'f5':
        subprocess.run('ipconfig /release', capture_output=True, text=True, shell=True)
        print('网络已关闭')
    elif event.name == 'f6':
        subprocess.run('ipconfig /renew', capture_output=True, text=True, shell=True)
        print('网络已开启')


keyboard.on_press(on_key)
keyboard.wait('f8')  # 等待按下ESC键停止程序
