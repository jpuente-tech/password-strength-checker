#=====================================
#Password Strength checker
#My First Cybersecurity Pyhton Program
#=====================================

# STEP 1: Ask the user for a password

password = input("Enter a test password: ")

#STEP 2: Count the password characters 
length = len(password)
print("Password Length:", length)

#STEP 3: Check for uppercase letters
if length < 12:
    print("Your password is too short.") 
else: 
    print("Your password meets our minimum length.")

#STEP 4: Check for uppercase letters
has_uppercase = False   #Boolean (We haven't found an uppercase letter yet)
#we started with false, because if we started with true it would tell me there is an uppercase even if there isn't

for character in password:    #Loop (python starts to examine each character)
    if character.isupper():   #(Python checks whether that character is uppercase)
        has_uppercase = True  #(Once python finds an uppercase letter,it updates our variable)

print("Contains uppercase:" , has_uppercase)

#STEP 5: Check for Lowercase letters
# same as uppercase section just checking for lowercase this time
has_lowercase = False

for character in password:
    if character.islower():
        has_lowercase = True

print("Contains lowercase:", has_lowercase)

#STEP 6: Check for numbers
# same as uppercase and lowercase but variable changes to check for numbers
has_number = False

for character in password:
    if character.isdigit():
        has_number = True

print("Contains number:", has_number)

#STEP 7: Check for special characters
# same as the other steps we are checking for special characters this time
special_characters = "!@#$%^&*()-_=+{}[]:;'\",.<>/?\\|`~" # we created a varibale that stores symbols our program recognizes.

has_special = False

for character in password:
    if character in special_characters: # the keyword "in" checks to see if any of those characters appear in the password
        has_special = True

print("Comtains speacial character:", has_special)

#STEP 8: Check if all requirements are met

if length >= 12 and has_uppercase and has_lowercase and has_number and has_special:
    print("Password meets all our requirements!")
else:
    print("Password does not meet all requirements.")

#"and" operator. Every condition must be True for the entire expression to be True if one is wrong the "else" statemnt will appear