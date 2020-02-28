import os
import time

for i in range(500):
    now = str(time.time())
    os.system ('/Users/YuukiTakao/Library/Android/sdk/platform-tools/adb shell screencap -p /storage/self/primary/Pictures/Screenshots/girl_' + now + '.png')
    os.system ('/Users/YuukiTakao/Library/Android/sdk/platform-tools/adb shell input touchscreen tap 750 1850')


