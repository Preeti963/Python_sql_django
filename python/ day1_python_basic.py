#day 1: python basics
# variables,Data Types,Intput/output ,conditions

#variables and data tpes
name="Preeti"
age = 20
height = 5
is_student=True

print("Name:",name)
print("Age:",age)
print("Height:",height)
print("IS Student:",is_student)

print("\n-- user Input Example ---")

#Taking input from User
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("your age is ", user_age)

print("\n-- If-Else Condition ---")

#condition check 
if user_age >= 18:
    print("you are eligiable to vote.")
else:
    print("You are not eligible to vote.")

#