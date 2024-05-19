import time
import subprocess
import platform
import pyautogui as pa

calc_png = './input/calc.png'
calc_root = './input/calc_root.png'

if platform.system() == 'Windows':
    app = [r'c:\Windows\System32\calc.exe']
    subprocess.Popen(app)
elif platform.system() == 'Darwin':
    app = ['open', '/System/Applications/Calculator.app']
    time.sleep(3)
    subprocess.Popen(app)
    time.sleep(3)
    pa.hotkey('command', '2', interval=0.25)

time.sleep(3)

pos = None
for i in range(10):
    pos = pa.locateOnScreen(calc_png, grayscale=True, confidence=0.5)
    if pos is None:
        time.sleep(1)
        print('찾고 있습니다')
        continue
    break

if pos is None:
    pa.alert('찾지 못했습니다')
    quit()

print('찾았습니다! 계산기: ', pos)

pa.write('3 * 3 =', interval=0.3)
r_btn = pa.locateCenterOnScreen(calc_root, grayscale=True, confidence=0.5)
print('버튼: ', r_btn)
time.sleep(3)
if platform.system() == 'Windows':
    pa.click(r_btn)
else:
    pa.click(r_btn.x / 2, r_btn.y / 2)

print('키 입력 완료')
