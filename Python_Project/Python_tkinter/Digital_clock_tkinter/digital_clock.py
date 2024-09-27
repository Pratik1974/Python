import tkinter as tk
from time import strftime, sleep
import time
import threading
import random

root = tk.Tk()
root.title("Digital Clock with Timer, Alarm, and Stopwatch")

# List of colors for dynamic background
colors = ["black", "darkblue", "darkgreen", "darkred", "darkviolet", "darkorange"]

# Function to display time and date
def time_display():
    current_time = strftime('%H:%M:%S %p\n%A, %B %d, %Y')
    clock_label.config(text=current_time)
    
    # Change background color dynamically every 5 seconds
    if int(strftime('%S')) % 5 == 0:
        change_bg_color()
        
    clock_label.after(1000, time_display)

# Function to change the background color dynamically
def change_bg_color():
    color = random.choice(colors)
    clock_label.config(background=color)

# Timer functionality
def start_timer():
    timer_seconds = int(timer_input.get())
    while timer_seconds >= 0:
        mins, secs = divmod(timer_seconds, 60)
        timer_label.config(text=f'{mins:02d}:{secs:02d}')
        root.update()
        sleep(1)
        timer_seconds -= 1
    timer_label.config(text="Time's up!")

# Alarm functionality
def alarm():
    alarm_time = alarm_input.get()
    while True:
        current_time = strftime('%H:%M %p')
        if current_time == alarm_time:
            alarm_status_label.config(text="Alarm ringing!")
            break
        sleep(1)

# Stopwatch functionality
running = False
counter = 0

def start_stopwatch():
    global running
    running = True
    update_stopwatch()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global counter
    counter = 0
    stopwatch_label.config(text="00:00:00")

def update_stopwatch():
    global counter
    if running:
        minutes, seconds = divmod(counter, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        counter += 1
        root.after(1000, update_stopwatch)

# UI Layout

# Clock Display
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white', bd=20, relief='sunken', padx=20, pady=20)
clock_label.pack(anchor='center')

# Timer Section
timer_frame = tk.Frame(root)
timer_frame.pack(pady=10)

timer_label = tk.Label(timer_frame, text="Timer (minutes:seconds)", font=('calibri', 20))
timer_label.pack(side=tk.TOP)

timer_input = tk.Entry(timer_frame, width=5)
timer_input.pack(side=tk.LEFT)

start_timer_button = tk.Button(timer_frame, text="Start Timer", command=lambda: threading.Thread(target=start_timer).start())
start_timer_button.pack(side=tk.LEFT, padx=5)

# Alarm Section
alarm_frame = tk.Frame(root)
alarm_frame.pack(pady=10)

alarm_label = tk.Label(alarm_frame, text="Set Alarm (HH:MM AM/PM)", font=('calibri', 20))
alarm_label.pack(side=tk.TOP)

alarm_input = tk.Entry(alarm_frame, width=10)
alarm_input.pack(side=tk.LEFT)

set_alarm_button = tk.Button(alarm_frame, text="Set Alarm", command=lambda: threading.Thread(target=alarm).start())
set_alarm_button.pack(side=tk.LEFT, padx=5)

alarm_status_label = tk.Label(alarm_frame, text="", font=('calibri', 15))
alarm_status_label.pack(side=tk.LEFT)

# Stopwatch Section
stopwatch_frame = tk.Frame(root)
stopwatch_frame.pack(pady=10)

stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00", font=('calibri', 30))
stopwatch_label.pack()

start_stopwatch_button = tk.Button(stopwatch_frame, text="Start", command=start_stopwatch)
start_stopwatch_button.pack(side=tk.LEFT, padx=5)

stop_stopwatch_button = tk.Button(stopwatch_frame, text="Stop", command=stop_stopwatch)
stop_stopwatch_button.pack(side=tk.LEFT, padx=5)

reset_stopwatch_button = tk.Button(stopwatch_frame, text="Reset", command=reset_stopwatch)
reset_stopwatch_button.pack(side=tk.LEFT, padx=5)

# Start the clock
time_display()

# Run the main event loop
root.mainloop()
