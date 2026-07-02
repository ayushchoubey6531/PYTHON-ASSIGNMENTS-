"""
1. Write a Python program to check if a number is positive.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Not a Positive Number")

Enter a number: -5
Not a Positive Number

Enter a number: 20
Positive Number

2. Print "Eligible to vote" if age is 18 or above.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

Enter your age: 20
Eligible to vote

Enter your age: 17
Not eligible

3.Check if a number is divisible by 7

num = int(input("Enter a number: "))

if num % 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")

Enter a number: 21
The number is divisible by 7

Enter a number: 20
The number is not divisible by 7

4. Print "Pass" if marks are greater than 40.

marks = int(input("Enter marks: "))

if marks > 40:
    print("Pass")
else:
    print("Fail")

Enter marks: 55
Pass

Enter marks: 25
Fail

5. Check if a number is greater than 100.

num = int(input("Enter a number: "))

if num > 100:
    print("The number is greater than 100")
else:
    print("The number is not greater than 100")

Enter a number: 152
The number is greater than 100

Enter a number: 85
The number is not greater than 100

6. Display a message if temperature exceeds 45°C.

temperature = int(input("Enter temperature in °C: "))

if temperature > 45:
    print("Temperature exceeds 45°C")

Enter temperature in °C: 52
Temperature exceeds 45°C

7. Check if a string length is more than 8 characters.

text = input("Enter a string: ")

if len(text) > 8:
    print("The string has more than 8 characters")
else:
    print("The string has 8 or fewer characters")

Enter a string: PYTHONPROGRAMMING
The string has more than 8 characters

Enter a string: PYTHON
The string has 8 or fewer characters

8. Print "Logged In" if password matches "admin123".

password = input("Enter password: ")

if password == "admin123":
    print("Logged In")

Enter password: admin123
Logged In

9. Check if a number is a multiple of 10.

num = int(input("Enter a number: "))

if num % 10 == 0:
    print("The number is a multiple of 10")
else:
    print("The number is not a multiple of 10")

Enter a number: 50
The number is a multiple of 10

Enter a number: 25
The number is not a multiple of 10

10. Print a warning if balance is below minimum limit.

balance = int(input("Enter account balance: "))
minimum_limit = 1000

if balance < minimum_limit:
    print("Warning: Balance is below the minimum limit")

Enter account balance: 500
Warning: Balance is below the minimum limit

11. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

Enter a number: 4
Even

Enter a number: 3
Odd

12. Find the largest of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Largest number is", num1)
else:
    print("Largest number is", num2)

Enter first number: 40
Enter second number: 20
Largest number is 40

13. Check whether a person is eligible for driving license.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

Enter your age: 20
Eligible for driving license

Enter your age: 15
Not eligible for driving license

14. Print "Pass" or "Fail" based on marks.

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

Enter your marks: 50
Pass

Enter your marks: 30
Fail

15. Check whether a number is positive or negative.

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

Enter a number: 12
Positive

Enter a number: -5
Negative

16. Check whether a character is a vowel or consonant.

ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

Enter a character: a
Vowel

Enter a character: b
Consonant

17. Check if a year is leap or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

Enter a year: 2024
Leap Year

Enter a year: 2023
Not a Leap Year

18. Print "Valid Password" or "Invalid Password".

password = input("Enter password: ")

if password == "admin123":
    print("Valid Password")
else:
    print("Invalid Password")
Enter password: admin123
Valid Password

Enter password: hello123
Invalid Password

19. Determine whether salary is taxable or not.

salary = float(input("Enter your salary: "))

if salary > 250000:
    print("Taxable")
else:
    print("Not Taxable")

Enter your salary: 300000
Taxable

Enter your salary: 100000
Not Taxable

20. Check whether a number is greater than 50 or not.

num = int(input("Enter a number: "))

if num > 50:
    print("The number is greater than 50")
else:
    print("The number is not greater than 50")

Enter a number: 75
The number is greater than 50

Enter a number: 20
The number is not greater than 50

21. Find the largest of three numbers.

# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)

Enter first number: 15
Enter second number: 18
Enter third number: 30
The largest number is: 30.0

22. Check whether a number is positive, negative, or zero.

num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

Enter a number: 25
The number is Positive.

Enter a number: -8
The number is Negative.

Enter a number: 0
The number is Zero.

#23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60

marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

Enter your marks: 90
Grade: A

Enter your marks: 80
Grade: B

Enter your marks: 65
Grade: C

Enter your marks: 45
Grade: Fail

24. Check whether a triangle is equilateral, isosceles, or scalene.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a == b == c:
    print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")

Enter first side: 5
Enter second side: 5
Enter third side: 5
The triangle is Equilateral.

Enter first side: 5
Enter second side: 5
Enter third side: 4
The triangle is Isosceles.

Enter first side: 3
Enter second side: 5
Enter third side: 4
The triangle is Scalene.

25.Check whether a character is uppercase, lowercase, digit, or special character.

ch = input("Enter a character: ")
if ch.isupper():
    print("The character is an Uppercase letter.")
elif ch.islower():
    print("The character is a Lowercase letter.")
elif ch.isdigit():
    print("The character is a Digit.")
else:
    print("The character is a Special character.")

Enter a character: a
The character is a Lowercase letter.

Enter a character: A
The character is an Uppercase letter.

Enter a character: 3
The character is a Digit.

Enter a character: @
The character is a Special character.

26. Calculate electricity bill using slab-wise rates

units = float(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = (100 * 1.50) + ((units - 100) * 2.50)
else:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
print("Electricity Bill = ₹", bill)

Enter electricity units consumed: 80
Electricity Bill = ₹ 120.0

Enter electricity units consumed: 150
Electricity Bill = ₹ 275.0

Enter electricity units consumed: 250
Electricity Bill = ₹ 600.0

27. Validate login using username and password.

correct_username = "admin"
correct_password = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid Username or Password.")

Enter username: admin
Enter password: 1234
Login Successful!

Enter username: user
Enter password: 1234
Invalid Username or Password.

28. Check student result using marks of 3 subjects.

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
total = m1 + m2 + m3
percentage = (total / 300) * 100
if m1 >= 33 and m2 >= 33 and m3 >= 33 and percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

print("Percentage:", percentage)

Enter marks of subject 1: 45
Enter marks of subject 2: 55
Enter marks of subject 3: 60
Result: Pass
Percentage: 53.333333333333336

Enter marks of subject 1: 30
Enter marks of subject 2: 55
Enter marks of subject 3: 50
Result: Fail
Percentage: 45.0

29. Find the second largest number among three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a > b and a < c) or (a > c and a < b):
    second_largest = a
elif (b > a and b < c) or (b > c and b < a):
    second_largest = b
else:
    second_largest = c
print("Second largest number is:", second_largest)

Enter first number: 10
Enter second number: 20
Enter third number: 30
Second largest number is: 20.0

Enter first number: 50
Enter second number: 10
Enter third number: 30
Second largest number is: 30.0

30. Check loan eligibility using age, salary, and credit score.

age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))
if age >= 21 and salary >= 25000 and credit_score >= 650:
    print("Loan Status: Eligible")
else:
    print("Loan Status: Not Eligible")

Enter age: 25
Enter monthly salary: 36000
Enter credit score: 700
Loan Status: Eligible

Enter age: 19
Enter monthly salary: 40000
Enter credit score: 720
Loan Status: Not Eligible

Enter age: 30
Enter monthly salary: 20000
Enter credit score: 680
Loan Status: Not Eligible

31. Print day name using day number (1–7).#include <stdio.h>

day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number! Please enter a number between 1 and 7.")

Enter day number (1-7): 3
Wednesday

Enter day number (1-7): 9
Invalid day number! Please enter a number between 1 and 7.

32. Print month name using month number.

month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")

Enter month number (1-12): 10
October

Enter month number (1-12): 16
Invalid month number! Please enter a number between 1 and 12.

33. Display grade based on percentage.

percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
elif percentage >= 40:
    print("Grade: E")
elif percentage >= 0:
    print("Grade: F (Fail)")
else:
    print("Invalid percentage!")

Enter your percentage: 92
Grade: A+

Enter your percentage: 75
Grade: B

Enter your percentage: 35
Grade: F (Fail)

34. Display bonus percentage based on experience years. 

experience = int(input("Enter years of experience: "))

if experience >= 10:
    print("Bonus: 20%")
elif experience >= 5:
    print("Bonus: 10%")
elif experience >= 2:
    print("Bonus: 5%")
elif experience >= 0:
    print("Bonus: No Bonus")
else:
    print("Invalid experience!")

Enter years of experience: 12
Bonus: 20%

Enter years of experience: 6
Bonus: 10%

Enter years of experience: 3
Bonus: 5%

Enter years of experience: 1
Bonus: No Bonus

Enter years of experience: -5
Invalid experience!

35. Identify traffic signal meaning. 

signal = input("Enter traffic signal color (Red/Yellow/Green): ")

if signal.lower() == "red":
    print("Stop")
elif signal.lower() == "yellow":
    print("Get Ready")
elif signal.lower() == "green":
    print("Go")
else:
    print("Invalid traffic signal color!")


Enter traffic signal color (Red/Yellow/Green): red
Stop

Enter traffic signal color (Red/Yellow/Green): yellow
Get Ready

Enter traffic signal color (Red/Yellow/Green): green
Go

Enter traffic signal color (Red/Yellow/Green): blue
Invalid traffic signal color!

36. Categorize temperature as Cold / Warm / Hot.

temperature = float(input("Enter temperature (°C): "))

if temperature < 20:
    print("Cold")
elif temperature <= 30:
    print("Warm")
else:
    print("Hot")

Enter temperature (°C): 15
Cold

Enter temperature (°C): 25
Warm

Enter temperature (°C): 38
Hot

37. Categorize employee based on salary range. 

salary = float(input("Enter employee salary: "))

if salary >= 100000:
    print("High Salary Employee")
elif salary >= 50000:
    print("Medium Salary Employee")
elif salary >= 20000:
    print("Low Salary Employee")
elif salary >= 0:
    print("Very Low Salary Employee")
else:
    print("Invalid salary!")

Enter employee salary: 120000
High Salary Employee

Enter employee salary: 60000
Medium Salary Employee

Enter employee salary: 15000
Very Low Salary Employee

38. Print discount percentage based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount >= 10000:
    print("Discount: 20%")
elif amount >= 5000:
    print("Discount: 10%")
elif amount >= 2000:
    print("Discount: 5%")
elif amount >= 0:
    print("Discount: No Discount")
else:
    print("Invalid amount!")

Enter purchase amount: 12000
Discount: 20%

Enter purchase amount: 6000
Discount: 10%

Enter purchase amount: 800
Discount: No Discount

39. Identify number type: single-digit / double-digit / multi-digit.

num = int(input("Enter a number: "))

if -9 <= num <= 9:
    print("Single-digit number")
elif -99 <= num <= 99:
    print("Double-digit number")
else:
    print("Multi-digit number")

Enter a number: 7
Single-digit number

Enter a number: 45
Double-digit number

Enter a number: 1235
Multi-digit number

40. Assign performance rating: Poor / Average / Good / Excellent. 

score = float(input("Enter performance score (0-100): "))

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Average")
elif score >= 0:
    print("Poor")
else:
    print("Invalid score!")

Enter performance score (0-100): 95
Excellent

Enter performance score (0-100): 78
Good

Enter performance score (0-100): 60
Average

Enter performance score (0-100): 45
Poor

41. Check whether a number is divisible by 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
elif num % 5 == 0:
    print("Number is divisible by 5 only")
elif num % 11 == 0:
    print("Number is divisible by 11 only")
else:
    print("Number is not divisible by 5 or 11")

Enter a number: 55
Number is divisible by both 5 and 11

Enter a number: 25
Number is divisible by 5 only

Enter a number: 22
Number is divisible by 11 only

42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700 

age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

Enter age: 25
Enter salary: 30000
Enter credit score: 720
Eligible for loan

Enter age: 20
Enter salary: 40000
Enter credit score: 750
Not eligible for loan

Enter age: 30
Enter salary: 20000
Enter credit score: 710
Not eligible for loan

43. Validate login using username AND password.

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

Enter username: admin
Enter password: 12345
Login Successful

Enter username: admin
Enter password: 11111
Invalid Username or Password

Enter username: user
Enter password: 12345
Invalid Username or Password

44. Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

average = (sub1 + sub2 + sub3) / 3

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and average >= 50:
    print("Pass")
else:
    print("Fail")

Enter marks of Subject 1: 60
Enter marks of Subject 2: 55
Enter marks of Subject 3: 70
Pass

Enter marks of Subject 1: 45
Enter marks of Subject 2: 38
Enter marks of Subject 3: 80
Fail

Enter marks of Subject 1: 50
Enter marks of Subject 2: 50
Enter marks of Subject 3: 45
Fail

45. Check if a number lies between 10 and 100. 

num = int(input("Enter a number: "))

if 10 <= num <= 100:
    print("Number lies between 10 and 100")
else:
    print("Number does not lie between 10 and 100")

Enter a number: 25
Number lies between 10 and 100

Enter a number: 5
Number does not lie between 10 and 100

46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

attendance = float(input("Enter attendance percentage: "))
medical_certificate = input("Medical certificate available? (yes/no): ")

if attendance >= 75 or medical_certificate.lower() == "yes":
    print("Eligible for exam")
else:
    print("Not eligible for exam")

Enter attendance percentage: 80
Medical certificate available? (yes/no): no
Eligible for exam

Enter attendance percentage: 60
Medical certificate available? (yes/no): yes
Eligible for exam

Enter attendance percentage: 60
Medical certificate available? (yes/no): no
Not eligible for exam

47. Validate a date using conditions.

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid date")
elif day < 1:
    print("Invalid date")
elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
    print("Valid date")
elif month in [4, 6, 9, 11] and day <= 30:
    print("Valid date")
elif month == 2 and day <= 28:
    print("Valid date")
else:
    print("Invalid date")

Enter day: 15
Enter month: 8
Enter year: 2026
Valid date

Enter day: 31
Enter month: 4
Enter year: 2026
Invalid date

Enter day: 29
Enter month: 2
Enter year: 2026
Invalid date

48. Check whether an email format is valid.

email = input("Enter email: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")

    # Basic rules:
    # @ should not be at start
    # . should come after @
    # there should be characters between @ and .
    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print("Valid email format")
    else:
        print("Invalid email format")
else:
    print("Invalid email format")

Enter email: user@gmail.com
Valid email format

Enter email: user@gmail.com
Valid email format

Enter email: user.com
Invalid email format

49. Determine insurance eligibility using age, health status, and income. 

age = int(input("Enter age: "))
health = input("Health status (good/poor): ")
income = float(input("Enter annual income: "))

if age >= 18 and health.lower() == "good" and income >= 200000:
    print("Eligible for insurance")
else:
    print("Not eligible for insurance")

Enter age: 25
Health status (good/poor): good
Enter annual income: 300000
Eligible for insurance

Enter age: 17
Health status (good/poor): good
Enter annual income: 500000
Not eligible for insurance

Enter age: 30
Health status (good/poor): poor
Enter annual income: 400000
Not eligible for insurance

50. Check leap year using complete leap year logic. 

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

Enter a year: 2024
Leap Year

Enter a year: 1900
Not a Leap Year

Enter a year: 2000
Leap Year

51. Write a Python program to calculate income tax using slabs.

income = float(input("Enter annual income: "))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.2
else:
    tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3

print("Income Tax:", tax)

Enter annual income: 300000
Income Tax: 2500.0

Enter annual income: 750000
Income Tax: 62500.0

Enter annual income: 1200000
Income Tax: 172500.0

52. Create an ATM withdrawal program with balance checks.

balance = 10000  # initial balance

print("Current Balance:", balance)
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount!")
elif amount > balance:
    print("Insufficient balance!")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining Balance:", balance)

Current Balance: 10000
Enter withdrawal amount: 2000
Withdrawal successful
Remaining Balance: 8000.0

Current Balance: 10000
Enter withdrawal amount: 15000
Insufficient balance!

Current Balance: 10000
Enter withdrawal amount: -500
Invalid amount!

53. Check promotion eligibility using experience and performance. 

experience = int(input("Enter years of experience: "))
performance = input("Enter performance (good/average/poor): ")

if experience >= 5 and performance.lower() == "good":
    print("Eligible for Promotion")
elif experience >= 3 and performance.lower() == "good":
    print("Under Consideration for Promotion")
else:
    print("Not Eligible for Promotion")

Enter years of experience: 6
Enter performance (good/average/poor): good
Eligible for Promotion

Enter years of experience: 2
Enter performance (good/average/poor): average
Not Eligible for Promotion

Enter years of experience: 4
Enter performance (good/average/poor): good
Under Consideration for Promotion

54. Implement a grading system using nested if–else.

marks = float(input("Enter marks (0-100): "))

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade: A+")
    else:
        if marks >= 80:
            print("Grade: A")
        else:
            if marks >= 70:
                print("Grade: B")
            else:
                if marks >= 60:
                    print("Grade: C")
                else:
                    if marks >= 50:
                        print("Grade: D")
                    else:
                        print("Grade: F (Fail)")
else:
    print("Invalid marks!")

Enter marks (0-100): 92
Grade: A+

Enter marks (0-100): 75
Grade: B

Enter marks (0-100): 45
Grade: F (Fail)

55. Validate strong password using multiple conditions.

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Password must be at least 8 characters long")

Enter password: Abc@1234
Strong Password

Enter password: abc@1234
Weak Password

Enter password: ab@123
Password must be at least 8 characters long

56. Calculate delivery charges based on location and order amount. 

location = input("Enter location (local/outstation): ")
amount = float(input("Enter order amount: "))

if location.lower() == "local":
    if amount >= 500:
        charge = 0
    else:
        charge = 50
elif location.lower() == "outstation":
    if amount >= 1000:
        charge = 100
    else:
        charge = 200
else:
    print("Invalid location!")
    charge = None

if charge is not None:
    print("Delivery Charge:", charge)

Enter location (local/outstation): local
Enter order amount: 600
Delivery Charge: 0

Enter location (local/outstation): local
Enter order amount: 300
Delivery Charge: 50

Enter location (local/outstation): outstation
Enter order amount: 800
Delivery Charge: 200

57. Determine online exam qualification. 

attendance = float(input("Enter attendance percentage: "))
assignment_score = float(input("Enter assignment score (0-100): "))
fee_paid = input("Fee paid? (yes/no): ")

if attendance >= 75 and assignment_score >= 50 and fee_paid.lower() == "yes":
    print("Qualified for Online Exam")
else:
    print("Not Qualified for Online Exam")

Enter attendance percentage: 80
Enter assignment score (0-100): 65
Fee paid? (yes/no): yes
Qualified for Online Exam

Enter attendance percentage: 70
Enter assignment score (0-100): 80
Fee paid? (yes/no): yes
Not Qualified for Online Exam

Enter attendance percentage: 80
Enter assignment score (0-100): 40
Fee paid? (yes/no): no
Not Qualified for Online Exam

58. Create movie ticket pricing logic based on age & show time. 

age = int(input("Enter age: "))
time = input("Enter show time (morning/evening/night): ")

price = 0

if time.lower() == "morning":
    if age < 12:
        price = 100
    elif age <= 60:
        price = 150
    else:
        price = 120

elif time.lower() == "evening":
    if age < 12:
        price = 150
    elif age <= 60:
        price = 200
    else:
        price = 170

elif time.lower() == "night":
    if age < 12:
        price = 180
    elif age <= 60:
        price = 250
    else:
        price = 200
else:
    print("Invalid show time!")
    price = None

if price is not None:
    print("Ticket Price:", price)

Enter age: 10
Enter show time (morning/evening/night): evening
Ticket Price: 150

Enter age: 30 
Enter show time (morning/evening/night): night
Ticket Price: 250

Enter age: 70
Enter show time (morning/evening/night): morning
Ticket Price: 120

59. Determine bank account type based on balance. 

balance = float(input("Enter account balance: "))

if balance >= 100000:
    print("Premium Account")
elif balance >= 50000:
    print("Gold Account")
elif balance >= 10000:
    print("Silver Account")
elif balance >= 0:
    print("Basic Account")
else:
    print("Invalid balance!")

Enter account balance: 120000
Premium Account

Enter account balance: 60000
Gold Account

Enter account balance: 500
Basic Account

60. Create a menu-driven program using if–elif–else.# Menu-driven program

print("MENU")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)

elif choice == 2:
    print("Result:", num1 - num2)

elif choice == 3:
    print("Result:", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice!")

MENU
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 1
Enter first number: 10
Enter second number: 5
Result: 15.0

MENU
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 4
Enter first number: 20
Enter second number: 4
Result: 5.0

MENU
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 4
Enter first number: 10
Enter second number: 0
Cannot divide by zero
"""





