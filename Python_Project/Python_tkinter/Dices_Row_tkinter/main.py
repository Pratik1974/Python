import tkinter as tk  # It's better to use an alias for tkinter
import random

root = tk.Tk()  # Tk should be capitalized
root.geometry("700x450")
root.title("Roll Dice")

label = tk.Label(root, text="", font=("times", 260))  # Tkinter widgets should use tk prefix when aliasing

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # Dice Unicode values
    label.configure(text=f'{random.choice(dice)}')  # Corrected: random.choice selects one dice value
    label.pack()

button = tk.Button(root, text="Let's Roll...", width=40, height=5, font=10, bg="white", bd=2, command=roll)  # Button should be capitalized
button.pack(padx=10, pady=10)

label.pack()  # Packing the label before the main loop

root.mainloop()
