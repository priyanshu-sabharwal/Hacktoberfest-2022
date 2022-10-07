# Import QRCode from pyqrcode
import pyqrcode
from pyautogui import*
import png
from pyqrcode import QRCode
while True:
    x = str(input('Paste/Type  your link here: '))
    press('', interval = 2)
    write('www.')
    # String which represents the QR code

    # Generate QR code
    url = pyqrcode.create(x)

    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale = 8)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 6)

    print("""QR generated successfully.""")
    print('---------------------------------------------------')

