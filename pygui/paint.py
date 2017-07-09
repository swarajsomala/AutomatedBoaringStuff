import pyautogui,time
time.sleep(5)
pyautogui.click()
distance = 100 
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.5)   # move right
	distance = distance-5
	pyautogui.dragRel(0, distance, duration=0.5)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left	
	distance = distance-5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up	

