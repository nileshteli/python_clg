# for i in range(5):
#     for ap in range(i,4-i):
#             print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# print("out of loop")


# for i in range(11):
#     for j in range(i+1):
#         print(j,end=' ')
#     print()
# print("out of loop")

#program to print reverse of a 3 digit number using loop.
# n,x,y= input("Enter a three numeber").split()
# n,x,y=int(n),int(x),int(y)
# num=n,x,y
# print(num[::-1])


# program to find largest of three numbers
# a,b,c = input("Enter a  three number: ").split()
# a,b,c = int(a),int(b),int()
# if a>b and a>c:
#     print("a is greater than ")
# elif b>a and b>c:
#     print("b is greater than")
# else:
#     print("c is greater than")



# program to print numbers from 1 to 35 skipping the multiples of 3

# for i in range(1,35):
#     if(i%3==0):
#         continue
#     print(i)



# program to print multipicatioN TABLE  of a given numbers . Print the result using format string.
# n = input("Enter a number")
#
# for i in range(1,11):
#     result = 5 * i
#     print(f"{n}*{i}=",result)

# program to read  priciopal , rate and time using a single input statement and calculate simple and amount . Use f string to print the result.


# principal, rate, time = map(float, input("Enter principal, rate (as a percentage), and time (in years) separated by spaces: ").split())
#
# rate /= 100
#
#
# simple_interest = principal * rate * time
# amount = principal + simple_interest
# print(f"Principal: {principal:.2f}")
# print(f"Rate: {rate:.2%}")
# print(f"Time:",time,"years")
# print(f"Simple Interest: {simple_interest:.2f}")
# print(f"Amount: {amount:.2f}")


# program to read the total bill amount from user and provide a discount of 10% if bill amount greate than 1000. then print the discount in rupees and net payable amount

# Get input for the total bill amount
# total_bill_amount = float(input("Enter the total bill amount: "))
#
# # Check if the bill amount is greater than 1000
# if total_bill_amount > 1000:
#     # Calculate the discount (10% of the total bill amount)
#     discount = 0.10 * total_bill_amount
#
#     # Calculate the net payable amount after discount
#     net_payable_amount = total_bill_amount - discount
#
#     # Print the discount in rupees and net payable amount
#     print(f"Discount: ₹{discount:.2f}")
#     print(f"Net Payable Amount: ₹{net_payable_amount:.2f}")
# else:
#     # If the bill amount is not greater than 1000, no discount is applied
#     print("No discount applied. Net Payable Amount: ₹{:.2f}".format(total_bill_amount))


# program to read day number from user and print day name.
#
# day_number = int(input("Enter the day number (1-7): "))
#
# if day_number == 1:
#     "Monday"
# elif day_number == 2:
#     "Tuesday"
# elif day_number == 3:
#     print("Wednesday")
# elif day_number == 4:
#     print("Thursday")
# elif day_number == 5:
#     print("Friday")
# elif day_number == 6:
#     print("Saturday")
# elif day_number == 7:
#     print("Sunday")
# else:
#     print("Invalid")


# program to read a string from user and print number of spaces, number of digits and number alphabets present in string

# s = input('Enter a some thing: ')
#
# spaces=0
# digits=0
# alphabets=0
#
# for i in s:
#     if(i.isdigit()):
#         digits+=1
#     elif(i.isspace()):
#         spaces+=1
#     elif(i.isalpha()):
#         alphabets+=1
# print('Number of digits:',digits)
# print('Number of spaces:',spaces)
# print('Number of alphabets:',alphabets)



# Read a numbers from user,print its first 5 multiples in separate lines using a single print statement

# Get input for the number from the user
# number = int(input("Enter a number: "))
#
# # Print the first 5 multiples in separate lines using a single print statement
# print(f"The first 5 multiples of {number} are:")
# for i in range(1, 6):
#     print(f"{number} x {i} = {number * i}")


# program to read two numbers from user and print grater number among those number using a single liner if else statements

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
#
#
# print(f"The greater number is: {number1 if number1 > number2 else number2}")
#

# Program to read a numbers from user and check if it even or odd using a single liner if else statements
# number = int(input("Enter a number: "))
# print(f"The number is {'even' if number % 2 == 0 else 'odd'}.")


# Read a number from user , print its first 5 multiples in same line using a 5 print statements

# number = int(input("Enter a number: "))
# print(f"The first 5 multiples of {number} are:", end=" ")
# for i in range(1, 6):
#     print(number * i, end=" ")


# Program to print the following pattern using a single for loop.
# rows = 5
# for i in range(1, rows * 2):
#     if i <= rows:
#         print("*" * i)
#     else:
#         print("*" * (rows * 2 - i))


# Program to print first n terms of Fibonacci series
# Function to print the first n terms of Fibonacci series


# def fibonacci(n):
#     fib_series = [0, 1]
#
#     for i in range(2, n):
#         next_term = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_term)
#
#     return fib_series[:n]
#
# n = int(input("Enter the number of terms for the Fibonacci series: "))
#
# result = fibonacci(n)
# print(f"The first {n} terms of the Fibonacci series are: {result}")


# Program to read a string from keyboard  and print all of its characters in separatess lines
 # Get input for the string from the user

# user_input = input("Enter a string: ")
# for char in user_input:
#     print(char)


# Read a string from user and apply following functions on it a.partition b. split c.rpartition

#
# user_input = input("Enter a string: ")
# result_partition = user_input.partition(' ')
# result_split = user_input.split(' ')
# result_rpartition = user_input.rpartition(' ')
# print(f"\nResult of partition function: {result_partition}")
# print(f"Result of split function: {result_split}")
# print(f"Result of rpartition function: {result_rpartition}")

 # ADD

# a=input("Enter a string: ")
# print(a.partition(" "))
# print(a.split(" "))
# print(a.rpartition(" "))


# Read a string and  a substring from user, check whether the string contains the substring if  yes print its position , else print "No"

main_string = input("Enter a main string: ")
substring = input("Enter a substring: ")
position = main_string.find(substring)
if position != -1:
    print(f"The substring '{substring}' is found at position {position + 1}.")
else:
    print("No")
