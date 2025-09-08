#ask user enter a key
#convert it in to qrcode
import qrcode


#ask user enter a message
secret_message = input("Enter the a secret message: ")


# step 2
# generate a qr code and save 

qr = qrcode.QRCode(box_size="10", border="4")
qr.add_data(secret_message)
qr.make(fit= True)

image = qr.make_image(fill_color="black", black_color="white")
image.save("secret.jpg")


print("secret qr code saved as secret.jpg")
