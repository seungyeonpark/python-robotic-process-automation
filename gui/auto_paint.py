import webbrowser
import time
import platform
import subprocess
import pyautogui as pa

try:
    if platform.system() == 'Windows':
        subprocess.Popen(r'C:\Windows\System32\mspaint.exe')
        time.sleep(2)
        pa.hotkey('Alt', 'Space', 'X', interval=0.25)

    if platform.system() == 'Darwin':
        path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(path).open('https://keep.google.com/')
        time.sleep(3)
        pa.hotkey('command', 'ctrl', 'f', interval=0.25)
        btn = pa.locateCenterOnScreen('input/brush.png')
        print(btn)
        time.sleep(1)
        pa.click(btn.x / 2, btn.y / 2)
        time.sleep(1)
except:
    pa.alert('페인트 툴이 실행되지 않았다면\n페인트 툴을 직접 실행해주세요.')
    time.sleep(10)
finally:
    bx = 300
    by = 300
    val = 300

    pa.moveTo(bx, by)
    pa.dragTo(bx + val, by + val, 2, button='left')
    pa.drag(-val, 0, 2, button='left')
    pa.drag(0, -val, 2, button='left')

    sec = 0.1
    for i in range(5):
        d = i * 10 + 10
        pa.moveTo(bx + d, bx + d)

        pa.drag(0, val + d, sec, button='left')
        pa.drag(val + d, 0, sec, button='left')
        pa.drag(0, -val - d, sec, button='left')
        pa.drag(-val - d, 0, sec, button='left')
