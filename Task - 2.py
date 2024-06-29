def pwd_checker(pwd):
    upper=False
    lower=False
    digits=False
    special=False
    
    sc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    for char in pwd:
        if char.isupper():
            upper=True
        elif char.islower():
            lower=True
        elif char.isdigit():
            digits=True
        elif char in sc:
            special=True
        
    l=len(pwd)
    if l>=8 and upper and lower and digits and special:
        return "Strong password"
    elif l>=8 and (upper or lower) and (digits or special):
        return "Moderate password"
    else:
        return "Weak password"
        
password=input("Enter password : ")
strength=pwd_checker(password)
print("The password entered is : ",strength)

