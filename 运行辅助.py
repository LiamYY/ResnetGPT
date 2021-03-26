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
class MyMNTDevice():
    def __init__(self,ID):
        # MNTDevice.__init__(self,ID)
        pass


    def 发送(self,内容):

        # wangzhe_fuc()
        print(内容)
        # pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
        pyautogui.keyUp('a')
        pyautogui.keyUp('w')
        pyautogui.keyUp('d')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('s')

        if 内容 == "下移" or 内容 == "手动模式 下移":

            pyautogui.keyDown('s')
            print(" pyautogui.keyDown('s')")
        elif  内容 == "左移":
            pyautogui.keyDown('a')
            print("pyautogui.keyDown('a')")
        elif 内容 == "右移" or 内容 == "手动模式 右移":
            pyautogui.keyDown('d')
            print(" pyautogui.keyDown('d')")
        elif 内容 == "上移" or  内容 == "手动模式 上移":
            pyautogui.keyDown('w')
            print("")
        elif 内容 == "右下移"or  内容 == "手动模式 右下移":
            pyautogui.keyDown('a')
            pyautogui.keyDown('s')
            print("右下移 pyautogui.keyDown('s')")
        elif 内容 == "左下移" or  内容 == "手动模式 左下移":
            pyautogui.keyDown('')
            pyautogui.keyDown('s')
            print("左下移 pyautogui.keyDown('s')")
        elif 内容 == "攻击":
            pyautogui.moveTo(880, 521, duration=0, tween=pyautogui.easeInOutQuad)
            pyautogui.click()
            print(" pyautogui.click()")
        elif 内容 == "移动停":
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
            print("shift")
        else:
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
            print("else")

        # pyautogui.press('d')  # Simulate pressing the Escape key.
        # pyautogui.keyDown('shift')
        # pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
        # pyautogui.keyUp('shift')
        # pyautogui.hotkey('ctrl', 'c')


def 取图(窗口名称):
    # # 获取后台窗口的句柄，注意后台窗口不能最小化
    # hWnd = win32gui.FindWindow(0,窗口名称)  # 窗口的类名可以用Visual Studio的SPY++工具获取
    # # 获取句柄窗口的大小信息
    # left, top, right, bot = win32gui.GetWindowRect(hWnd)
    # width = right - left
    # height = bot - top
    # # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    # hWndDC = win32gui.GetWindowDC(hWnd)
    # # 创建设备描述表
    # mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # # 创建内存设备描述表
    # saveDC = mfcDC.CreateCompatibleDC()

    # # 创建位图对象准备保存图片
    # saveBitMap = win32ui.CreateBitmap()
    # # 为bitmap开辟存储空间
    # saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # # 将截图保存到saveBitMap中
    # saveDC.SelectObject(saveBitMap)
    # # 保存bitmap到内存设备描述表
    # saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)


    # bmpinfo = saveBitMap.GetInfo()
    # bmpstr = saveBitMap.GetBitmapBits(True)

    im_PIL = pyautogui.screenshot(region=(0, 0, 1000, 650)).convert('RGB')

    ###生成图像
    # im_PIL = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX')
    # im_PIL = Image.open("image/85.jpg")
    #im_PIL= Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr)
    #im_PIL =Image.frombytes('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr)
    box = (0,65,960,545)
    im2 = im_PIL.crop(box)

    #im2.save('./dd2d.jpg')
    # win32gui.DeleteObject(saveBitMap.GetHandle())
    # saveDC.DeleteDC()
    # mfcDC.DeleteDC()
    # win32gui.ReleaseDC(hWnd, hWndDC)
    print("读取图片")
    # im2.show()
    return im2


