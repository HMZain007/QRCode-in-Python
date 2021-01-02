import pyqrcode
import os
text = 'Username = abcd, Password = 12345'
qr= pyqrcode.create(text)

qr.png('Facebook.png',scale=10)

os.system('Facebook.png')
