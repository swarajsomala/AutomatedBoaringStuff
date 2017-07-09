import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width , height = pyautogui.size()
print("{width = }",width,"{height = }",height);
#for i in range(2):
#	pyautogui.moveTo(100,100,duration = 0.25)
#	pyautogui.moveTo(200,100,duration = 0.25)
#	pyautogui.moveTo(200,200,duration = 0.25)
#	pyautogui.moveTo(100,200,duration = 0.25)
try :
	while True:
		width , height = pyautogui.position()
		positionStr = 'X: ' + str(width).rjust(4) + ' Y: ' + str(height).rjust(4)
		print(positionStr, end='')
		print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
	print("CLOSED ☻ ")
