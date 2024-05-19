import time
import subprocess
import platform
import pyperclip
import pyautogui as pa

if platform.system() == 'Windows':
    subprocess.Popen(r'C:\Windows\notepad.exe')
    time.sleep(2)
    pa.write('Hello World!!!')
    pa.press('enter')
    pyperclip.copy("Windows에서 실행")
    pa.hotkey('ctrl', 'v')

if platform.system() == 'Darwin':
    subprocess.Popen(['open', '/System/Applications/TextEdit.app'])
    time.sleep(2)
    pa.write('Hello World!!!')
    pa.press('enter')
    pyperclip.copy("MacOS에서 실행")
    pa.hotkey('command', 'v')