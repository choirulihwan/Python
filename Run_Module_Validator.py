#custom modules
#import Module_Validator
from Module_Validator import validate_email

email = "aristhu_oracle@yahoo.com"
#if (Module_Validator.validate_email(email)):
if (validate_email(email)):
    print("Email is valid")
else:
    print("Not a valid email")