import pyautogui

pyautogui.PAUSE = 1 #调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常

# 图像识别（一个）
# btm = pyautogui.locateOnScreen('./resource/images/wechat_logo.png')
# print(btm)  # Box(left=1280, top=344, width=22, height=22)



""" 比对分辨率，以确定不同设备之间的dpi """
SCREEN_W,SCREEN_H = [1920,1080]  #当前电脑分辨率
screenwidth,screenheight = pyautogui.size()
screen_dpi = float(screenwidth/SCREEN_W)

tick = pyautogui.locateOnScreen("./resource/img/addressBook.png",confidence=0.7)
print(tick)
pyautogui.moveTo(tick.left,tick.top,0)



