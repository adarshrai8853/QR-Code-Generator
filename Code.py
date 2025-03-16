import qrcode
from qrcode.constants import ERROR_CORRECT_L

try:
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data("https://www.youtube.com/results?search_query=bakchodi+on+top+channel")
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    img.save("youtube.png")
    print("QR code generated successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")
