from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        # Set up the window
        master.title("Calculator")
        master.geometry('357x520+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        # Equation StringVar and Entry widget
        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=17, bg='#fff', font=('Arial', 28), textvariable=self.equation).place(x=0, y=0)

        # Calculator buttons
        Button(master, text='C', width=10, height=3, command=self.clear).place(x=0, y=70)
        Button(master, text='/', width=10, height=3, command=lambda: self.show('/')).place(x=90, y=70)
        Button(master, text='*', width=10, height=3, command=lambda: self.show('*')).place(x=180, y=70)
        Button(master, text='-', width=10, height=3, command=lambda: self.show('-')).place(x=270, y=70)

        Button(master, text='7', width=10, height=3, command=lambda: self.show('7')).place(x=0, y=140)
        Button(master, text='8', width=10, height=3, command=lambda: self.show('8')).place(x=90, y=140)
        Button(master, text='9', width=10, height=3, command=lambda: self.show('9')).place(x=180, y=140)
        Button(master, text='+', width=10, height=3, command=lambda: self.show('+')).place(x=270, y=140)

        Button(master, text='4', width=10, height=3, command=lambda: self.show('4')).place(x=0, y=210)
        Button(master, text='5', width=10, height=3, command=lambda: self.show('5')).place(x=90, y=210)
        Button(master, text='6', width=10, height=3, command=lambda: self.show('6')).place(x=180, y=210)

        Button(master, text='1', width=10, height=3, command=lambda: self.show('1')).place(x=0, y=280)
        Button(master, text='2', width=10, height=3, command=lambda: self.show('2')).place(x=90, y=280)
        Button(master, text='3', width=10, height=3, command=lambda: self.show('3')).place(x=180, y=280)
        Button(master, text='=', width=10, height=7, command=self.solve).place(x=270, y=280)

        Button(master, text='0', width=22, height=3, command=lambda: self.show('0')).place(x=0, y=350)
        Button(master, text='.', width=10, height=3, command=lambda: self.show('.')).place(x=180, y=350)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)  # Evaluate the expression
            self.equation.set(result)  # Display the result
            self.entry_value = str(result)  # Update the entry value to the result
        except:
            self.equation.set('Error')  # Handle any errors
            self.entry_value = ''

# Main program to run the calculator
root = Tk()  # Initialize the root window
calc = Calculator(root)  # Create an instance of the Calculator class
root.mainloop()  # Start the Tkinter event loop
