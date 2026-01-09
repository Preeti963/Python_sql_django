#what is function?
"""- block of reusable code
- reduce the  code repetition makes the organized and readable
"""
# basic function
# def greet():
#     print("hello, welcome to python functions!")
# greet()

# function with arguments
# def greet_user(name):
#     print("hello",name)
# greet_user("preeti")

#function with multiple arguments
# def add_numbers(a,b):
#     print("Sum is:",a+b)
# add_numbers(5,3)

#function with return value
# def multiply(a,b):
#     return a*b
# result = multiply(4,5)
# print("result:",result)

#default arguments
# def student_info(name,course="python"):
#     print("Name:",name)
#     print("Course:",course)

# student_info("Sushila")
# student_info("Sushila""\ttamang")

# *args(multiple values)
# def total_marks(*marks):
#     total = sum(marks)
#     print("Total Marks:",total)
# total_marks(80,75,90)

#**kwargs(key-valuse Pairs)
def user_details(**info):
    for key, value in info.items():
        print(key,":",value)
user_details(name="Usik",age=20,role="student")