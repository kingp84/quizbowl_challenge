# modules/timers.py

import time

def stall_count(seconds: int = 3):
    for i in range(seconds):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Stall!")