import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr():
    upi_id = upi_entry.get()
    name = name_entry.get()
    amount = amount_entry.get()

    # Validation for required fields
    if not upi_id or not name:
        messagebox.showerror("Error", "UPI ID and Recipient Name are required!")
        return
    
    if not amount:  # If amount is empty, default to 0
        amount = '0'
    
    # Generate UPI URL
    upi_url = f'upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR'
    
    # Create QR code and display it
    qr = qrcode.make(upi_url)
    qr.show()

# Set up the Tkinter GUI window
root = tk.Tk()
root.title("UPI QR Code Generator")

# Create input fields and labels
tk.Label(root, text="UPI ID").grid(row=0)
tk.Label(root, text="Recipient Name").grid(row=1)
tk.Label(root, text="Amount").grid(row=2)

upi_entry = tk.Entry(root)
name_entry = tk.Entry(root)
amount_entry = tk.Entry(root)

upi_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)

# Add a button to generate the QR code
tk.Button(root, text="Generate QR", command=generate_qr).grid(row=3, column=1)

# Start the Tkinter main loop
root.mainloop()
