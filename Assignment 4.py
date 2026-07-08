"""
1. Print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1
OUPUT
1
2
3
4
5
6
7
8
9
10

2. Print even numbers from 1 to 20.

i = 2
while i <= 20:
    print(i)
    i += 2
OUTPUT
2
4
6
8
10
12
14
16
18
20

3.Print odd numbers from 1 to 20

i = 1
while i <= 20:
    print(i)
    i += 2
OUTPUT
1
3
5
7
9
11
13
15
17
19

4.Print numbers from 10 to 1 in reverse order

i = 10
while i >= 1:
    print(i)
    i -= 1
OUTPUT
10
9
8
7
6
5
4
3
2
1

5.Print multiplication table of 5 using while loop

i = 1
while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1
OUTPUT
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6.Find the sum of first 10 natural numbers using while loop

i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i += 1
print("Sum =", sum)

OUTPUT->Sum = 55

7.Find factorial of a number entered by the user

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i += 1
print("Factorial =", fact)

OUTPUT
Enter a number: 5
Factorial = 120

8.Count the number of digits in a given number

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits =", count)

OUTPUT
Enter a number: 12345
Number of digits = 5

9.Reverse a number using while loop

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number =", reverse)

OUTPUT
Enter a number: 12345
Reversed number = 54321

10. Check whether a number is palindrome or not using while loop

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

OUTPUT
Enter a number: 121
Palindrome Number

11.Print pattern:
*
**
***
****
*****

i = 1

while i <= 5:
    print("*" * i)
    i += 1
    
OUTPUT
*
**
***
****
*****

12. Print pattern:

1
12
123
1234
12345

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
    
OUTPUT
1
12
123
1234
12345

13.Ask the user to enter the password until the correct password is entered

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Login Successful!")

OUTPUT
Enter password: abc
Enter password: 123
Enter password: python123
Login Successful!

14.Create a number guessing game:
• Generate a random number (1–10)
• Keep asking user until they guess correctly

import random

secret_number = random.randint(1, 10)

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Wrong guess! Try again.")
        
OUTPUT->
Guess a number between 1 and 10: 3
Wrong guess! Try again.
Guess a number between 1 and 10: 7
Wrong guess! Try again.
Guess a number between 1 and 10: 5
Wrong guess! Try again.
Guess a number between 1 and 10: 4
Congratulations! You guessed the correct number.

15.Keep taking input numbers until user enters 0, then print total sum.

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    total = total + num

print("Total Sum =", total)

OUTPUT
Enter a number (0 to stop): 10
Enter a number (0 to stop): 20
Enter a number (0 to stop): 5
Enter a number (0 to stop): 0
Total Sum = 35

16. Print Fibonacci series up to N terms using while loop.

n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

OUTPUT
Enter the number of terms: 7
0 1 1 2 3 5 8

17. Check whether a number is Armstrong number.

num = int(input("Enter a number: "))
original = num
sum = 0

digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + (digit ** digits)
    num = num // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

OUTPUT
Enter a number: 153
Armstrong Number

18. Print prime numbers between 1 to 50 using while loop.

num = 2

while num <= 50:
    i = 2
    prime = True

    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(num, end=" ")

    num += 1

OUTPUT->2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

"""




