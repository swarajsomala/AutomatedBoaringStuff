import pyautogui,time
time.sleep(1)
pyautogui.typewrite("hello swaraj")
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.click()
for i in range(10):
	pyautogui.press('enter')
	pyautogui.hotkey('ctrl', 'v')

