def  illuminate(num):
    num= int(num)
    pattern=["yyyyyyn", "nyynnnn", "yynyyny", "yyyynny", "nyynnyy", "ynyynyy", "ynyyyyy", "yyynnnn", "yyyyyyy", "yyyynyy"]
    return pattern[num]
    
def  get_digits(text):
    res=[]
    for i in range (0,len(text)): 
        ch= text[i]
        if (ch>='0' and ch<='9'): 
            res.append(illuminate(ch))
    return res
