import qrcode


def myqr():

    qr = qrcode.QRCode(
        version=10,
        box_size=10,
        border=5,
    )
    qr.add_data(n)
    qr.make(fit=True)
    qr.setup_position_adjust_pattern()

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("my_qr_generator.png")


n = input("enter data you want to import in QR image? : ")
myqr()
