import pyperclip,time,pyautogui
number = ''
for i in range(10):
	number = number + str(i) + '\n'
pyperclip.copy(number)
time.sleep(5); pyautogui.scroll(10)
