import pyautogui, time 

amount = input("How many comments to do you want to make?") 
amount = int(amount)
comment = input("What do you want to comment?")

print("The program is starting in 5 seconds.")
time.sleep(5)

pyautogui.scroll(100)
pyautogui.scroll(-7)
time.sleep(2)

for i in range(amount):
    pyautogui.moveTo(200, 490) 
    pyautogui.click()
    pyautogui.write(comment)
    pyautogui.moveTo(1300, 530)
    pyautogui.click()
    time.sleep(3)
