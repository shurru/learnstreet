""" Rules:
Username:
    1. Username Should be minimum 5 characters long.
    2. No Space, no Special Characters (i.e., must be alphanumeric).
Email:
    1. Valid Email Address.
        = valid characters + '@' + more valid chars + '.' + yet more valid chars
Phone:
    1. Valid US Phone Number(10 digits: 123-454-7890, (123) 454-7890, (123)+454 7890)
Password:
    1. Password length should be minimum 6 characters long.
    2. Password should not be same as Username.
    
"""
import re
def username_validation(name):
    if len(name)>=5: 
        if re.match("^[a-zA-Z0-9_.-]+$", name):
            return True
        else: 
            return False
    else: 
        return False


def email_validation(email):
    regex_email = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
    if len(email)>7: 
        if re.match (regex_email, email): 
            return True
        else: 
            return False 
            
    return False 
    
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"


def phone_validation(phone):
    regex_phone = "(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$"
    if len(phone)>=10: 
        if re.match(regex_phone, phone): 
            return True 
        else: 
            return False
    return False
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    

def password_validation(password, uname):
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    if len(password)>=6: 
        if password!=uname: 
            return True
    else: 
        return False 


def conpassword_validation(conpass, res):
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    if conpass==res: 
        return True
    else: 
        return False
  
