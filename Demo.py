import pyautogui
import PIL
pyautogui.PAUSE = 1 #调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常

# 图像识别（一个）
# btm = pyautogui.locateOnScreen('./resource/images/wechat_logo.png')
# print(btm)  # Box(left=1280, top=344, width=22, height=22)

screenwidth,screenheight = pyautogui.size()
screen = pyautogui.screenshot("./resource/images/screen.png")
screen_dpi = int(screen.size[0]/screenwidth)

print(screen_dpi)
# screen = pyautogui.screenshot("./resource/images/screen.png")







