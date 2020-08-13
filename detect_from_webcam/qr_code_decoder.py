from pyzbar.pyzbar import decode
def decode_qr_codes(frame):
    d = decode(frame)
    text_in_qr = d[0].data.decode('ascii')
    return text_in_qr