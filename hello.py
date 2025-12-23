import os
import time
from datetime import datetime

c_min = datetime.now().minute
while True:
    x = datetime.now().minute
    time.sleep(3)
    if (x - c_min) % 60 == 1:
        os.system("shutdown /s /t 0")
    