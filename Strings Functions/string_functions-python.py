#string defs project
def revers(str):
    str2= str[::-1] #reverses the string
    return str2
    # Accept an input string, str, and reverse its characters in order
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"

def uppercase(str):
    str0= str.upper()
    return str0
    # Convert all the characters of the input string, str, to upper
    # case. Reurn the uppercased string.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"

def palindrome(str):
    str2=revers(str)
    if str2== str:
        return "is a palindrome"
    else:
        return "is not a palindrome"
    
    # Check if the input string, str, is spelled the same forwards
    # as it is spelled backwards.
    # Return "is a palindrome" if it is, or "is not a palindrome" if it is not.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"