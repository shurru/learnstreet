#Basic units conversion tool
def temperature(n, frm):
    res = []
    if frm == 'fahrenheit':
        celcius = (5 / 9.0) * (n - 32)
        kelvin = ((5 / 9.0) * (n - 32) + 273.15) 
        res.append(celcius)
        res.append(kelvin)
        return res 
    if frm == 'celsius': 
        fahrenheit = (n * (9 / 5.0) + 32) 
        kelvin = (n + 273.15) 
        res.append(fahrenheit)
        res.append(kelvin)
        return res 
     
    if frm == 'kelvin': 
        fahrenheit = (((n - 273.15) * (9 / 5.0)) + 32) 
        celsius = (n - 273.15) 
        res.append(fahrenheit)
        res.append(celsius)
        return res
   
    "REPLACE THIS CODE WITH YOUR TEMPERATURE CONVERSION METHOD"

def length(n, frm):
    "REPLACE THIS CODE WITH YOUR LENGTH CONVERSION METHOD"
    length=[]
    if frm== "miles": 
        km= n*1.609 
        ft= n*5280
        m= (n*1609)
        length.append(km)
        length.append(ft)
        length.append(m)
        return length
    if frm== "feet":
        km= n*0.0003047
        m= n*0.3047 
        mi= n/5280
        length.append(km)
        length.append(m)
        length.append(mi)
        return length
    if frm== "kilometers":
        mi= n/1.609 
        m= n*1000
        ft= n* 3280.85
        length.append(mi)
        length.append(m)
        length.append(ft)
        return length
    if frm== "meters":
        mi= n/1609
        km= n/1000
        ft= n*3.28085
        length.append(mi)
        length.append(km)
        length.append(ft)
        return length
        

def volume(n, frm):
    "REPLACE THIS CODE WITH YOUR VOLUME CONVERSION METHOD"
    vol = [] 
    if frm == 'cubic_meter': 
        milliliters = n * 1000000 
        cubic_inches = n * 61023.74 
        gallons = n * 264.17 
        vol.append(milliliters)
        vol.append(cubic_inches)
        vol.append(gallons)
        return vol 
     
    if frm == 'milliliters': 
        cubic_meters = n * 0.000001 
        cubic_inches = n * 0.061 
        gallons = n * 0.00026 
        vol.append(cubic_meters)
        vol.append(cubic_inches)
        vol.append(gallons)
        return vol 
     
    if frm == 'cubic_inches': 
        cubic_meters = n * 0.000016 
        milliliters = n * 16.38 
        gallons = n * 0.0043 
        vol.append(cubic_meters)
        vol.append(milliliters)
        vol.append(gallons)
        return vol 
     
    if frm == 'gallons': 
        cubic_meters = n * 0.0037 
        milliliters = n * 3785.4 
        cubic_inches = n * 231 
        vol.append(cubic_meters)
        vol.append(milliliters)
        vol.append(cubic_inches)
        return vol


def weight(n, frm):
    "REPLACE THIS CODE WITH YOUR OWN WEIGHT CONVERSION METHOD"
    weight= []
    if frm== "pounds":
        kg= n*0.45
        oz= n*16
        weight.append(kg)
        weight.append(oz)
        return weight
        
    if frm == 'kilograms': 
        pounds = n * 2.2 
        ounces = n * 35.27 
        weight.append(pounds)
        weight.append(ounces)
        return weight 
     
    if frm == 'ounces': 
        pounds = n * 0.0625 
        kilograms = n * 0.028 
        weight.append(pounds)
        weight.append(kilograms)
        return weight
    