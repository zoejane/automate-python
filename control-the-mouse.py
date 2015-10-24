import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()
print(pyautogui.position())

pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10,duration=1.5)

