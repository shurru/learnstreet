#ROT-13 Project
from string import ascii_uppercase, ascii_lowercase
import math
def string_rot13(str):
    # ROT-13 is a simple substitution cypher. It stands for
    # "ROTate by 13 places." The cypher replaces any letter
    # (a-z or A-Z) with the one that appears 13 sequential places
    # behind it. Note that for the last half of the alphabet, the
    # ROT-13 character loops back around to the beginning of the
    # alphabet. Also note that characters that aren't in the alphabet
    # are passed through.
    "Return a string in its ROT-13 format"
    total = []
    for i in str: 
        if i in ascii_uppercase: 
            indx= (ascii_uppercase.find(i)+13)%26
            total.append(ascii_uppercase[indx])
        elif i in ascii_lowercase: 
            indx= (ascii_lowercase.find(i)+13)%26
            total.append(ascii_lowercase[indx])
        else: 
            total.append(i)
    return ' '.join(total)
    "REPLACE THIS CODE WITH ROT-13 METHOD"
    
    
