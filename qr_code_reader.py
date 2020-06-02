import PySimpleGUI as sg 
def decode_qr_codes(file_path):
    from pyzbar.pyzbar import decode
    from PIL import Image

    d = decode(Image.open(file_path))

    text_in_file = d[0].data.decode('ascii')
    sg.popup(f'the file says:-        {text_in_file}')


layout = [ [sg.Text('find the file')],
            [sg.Input(), sg.FileBrowse(button_text='select file')],
            [sg.OK()]]


window = sg.Window("QR code scanner").Layout(layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'OK'):	# if user closes window or clicks cancel
        file = values[0]
        break

decode_qr_codes(file)