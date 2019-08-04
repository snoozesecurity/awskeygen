import random

chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","/"]

# Function to print a 20 character string with all uppercase letters and no slashes as per the chars list above

def aws_id():
    output = ''
    for i in range(20):
        output += random.choice(chars[0:36]).upper()
    return output

# Function to print a 40 character string with random uppercase letters and occasional slashes (but only at index 1 through 38)

def aws_key():
    output = ''
    for i in range(40):
        if i == 0 or i == 39:
            ranUpper = random.choice(chars[0:26]).upper()
            output += random.choice([ranUpper, random.choice(chars[0:36])])
        else:
            ranUpper = random.choice(chars[0:26]).upper()
            output += random.choice([ranUpper, random.choice(chars)])
    return output

# Final print statement with proper AWS credentials file formatting

print("[default]")
print("aws_access_key_id=" + aws_id())
print("aws_secret_access_key=" + aws_key())