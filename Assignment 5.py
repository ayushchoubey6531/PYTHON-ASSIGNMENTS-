"""
1. Write a Python program to create a list of integers and print its elements.

numbers = [10, 20, 30, 40, 50]
print("Elements of the list are:")
for num in numbers:
    print(num)

OUTPUT
Elements of the list are:
10
20
30
40
50

2. Write a program to find the sum and average of all elements in a list.

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("List:", numbers)
print("Sum =", total)
print("Average =", average)

OUTPUT
List: [10, 20, 30, 40, 50]
Sum = 150
Average = 30.0

3. Write a program to find the largest and smallest element in a list.

numbers = [12, 45, 7, 89, 23, 5]
largest = max(numbers)
smallest = min(numbers)
print("List:", numbers)
print("Largest element =", largest)
print("Smallest element =", smallest)

OUTPUT
List: [12, 45, 7, 89, 23, 5]
Largest element = 89
Smallest element = 5

4. Write a Python program to count the number of elements in a list without using len().

numbers = [10, 20, 30, 40, 50]
count = 0
for num in numbers:
    count += 1
print("List:", numbers)
print("Number of elements in the list =", count)

OUTPUT
List: [10, 20, 30, 40, 50]
Number of elements in the list = 5

5. Write a program to reverse a list without using built-in functions.

numbers = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print("Original List:", numbers)
print("Reversed List:", reversed_list)

OUTPUT
Original List: [10, 20, 30, 40, 50]
Reversed List: [50, 40, 30, 20, 10]

6. Write a program to check if an element exists in a list.

numbers = [10, 20, 30, 40, 50]
element = int(input("Enter the element to search: "))
found = False
for num in numbers:
    if num == element:
        found = True
        break
if found:
    print(element, "exists in the list.")
else:
    print(element, "does not exist in the list.")

OUTPUT
Enter the element to search: 30
30 exists in the list.

7. Write a Python program to remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("Original List:", numbers)
print("List after removing duplicates:", unique_list)

OUTPUT
Original List: [10, 20, 30, 20, 40, 10, 50, 30]
List after removing duplicates: [10, 20, 30, 40, 50]

8. Write a program to sort a list in ascending and descending order.

numbers = [45, 12, 89, 23, 7, 56]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

OUTPUT
Original List: [45, 12, 89, 23, 7, 56]
Ascending Order: [7, 12, 23, 45, 56, 89]
Descending Order: [89, 56, 45, 23, 12, 7]

9.Write a program to merge two lists and remove duplicate.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1 + list2
unique_list = []
for item in merged_list:
    if item not in unique_list:
        unique_list.append(item)
print("Merged List:", merged_list)
print("List after removing duplicates:", unique_list)

OUTPUT
Merged List: [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
List after removing duplicates: [1, 2, 3, 4, 5, 6, 7, 8]

10. Write a program to find common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)

OUTPUT
List 1: [1, 2, 3, 4, 5]
List 2: [4, 5, 6, 7, 8]
Common elements: [4, 5]

11. Write a program to split a list into even and odd numbers

numbers = [10, 15, 22, 33, 40, 51, 64, 77]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Original List:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

OUTPUT
Original List: [10, 15, 22, 33, 40, 51, 64, 77]
Even Numbers: [10, 22, 40, 64]
Odd Numbers: [15, 33, 51, 77]

12. Write a program to rotate a list by n positions.

numbers = [10, 20, 30, 40, 50]
n = 2
rotated = numbers[n:] + numbers[:n]
print("Original List:", numbers)
print("Rotated List:", rotated)

OUTPUT
Original List: [10, 20, 30, 40, 50]
Rotated List: [30, 40, 50, 10, 20]

13. Write a Python program to find the second largest number in a list.

numbers = [10, 25, 45, 60, 35, 50]
largest = second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("List:", numbers)
print("Second Largest Number:", second_largest)

OUTPUT
List: [10, 25, 45, 60, 35, 50]
Second Largest Number: 50

14. Write a program to flatten a nested list.

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print("Nested List:", nested_list)
print("Flattened List:", flat_list)

OUTPUT
Nested List: [[1, 2], [3, 4], [5, 6]]
Flattened List: [1, 2, 3, 4, 5, 6]

15. Write a program to count frequency of each element in a list.

numbers = [10, 20, 10, 30, 20, 10, 40]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("List:", numbers)
print("Frequency of each element:")
for key in frequency:
    print(key, ":", frequency[key])

OUTPUT
List: [10, 20, 10, 30, 20, 10, 40]
Frequency of each element:
10 : 3
20 : 2
30 : 1
40 : 1

16. Write a program to replace all negative numbers with zero in a list.

numbers = [10, -5, 20, -8, 15, -3, 25]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print("Updated List:", numbers)

OUTPUT
Updated List: [10, 0, 20, 0, 15, 0, 25]

17. Write a program to remove all occurrences of a given element from a list.

numbers = [10, 20, 30, 20, 40, 20, 50]
element = 20
new_list = []
for num in numbers:
    if num != element:
        new_list.append(num)
print("Original List:", numbers)
print("Element to remove:", element)
print("Updated List:", new_list)

OUTPUT
Original List: [10, 20, 30, 20, 40, 20, 50]
Element to remove: 20
Updated List: [10, 30, 40, 50]

18. Write a program to check if a list is a palindrome.

numbers = [1, 2, 3, 2, 1]
if numbers == numbers[::-1]:
    print("The list is a Palindrome.")
else:
    print("The list is not a Palindrome.")

OUTPUT
The list is a Palindrome.

19. Write a Python program to find missing numbers in a given list of consecutive integers.

numbers = [1, 2, 4, 6, 7, 9]
missing = []
for i in range(numbers[0], numbers[-1] + 1):
    if i not in numbers:
        missing.append(i)
print("List:", numbers)
print("Missing Numbers:", missing)

OUTPUT
List: [1, 2, 4, 6, 7, 9]
Missing Numbers: [3, 5, 8]

20. Write a program to perform element-wise addition of two lists.

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print("List 1:", list1)
print("List 2:", list2)
print("Element-wise Addition:", result)

OUTPUT
List 1: [10, 20, 30, 40]
List 2: [1, 2, 3, 4]
Element-wise Addition: [11, 22, 33, 44]

21. Write a Python program to find the longest increasing subsequence in a list.

numbers = [10, 22, 9, 33, 21, 50, 41, 60]
lis = []
for num in numbers:
    if not lis or num > lis[-1]:
        lis.append(num)
print("List:", numbers)
print("Longest Increasing Subsequence:", lis)

OUTPUT
List: [10, 22, 9, 33, 21, 50, 41, 60]
Longest Increasing Subsequence: [10, 22, 33, 50, 60]

22. Write a program to group elements based on frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
grouped = {}
for key in frequency:
    freq = frequency[key]
    if freq not in grouped:
        grouped[freq] = []
    grouped[freq].append(key)
print("Original List:", numbers)
print("Grouped Elements Based on Frequency:")
for freq in grouped:
    print(freq, "time(s):", grouped[freq])

OUTPUT
Original List: [1, 2, 2, 3, 3, 3, 4, 4, 5]
Grouped Elements Based on Frequency:
1 time(s): [1, 5]
2 time(s): [2, 4]
3 time(s): [3]

23. Write a Python program to create a tuple and print its elements.

numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
print("Elements of the tuple:")
for i in numbers:
    print(i)

OUTPUT
Tuple: (10, 20, 30, 40, 50)
Elements of the tuple:
10
20
30
40
50

24. Write a program to find the length of a tuple.

numbers = (10, 20, 30, 40, 50)
length = len(numbers)
print("Tuple:", numbers)
print("Length of the tuple is:", length)

OUTPUT
Tuple: (10, 20, 30, 40, 50)
Length of the tuple is: 5

25. Write a program to find the maximum and minimum element in a tuple.

numbers = (10, 25, 5, 40, 15)
maximum = max(numbers)
minimum = min(numbers)
print("Tuple:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)

OUTPUT
Tuple: (10, 25, 5, 40, 15)
Maximum element: 40
Minimum element: 5

26. Write a program to convert a tuple into a list.

numbers = (10, 20, 30, 40, 50)
numbers_list = list(numbers)
print("Tuple:", numbers)
print("List:", numbers_list)

OUTPUT
Tuple: (10, 20, 30, 40, 50)
List: [10, 20, 30, 40, 50]

27. Write a program to check if an element exists in a tuple.

numbers = (10, 20, 30, 40, 50)
element = int(input("Enter the element to search: "))
if element in numbers:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")

OUTPUT
Enter the element to search: 30
Element exists in the tuple.

Enter the element to search: 60
Element does not exist in the tuple.

28. Write a program to count occurrences of an element in a tuple.

numbers = (10, 20, 30, 20, 40, 20, 50)
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print("Tuple:", numbers)
print("Occurrences of", element, "=", count)

OUTPUT
Enter the element to count: 20
Tuple: (10, 20, 30, 20, 40, 20, 50)
Occurrences of 20 = 3

Enter the element to count: 60
Tuple: (10, 20, 30, 20, 40, 20, 50)
Occurrences of 60 = 0

29. Write a program to slice a tuple and display the result.

numbers = (10, 20, 30, 40, 50, 60, 70)
sliced_tuple = numbers[1:5]
print("Original Tuple:", numbers)
print("Sliced Tuple:", sliced_tuple)

OUTPUT
Original Tuple: (10, 20, 30, 40, 50, 60, 70)
Sliced Tuple: (20, 30, 40, 50)

30. Write a program to find repeated elements in a tuple.

numbers = (10, 20, 30, 20, 40, 10, 50, 30)
repeated = []
for i in numbers:
    if numbers.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Tuple:", numbers)
print("Repeated elements:", repeated)

OUTPUT
Tuple: (10, 20, 30, 20, 40, 10, 50, 30)
Repeated elements: [10, 20, 30]

31. Write a program to merge two tuples.

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
merged_tuple = tuple1 + tuple2
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Merged Tuple:", merged_tuple)

OUTPUT
Tuple 1: (10, 20, 30)
Tuple 2: (40, 50, 60)
Merged Tuple: (10, 20, 30, 40, 50, 60)

32. Write a program to unpack elements of a tuple into variables.

numbers = (10, 20, 30)
a, b, c = numbers
print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)

OUTPUT
Value of a: 10
Value of b: 20
Value of c: 30

33. Write a Python program to sort a tuple.

numbers = (40, 10, 30, 20, 50)
sorted_tuple = tuple(sorted(numbers))
print("Original Tuple:", numbers)
print("Sorted Tuple:", sorted_tuple)

OUTPUT
Original Tuple: (40, 10, 30, 20, 50)
Sorted Tuple: (10, 20, 30, 40, 50)

34. Write a program to convert a list of tuples into a dictionary

data = [("A", 1), ("B", 2), ("C", 3), ("D", 4)]
dictionary = dict(data)
print("List of Tuples:", data)
print("Dictionary:", dictionary)

OUTPUT
List of Tuples: [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
Dictionary: {'A': 1, 'B': 2, 'C': 3, 'D': 4}

35. Write a program to find the index of an element in a tuple. 

numbers = (10, 20, 30, 40, 50)
element = int(input("Enter the element to find: "))
if element in numbers:
    index = numbers.index(element)
    print("Index of", element, "is:", index)
else:
    print("Element not found in the tuple.")

OUTPUT
Enter the element to find: 30
Index of 30 is: 2

Enter the element to find: 60
Element not found in the tuple.

36. Write a program to remove an element from a tuple (without directly modifying it).

numbers = (10, 20, 30, 40, 50)
element = int(input("Enter the element to remove: "))
new_tuple = tuple(i for i in numbers if i != element)
print("Original Tuple:", numbers)
print("New Tuple:", new_tuple)

OUTPUT
Enter the element to remove: 30
Original Tuple: (10, 20, 30, 40, 50)
New Tuple: (10, 20, 40, 50)

37. Write a program to find common elements between two tuples.

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
common = []
for i in tuple1:
    if i in tuple2:
        common.append(i)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common Elements:", common)

OUTPUT
Tuple 1: (10, 20, 30, 40, 50)
Tuple 2: (30, 40, 50, 60, 70)
Common Elements: [30, 40, 50]

38. Write a Python program to check if a tuple is a palindrome.

numbers = (1, 2, 3, 2, 1)
if numbers == numbers[::-1]:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")

OUTPUT
The tuple is a palindrome.

39. Write a program to find the element with maximum frequency in a tuple.

numbers = (10, 20, 30, 20, 40, 20, 50, 10)
max_element = numbers[0]
max_count = numbers.count(max_element)
for i in numbers:
    if numbers.count(i) > max_count:
        max_count = numbers.count(i)
        max_element = i
print("Tuple:", numbers)
print("Element with maximum frequency:", max_element)
print("Frequency:", max_count)

OUTPUT
Tuple: (10, 20, 30, 20, 40, 20, 50, 10)
Element with maximum frequency: 20
Frequency: 3

40. Write a program to create a nested tuple and access its elements.

nested_tuple = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
print("Nested Tuple:", nested_tuple)
print("First element of first tuple:", nested_tuple[0][0])
print("Second element of second tuple:", nested_tuple[1][1])
print("Third element of third tuple:", nested_tuple[2][2])

OUTPUT
Nested Tuple: ((10, 20, 30), (40, 50, 60), (70, 80, 90))
First element of first tuple: 10
Second element of second tuple: 50
Third element of third tuple: 90

"""


