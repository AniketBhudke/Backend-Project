#simple qr code

# import qrcode as qr
# img=qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=2s")
# img.save("wscude_t=youtube.png")


import qrcode
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=2s")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("QR CODE\\youtube_qrcode.png")
print("QR Code generated and saved successfully.")