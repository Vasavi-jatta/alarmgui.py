import tkinter as tk
import datetime
import time
import winsound
def set_alarm():
    alarmtime=entry.get()
    try:
        alarmhour=int(alarmtime[:2])
        alarmminute=int(alarmtime[3:])
        if alarmhour<0 or alarmhour>23 or alarmminute<0 or alarmminute>59:
            raise ValueError
        alarm=datetime.time(hour=alarmhour,minute=alarmminute)
        while True:
            curtime=datetime.datetime.now().time()
            if curtime>=alarm:
                break
            time.sleep(1)
        play_alarm()
    except ValueError:
        error_lable.config(text="invalid time format")

def play_alarm():
    for _ in range(3):
        print('wake up!..')
        winsound.Beep(1000,1000)
        time.sleep(1)
window=tk.Tk()
window.title("alarm clock")
label=tk.Label(window,text="enter alarm time(HH:MM):")
label.pack()
entry=tk.Entry(window)
entry.pack()
button=tk.Button(window,text="set alarm",command=set_alarm)
button.pack()
error_label=tk.Label(window,text="")
error_label.pack()
window.mainloop()
