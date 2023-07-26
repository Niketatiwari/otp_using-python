import os
import math
import random
import smtplib

# Step 1: Create a 6-digit random number
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

# Step 2: Store the number in a variable
otp = OTP + " is your OTP"

# Step 3: Write a program to send emails
msg = otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("niketatiwari014@gmail.com", "nzfztbjnqpshyshl")

# Step 5: Request user input for email and OTP
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
