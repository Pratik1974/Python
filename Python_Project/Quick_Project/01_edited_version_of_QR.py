import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Taking recipient's name and amount (optional)
recipient_name = input("Enter the recipient's name: ")
amount = input("Enter the amount (optional): ")
if amount == '':
    amount = '0'  # If the amount is not provided, it defaults to 0 (optional)

currency = "INR"  # Currency is set to INR by default

# Defining the payment URLs based on the UPI ID and recipient's name, amount, and currency
phonepe_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&mc=1234'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Display the QR codes (You may need to install the PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

# Optionally, save the QR codes to image files
# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')
