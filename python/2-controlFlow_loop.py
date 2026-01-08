#control flow and loops

#task 1 : check if the number is Positive, Negative or zero

# num = int(input("enter a number:"))
# if num > 0:
#     print("the number is positive")
# elif num < 0:
#     print("the number is negative")
# else:
#     print("the number is zero")

#task 2: print number from 1 to 10

# for i in range(1,11):
#     print(i)

#task 3: Print even number from 1 to 20 
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

#task 4: print numbers from 1 to 5 using while loop
# count = 1
# while count <= 5:
#     print(count)
#     count +=1

#task 5; break and  continue example

for i in range(1,11):
    if i ==5:
        continue # skip 5
    if i == 8:
        break # stops at 8
    print(i)