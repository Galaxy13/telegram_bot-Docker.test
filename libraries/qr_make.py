import qrcode

def qr_make(web_link):
    qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

    qr.add_data(web_link)
    qr.make(fit=True)
    return qr

def image_make(web_link, CHAT_ID):
    qr = qr_make(web_link)
    img = qr.make_image(fill_color="black",
                    back_color='white').convert('RGB')
    img.save('test_' + CHAT_ID + '.png')