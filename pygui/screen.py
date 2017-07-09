import pyautogui,pyperclip,time
im= pyautogui.screenshot()
'''
while True:
	x,y = pyautogui.position()
	positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	pixelColor = pyautogui.screenshot().getpixel((x, y))
	positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
	positionStr += ', ' + str(pixelColor[1]).rjust(3)
	positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
	print(positionStr, end='')
	print('\b'*len(positionStr),end = '',flush = True)
'''
time.sleep(2)
im = pyautogui.screenshot()
print(im.getpixel((432,622)))
#im = pyautogui.locateOnScreen('submit.png')
print(im)
#print(pyautogui.center(im))
