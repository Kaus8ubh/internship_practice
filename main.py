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

# arr1=[[23,48,92],[8,5,6]]
# arr2=[[40,2],[60,4],[60,6]]
# result=[[0,0],[0,0]]
# for i in range(len(arr1)):
#   for j in range(len(arr2[0])):
#     for k in range(len(arr2)):
#       result[i][j]+=arr1[i][k]*arr2[k][j]
# print(result)

# ones=["", "one", "two", "three", "four", "five", "six", "seven","eight", "nine"]
# teens=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# tens=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]
# def no_to_word(no):
#   if no==0:
#     return "zero"
#   word=""
#   if no >= 100000:
#     word += ones[no//100000] + " lakh "
#   no %= 100000
#   if (no//1000 >= 10 and no//1000 <= 19):
#     word += teens[no//1000] + " thousand "
#   if no >= 20000:
#     word += tens[no//10000]
#   no %= 10000
#   if no >= 1000:
#     word += ones[no//1000] + " thousand "
#   no%=1000
#   if no >= 100:
#     word += ones[no//100] + " hundred "
#   no%=100
#   if no >= 10 and no<=19:
#     word += teens[no-10]
#   if no >= 20:
#     word += tens[no//10] 
#   no%=10
#   if no>=0:
#     word += ones[no]

#   return word

# print(no_to_word(321967))


# class Tree:
#   def __init__(self, val=None):
#     self.value = val
#     if self.value:
#       self.left=Tree()
#       self.right=Tree()
#     else:
#       self.left = None
#       self.right = None

#   def is_empty(self):
#     return self.value == None

#   def insert(self, data):
#     if self.is_empty():
#       self.value = data
#       self.left=Tree()
#       self.right=Tree()
#       return

#     elif data > self.value:
#       self.right.insert(data)

#     elif data < self.value:
#       self.left.insert(data)

#     elif data == self.value:
#       return

# t=Tree(10)
# t.insert(5)
# t.insert(15)  
# t.insert(3)
# t.insert(7)
# t.insert(12)
# t.insert(18)
# t.insert(4)


# 

para="Geography is the study of places and the relationships between people and their environments. Geographers explore both the physical properties of Earth’s surface and the human societies spread across it. They also examine how human culture interacts with the natural environment and the way that locations and places can have an impact on people. Geography seeks to understand where things are found, why they are there, and how they develop and change over time.Ancient GeographersThe term geography was coined by the Greek scholar Eratosthenes in the third century B.C.E. In Greek, geo- means “earth” and -graphy means “to write.” Using geography, Eratosthenes and other Greeks developed an understanding of where their homeland was located in relation to other places, what their own and other places were like, and how people and environments were distributed. These concerns have been central to geography ever since.Of course, the Greeks  China. This period of time between the 15th and 17th centuries is known in the West as the Age of Exploration or the Age of Discovery.With the dawn of the Age of Discovery, the study of geography regained popularity in Europe. The invention of the printing press in the mid-1400s helped spread geographic knowledge by making maps and charts widely available. Improvements in shipbuilding and navigation facilitated more exploring, greatly improving the accuracy of maps and geographic information.Greater geographic understanding allowed European powers to extend their global influence. During the Age of Discovery, European nations established colonies around the world. Improved transportation, communication and navigational technology allowed countries such as the United Kihich nations trade with other nations, and what resources are exchanged. Philosophers analyze the responsibility people have to take care of Earth.Emergence of Modern GeographySome people have trouble understanding the complete scope of the discipline of geography because geography is interdisciplinary, meaning that it is not defined by one particular topic. Instead, geography is concerned with many different topics—people, culture, politics, settlements, plants, landforms and much more. Geography asks spatial questions—how and why things are distributed or arranged in particular ways on Earth’s surface. It looks at these differe"

def occurance_of_words(para):
  dict={}
  drops=["A","a","the","The","is","Is","of","Of","and",
         "And","to","To","in","In","for","For","on","are",
         "On","with","With","that","That","by","By","this","They","These"," "]
  words=para.split()
  for word in words:
    if word in drops:
      continue
    if word in dict:
      dict[word]+=1
    else:
      dict[word]=1
  return dict

print(occurance_of_words(para))