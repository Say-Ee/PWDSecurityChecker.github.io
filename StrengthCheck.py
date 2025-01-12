#takes time to startup, but gives instant result

rockyou_file = "rockyou.txt"
with open(rockyou_file, "r", encoding="latin-1") as file:
    rockyou_passwords = set(line.strip() for line in file)
password=input("Enter your password: ")
special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
strength={"Minimum_length":0, "Upper":0, "Lower":0, "Special":0, "Digit":0}
if(len(password)>=8):
    strength["Minimum_length"]=1
if(any(char.isupper() for char in password)):
    strength["Upper"]=1
if(any(char.islower() for char in password)):
    strength["Lower"]=1
if(any(char in special_characters for char in password)):
    strength["Special"]=1
if(any(char.isdigit() for char in password)):
    strength["Digit"]=1
str=sum(strength.values())
feedback = {
    "Minimum_length": "at least 8 characters",
    "Upper": "an uppercase letter",
    "Lower": "a lowercase letter",
    "Special": "a special character (e.g., !@#$%^&*)",
    "Digit": "a number",
}
print("Analysis.... ")
print("Password Strength: ")
if(str==5):
        print("- Strong")
elif(3<=str<5):
    print("- Moderate")
else:
    print("- Weak")
if str < 5:
    print("Feedback")
    print("Your password is missing:")
    for key, value in strength.items():
        if value == 0:
            print(f"- {feedback[key]}")
print("Password Uniqueness: ")
if password in rockyou_passwords:
    print("- Your password is too common!")
else:
    print("- Your password is unique.")