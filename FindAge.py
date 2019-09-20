import datetime

currentYear = datetime.datetime.now().year
DOB=input("Enter your DOB: ")
Age=currentYear-int(DOB)
print("Your age is {}".format(Age))