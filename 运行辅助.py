# import win32gui, win32ui, win32con
from PIL import Image
# from pyminitouch import MNTDevice
import sys, os
import time
import pyautogui

def wangzhe_fuc():
    # wangzhe

    command = "shell input tap 2000 900"

    command_right_up = "shell input swipe 445 866 640 969 500"

    command_right_down = "shell input swipe 445 866 692 578 200"

    command_right_down2 = "shell input swipe 692 578 692 578 200"

    command_left_up = "shell input swipe 445 866 218 644 500"

    command_left_down = "shell input swipe 445 866 191 963 500"

    # command_base = "/Users/liam/Library/Android/sdk/platform-tools/adb "
    command_base = "adb "

    from random import choice

    command_list = [command_right_up, command_right_down, command_left_up, command_left_down]

    command_list = [command_right_down, command_right_down2]

    for i in range(1000000):
        # time.sleep(1)
        command_move = command_base + choice(command_list)
        os.system(command_move)
        # time.sleep(10)
        # time.sleep(0.1)
        command_input = command_base + command
        os.system(command_input)

    # for i in range(100):
    #     pyautogui.keyDown('A')
    #
    # for i in range(100):
    #     pyautogui.keyDown('A')
    #
    # for i in range(100):
    #     pyautogui.keyDown('D')
    #
    # for i in range(100):
    #     pyautogui.keyDown('S')

# class MyMNTDevice(MNTDevice):
#     def __init__(self,ID):
#         MNTDevice.__init__(self,ID)
#
#
#     def 发送(self,内容):
#         self.connection.send(内容)

# wangzhe_fuc()
#

input_key = ""

def key_method(input):
    global input_key
    input_key = input
    pyautogui.keyDown(input)
    # pyautogui.press(input, interval= 2)
    

class MyMNTDevice():
    def __init__(self,ID):
        # MNTDevice.__init__(self,ID)
        pass


    def 发送(self,内容, Predict = False):

        # wangzhe_fuc()
        Predict = True
        if Predict:

            # pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
            pyautogui.keyUp(input_key)
            # print(" pyautogui.keyUp(input_key):{}".format(input_key))
            if "下移" in 内容 and len(内容) == 2:

                key_method("s")
                
                print(" pyautogui.keyDown('下移s')")
            elif "左移" in 内容 and len(内容) == 2:
                key_method('a')
                
                print("pyautogui.keyDown('左移a')")
            elif "右移" in 内容 and len(内容) == 2:
                key_method('d')
                
                print(" pyautogui.keyDown('右移d')")
            elif "上移" in 内容 and len(内容) == 2:
                key_method('w')
                print("pyautogui.keyDown('上移w')")
            elif "右上移"in 内容 :
                key_method('w')
                key_method('d')
                print("pyautogui.keyDown 右上移")
            elif "左上移"in 内容 :
                key_method('w')
                key_method('a')
                print("pyautogui.keyDown 左上移")
            elif "右下移"in 内容 :
                key_method('d')
                key_method('s')
                print("pyautogui.keyDown('右下移 ')")
            elif "左下移" in 内容 :
                key_method('a')
                key_method('s')
                
                print(" pyautogui.keyDown('左下移')")
            elif "攻击" in 内容 :
                pyautogui.press('up')
                print(" pyautogui.press('攻击 up')")

            elif "补刀" in 内容 :
                pyautogui.press('up')
                print(" pyautogui.press('补刀 up')")
            elif "一技能" in 内容 :
                pyautogui.press('1')
                print(" pyautogui.press('一技能1')")
            elif "二技能" in 内容 :
                pyautogui.press('2')
                print(" pyautogui.press('二技能2')")
            elif "三技能" in 内容 :
                pyautogui.press('3')
                print(" pyautogui.press('三技能3')")
            elif "推塔" in 内容 :
                pyautogui.press('down')
                print(" pyautogui.press('推塔down')")
            elif "恢复" in 内容 :
                pyautogui.press('q')
                print(" pyautogui.press('恢复q')")
            elif "回城" in 内容 :
                pyautogui.press('space')
                print(" pyautogui.press('回城space')")
            elif "移动停" in 内容 :
                pyautogui.keyUp('a')
                pyautogui.keyUp('w')
                pyautogui.keyUp('d')
                pyautogui.keyUp('s')
                print("移动停，releace key")
            elif "4" in 内容 :
                pyautogui.press('4')
                print("press 4")
            elif "5" in 内容 :
                pyautogui.press('5')
                print("press 5")
            elif "6" in 内容 :
                pyautogui.press('6')
                print("press 6")
            elif "f1" in 内容 :
                pyautogui.press('f1')
                print("press f1")
            else:

                print(内容)

            # pyautogui.press('d')  # Simulate pressing the Escape key.
            # pyautogui.keyDown('shift')
            # pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
            # pyautogui.keyUp('shift')
            # pyautogui.hotkey('ctrl', 'c')
        else:
            print("发送")

def 取图(窗口名称):

    im_PIL = pyautogui.screenshot(region=(0, 0, 1000, 650)).convert('RGB')

    box = (0,50,860,530)
    im2 = im_PIL.crop(box)

    print("读取图片")
    # im2.show()
    return im2


