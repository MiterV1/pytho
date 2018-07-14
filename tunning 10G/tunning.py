import pyautogui
pyautogui.PAUSE=0.1  #将 pyautogui.PAUSE 设置为 1，即每次函数调用后暂停一秒。

inputPercent=pyautogui.prompt(text='please input percnet (0-100)%', title='Set tester percent' , default='30')
print(inputPercent)

#inputPercent='35'

# port 1
#basicLocX, basicLocY = pyautogui.locateCenterOnScreen('basic.png')
#flowLocX, flowLocY = pyautogui.locateCenterOnScreen('flow.png')
basicLocX, basicLocY = 1202,492
flowLocX, flowLocY = 992,556
print("basicLocX=%d,basicLocY=%d" %(basicLocX, basicLocY))
print("flowLocX=%d,flowLocY=%d" %(flowLocX, flowLocY))

pyautogui.click(x=basicLocX, y=basicLocY, duration=0.1)
pyautogui.click(y=basicLocY+15, duration=0.1)

pyautogui.click(x=flowLocX, y=flowLocY, duration=0.1)
pyautogui.click(x=flowLocX+25, y=flowLocY+220, clicks=2)
pyautogui.press(['del', 'del', 'del'])
pyautogui.typewrite(inputPercent)

# downloadX, downloaY = pyautogui.locateCenterOnScreen('download.png')
# print("downloadX=%d,downloaY=%d" %(downloadX, downloaY))
downloadX, downloaY = (1602, 439)
pyautogui.click(x=downloadX, y=downloaY, duration=0.1)
pyautogui.click(x=downloadX+80, y=downloaY-70, duration=0.1)

# port 2
pyautogui.click(x=basicLocX, y=basicLocY, duration=0.1)
pyautogui.click(y=basicLocY+30, duration=0.1)
pyautogui.click(x=flowLocX, y=flowLocY, duration=0.1)
pyautogui.click(x=flowLocX+25, y=flowLocY+220, clicks=2)
pyautogui.press(['del', 'del', 'del'])
pyautogui.typewrite(inputPercent)
pyautogui.click(x=downloadX, y=downloaY, duration=0.1)
pyautogui.click(x=downloadX+80, y=downloaY-70, duration=0.1)

# port 3
pyautogui.click(x=basicLocX, y=basicLocY, duration=0.1)
pyautogui.click(y=basicLocY+45, duration=0.1)
pyautogui.click(x=flowLocX, y=flowLocY, duration=0.1)
pyautogui.click(x=flowLocX+25, y=flowLocY+220, clicks=2)
pyautogui.press(['del', 'del', 'del'])
pyautogui.typewrite(inputPercent)
pyautogui.click(x=downloadX, y=downloaY, duration=0.1)
pyautogui.click(x=downloadX+80, y=downloaY-70, duration=0.1)

# port 4
pyautogui.click(x=basicLocX, y=basicLocY, duration=0.1)
pyautogui.click(y=basicLocY+60, duration=0.1)
pyautogui.click(x=flowLocX, y=flowLocY, duration=0.1)
pyautogui.click(x=flowLocX+25, y=flowLocY+220, clicks=2)
pyautogui.press(['del', 'del', 'del'])
pyautogui.typewrite(inputPercent)
pyautogui.click(x=downloadX, y=downloaY, duration=0.1)
pyautogui.click(x=downloadX+80, y=downloaY-70, duration=0.1)

#see total
pyautogui.click(x=downloadX, y=downloaY+500, duration=0.1)
