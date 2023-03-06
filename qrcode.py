import qrcode

print("QRCode Generator by SalakoAdeyemi")

my = input("Enter anything you like to generate QRcode for: ")
img = qrcode.make(my)
img.save('myQrcode.png')
