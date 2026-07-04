"""
1.Use a for loop to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)
    
OUTPUT
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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

2.Print all even numbers between 1 and 20.

for i in range(2, 21, 2):
    print(i)

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

3.Print the sum of numbers from 1 to 10 using a for loop.

sum = 0

for i in range(1, 11):
    sum += i
    
print("Sum =", sum)

OUTPUT -> 55

4. Take a number from the user and print its multiplication table up to 10. 

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

Enter a number: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

5.Take a string and count the total number of characters using a for loop.

text = input("Enter a string: ")

count = 0

for char in text:
    count += 1
print("Total number of characters =", count)

Enter a string: HELLO PYHTON
Total number of characters = 12

6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.

for i in range(1, 11):
    if i == 5:
        break
    print(i)

OUTPUT
1
2
3
4

7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop. 

numbers = [10, 15, 20, 25, 30, 35]

for num in numbers:
    if num == 25:
        print("Found")
        break
OUTPUT -> Found

8.Given a list of numbers, print the first negative number and stop the loop. 

numbers = [10, 25, 8, -4, -7, 15]

for num in numbers:
    if num < 0:
        print("First negative number:", num)
        break
First negative number: -4

9. Print numbers from 1 to 10. 
Skip number 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

OUTPUT
1
2
3
4
6
7
8
9
10

10.Print numbers from 1 to 20. 
Skip all even numbers

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
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

11.Print each character of the string "PYTHON". 
Skip the letter "O".

text = "PYTHON"

for ch in text:
    if ch == "O":
        continue
    print(ch)
OUTPUT
P
Y
T
H
N

12.Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1, 6):
    pass

print("Loop completed.")

OUTPUT-> Loop completed.

13.Loop from 1 to 10. 
If number is 6, just use pass.

for i in range(1, 11):
    if i == 6:
        pass
    print(i)
OUTPUT
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

14. Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 100:
        print("Found")
        break
else:
    print("Not Found")

OUTPUT-> Not Found

# numbers = [10, 20, 100, 40, 50]

for num in numbers:
    if num == 100:
        print("Found")
        break
else:
    print("Not Found")

OUTPUT-> Found

15.Take a number from the user and check whether it is prime using for-else. 

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

Enter a number: 7
7 is a prime number.

Enter a number: 12
12 is not a prime number.

16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

for i in range(1, 6):
    print("*" * i)
OUTPUT
*
**
***
****
*****

17.Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
*

for i in range(5, 0, -1):
    print("*" * i)
OUTPUT
*****
****
***
**
*

18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
OUTPUT
1
12
123
1234
12345

19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555

for i in range(1, 6):
    print(str(i) * i)
OUTPUT
1
22
333
4444
55555

20. Pyramid Pattern 
Print: 
    * 
   ***
  ***** 
 ******* 
*********

       n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
OUTPUT
    *
   ***
  *****
 *******
*********

21.Inverted Pyramid 
Print: 
********* 
 ******* 
  ***** 
   ***
    *
    
         n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
OUTPUT
*********
 *******
  *****
   ***
    *

22.Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.

for i in range(1, 6):
    if i == 4:
        break
    print("*" * i)
OUTPUT
*
**
***

"""




