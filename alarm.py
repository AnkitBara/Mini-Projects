"""
mini project - Alarm
"""

from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
print("Setting up alarm..")
print(alarm_hour,alarm_minute, alarm_seconds)
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    print(current_hour)
    print(current_minute)
    if alarm_hour == current_hour:
        if alarm_minute == current_minute:
            print("Wake Up!")
            playsound(r'C:\Users\Badri\Downloads\mixkit-scanning-sci-fi-alarm-905.wav')
            break

'''

T = int(input())
Q = int(input())
stack = []
while T > 0:
    cases = input()

    for char in range(0, len(cases)):
        if char == "a":
            stack += [char[0]]

'''
