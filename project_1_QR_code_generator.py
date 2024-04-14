import qrcode

# Create a QR code instance
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data('https://discord.gg/df4k6HkB')
qr.make(fit=True)

# Create an image from the QR code with a dark background
img = qr.make_image(fill_color='white', back_color=(0, 0, 0))  # Use (0, 0, 0) for a black background
img.save('worklyrow.png')
