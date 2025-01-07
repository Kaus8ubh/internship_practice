# # print("hello wirld")
# Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."
# for i in range(1,51):
#     if i%3 == 0 and i%5 == 0:
#         print("fizzbuzz")
#     elif i%3 == 0:
#         print("fizz")
#     elif i%5 == 0:
#         print("buzz")
#     else:
#         print(i)

# 2. Palindrome Checker

# str=input("enter a string ")
# if str == str[::-1]:
#     print("it is a palindrome ")
# else:
#     print("it is not a palindrome")

# 3. Find the Largest Number

# list=[23,9,16298,3725,27241,8,9,0,1,2,3,4,5,6,7,8,9,0]
# print(max(list))

# # Count Vowels
# str=input(" ")
# vowels="aeiou"
# no_vovels=0
# for letter in str:
#     if letter in vowels:
#         no_vovels+=1
# print(no_vovels)

# Write a function to compute the factorial of a number using recursion.

# no=int(input())
# result=1
# for i in range (1,no+1):
#     result=result*i
# print( result)

# Write a program that computes the sum of all even numbers in a given list.
# list=[1, 2, 3, 4, 5, 6]
# add=0
# for num in list:
#   if num%2==0:
#     add=add+num
# print(add)

# Write a function that checks if a number is a prime number.
# no=int(input())
# is_prime=True
# for i in range(2,int(no**0.5)+1):
#     if no%i==0:
#       is_prime=False
#       break
# if is_prime:
#   print("it is a prime number")
# else:
#   print("it is not a prime number")


# Write a function that finds the missing number in an array of integers from 1 to n.
# 
# list=[1,2,3,5]
# for i in range(min(list),max(list)+1):
#     print(i,)

# Write a program that sorts a list of numbers in ascending order without using the built-in sort() method

# def bubble_sort(arr):
#   n=len(arr)
#   for i in range(n-1):
#     for j in range(n-i-1):
#       if arr[j]>arr[j+1]:
#         arr[j],arr[j+1]=arr[j+1],arr[j]
#   return arr

# numbers = [5, 2, 9, 1, 7]
# sorted_numbers = bubble_sort(numbers)
# print(f"Sorted list: {sorted_numbers}")

# Write a function to generate the first n Fibonacci numbers.



# sentense="This is a Python exam"
# words=sentense.split()
# print(len(words))

# def unique(numbers):
#   unique_no=[]
#   for no in numbers:
#     if no not in unique_no:
#       unique_no.append(no)
#   return unique_no

# numbers=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# print(unique(numbers))

# list=[1,2,3,4,5,6,7,8,9]
# print(list[::-1])

# def mergedlist(list1,list2):
#   merged_list=[]
#   i=0
#   j=0
#   while i<len(list1) and j<len(list2):
#     if list1[i]<=list2[j]:
#       merged_list.append(list1[i])
#       i+=1
#     else:
#       merged_list.append(list2[j])
#       j+=1
#   return merged_list

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# merged_list = mergedlist(list1, list2)
# print(f"Merged list: {merged_list}")

# def multiplicatiion(num):
#   for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# num=int(input("no...."))
# print(multiplicatiion(num))


# def decimal(no):
#   decimal=0
#   power=0
#   for digit in no[::-1]:
#     if digit=='1':
#       decimal+=2**power
#     power+=1
#   return decimal

# binary_string = "1010"
# decimal_number = decimal(binary_string)
# print(f"Binary string: {binary_string}")
# print(f"Decimal number: {decimal_number}")

# def count(list):
#   c=dict()
#   for item in list:
#     c[item]=c.get(item,0)+1
#   return c

# list=[1, 2, 2, 3, 3, 3]
# print(count(list))


#leapyear
# def is_leap(year):
#   if year%4==0:
#     if year%100==0:
#       if year%400==0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# year=2023
# print(is_leap(year))


# str="HellO wOrld"
# rank=[]
# i=0
# capitals="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for char in str:
#   if char in capitals:
#     rank.append(i)
#   i+=1
# print(rank)


# for i in range(2,101):
#   sum=0
#   for j in range(1,i):
#     if i%j==0:
#       sum+=j
#   if sum==i:
#     print(i)

arr1=[[23,48,92],[8,5,6]]
arr2=[[40,2],[60,4],[60,6]]
result=[[0,0],[0,0]]
for i in range(len(arr1)):
  for j in range(len(arr2[0])):
    for k in range(len(arr2)):
      result[i][j]+=arr1[i][k]*arr2[k][j]
print(result)