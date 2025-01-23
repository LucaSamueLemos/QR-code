import qrcode

imagem=qrcode.make('')

imagem.save("qrcode.png")

print ("QR code gerado!")