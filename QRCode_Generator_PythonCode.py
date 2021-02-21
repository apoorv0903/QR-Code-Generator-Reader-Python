import qrcode
from pyzbar.pyzbar import decode 
from PIL import Image

qrC = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
qrC.add_data("https://www.linkedin.com/in/erapoorvjain")

qrC.make(fit=True)
qrImg = qrC.make_image()

#create QC code iamge -- QR code Generator - encoding
qrImg.save("QRCode_Apoorvjain_LinkedIn_profile.png")

#decode the QR code
deC = decode(Image.open("QRCode_Apoorvjain_LinkedIn_profile.png"))

#As the decoded data is in binary format. print the ascii value of the message present in the QR code
print(deC[0].data.decode("ascii"))
