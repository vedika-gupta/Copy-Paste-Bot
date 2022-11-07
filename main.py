import time
import pyautogui as auto

file1 = open(r"Copy-Paste-Bot\paste.txt", "r")
message1 = file1.read()
print(message1)
time.sleep(5)
auto.write(message=message1)
file1.close()
