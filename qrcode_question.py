# create a question eg,{"What is 2+2?": "4", "Capital of France?": "Paris"}
# using this question generate a each qrcode
# save them in a file name 



import qrcode

# Questions
choice1 = "What is 2 + 2?"
choice2 = "What is the capital of France?"

# Generate QR code for question 1
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(choice1)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save("q1.png")

# Generate QR code for question 2
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(choice2)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save("q2.png")

print("✅ QR codes generated (q1.png and q2.png). Scan them to see the questions!")

# Function to check answers
def get_answer():
    answer1 = input("Answer for Question 1: ")  # user input
    if answer1.strip() == "4":
        print("Correct! 🎉")
    else:
        print("Wrong ❌")

    answer2 = input("Answer for Question 2: ")  # user input
    if answer2.strip().lower() == "paris":
        print("Correct! 🎉")
    else:
        print("Wrong ❌")

# Run quiz
get_answer()
