import time
from datetime import datetime

new_year_2025 = datetime(2025,1,1,0,0,1)

def countdown(time_until):
    while time_until:
        delta = new_year_2025 - datetime.now()
        print(delta, end="\r")
        time.sleep(1)
        time_until -= 1

countdown(10)