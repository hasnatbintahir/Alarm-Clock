from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_PRINT = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        remaining_time = seconds - time_elapsed
        minutes_remaining = remaining_time // 60
        seconds_remaining = remaining_time % 60
        
        print(f"{CLEAR_AND_PRINT}Alarm Rings in {minutes_remaining:02d}:{seconds_remaining:02d}")
    playsound("alarm.mp3")
    
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))

total_seconds = minutes * 60 + seconds
alarm(total_seconds)