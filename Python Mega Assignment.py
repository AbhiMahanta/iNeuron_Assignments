# ## Assignment Part-1

# Q1. Why do we call Python as a general purpose and high-level programming language?
# Ans: Python is general purpose programming language because its applicationj is not restricted to only one field.It can be used
#  in many fields like AI, ML, web programming, data automation , data analysis and many more. And it is a high level programming 
#  language because a high level programming language is that which is close to normal human language which makes it easy to 
#  understand to humans and easy to learn also

# Q2. Why is Python called a dynamically typed language?
# Ans: In python we do not need to mention the type of the variable during declaration like other programming language. Python will
# autometically assume the required type and assign required memory for the variable during run time.That is why python is called 
# dynamically typed language

# Q3. List some pros and cons of Python programming language?
# Ans: Pros: 
# 1. Easy to learn
# 2. As it is easy to lean and read it enhanced productivity
# 3. It has hugh community
# 4. It has a wide range of open source libreries
# 5. It has a vast area where it can be used
# 6. It is portable
# 
# Cons:
# 1. It is slower than other programming language because of its dynamically typed feature
# 2. It's memory consumption is high
# 3. Not suitable for mobile programming
# 4. As it is dynamically typed language its datatype can change anytime which can throw runtime error
# Q4. In what all domains can we use Python?
# ans: Data science, data engineering , ML , AI ,Application Development, automation, web programming etc

# # Q5. What are variable and how can we declare them?
# Ans: Variable is like a container which is used to hold data/values of different types. In python to create variable we do not
# # require to declare type of variable. When we assign any value to it pyhton will autometically determine the type of it.
# eg: int_var = 103
#     str_var = "Sample"

# Q6. How can we take an input from the user in Python?
# Ans: To take input from the user we need to use input function.
# eg: name = input("Please enter your name :")

# Q7. What is the default datatype of the value that has been taken as an input using input() function?
# Ans: string is the default datatype for the input function.

# Q8. What is type casting?
# ans: type casting is a process of converting one datatype to another based on requirement.
# eg: age = int(input("Enter your age :"))

# # Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
# Ans: we can take multiple input from the users using split method. If we dont specify separator type then by default space is 
# consider as separator
# name,job = input().split(',')
# print(name)
# print(job)

# Q10. What are keywords?
# ans:Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything but those 
# specific purposes. 

# Q11. Can we use keywords as a variable? Support your answer with reason.
# Ans: No we cannot use keyword as a variable in python because they are reserved for special predefined purpose for the compile.
# if we use keywords as variable then compiler will get confused and will throw error.

# # Q12. What is indentation? What's the use of indentaion in Python?
# Ans: Indentation is a process to define a scope of a block of a code. In other programming language normally {} is used to define
# scope of a section of a code but in python we need to use indentaion or 1 tab space to declare scope of the code.


# Q13. How can we throw some output in Python?
# Ans: with the help of print() function we can throw some output in python.

# # Q14. What are operators in Python?
# Ans: operators are some special symbols,words which are used to do some arithmetic and logical operations on variable and values.
# eg: sum = 10 + 12
# here '=' is assignment operator and '+' is arithmetic operator

# Q15. What is difference between / and // operators?
# # ans: / is float division operator and // is integer division operator.
# print(10/3) #output  3.3333333333333335
# print(10//3)#output  3

# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
#
# Ans: ```
# print("iNeuron"*4)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
# Ans:
# inputed_num = int(input("Please enter a number: "))

# if inputed_num % 2==0 :
#     print("THe number is even")
# else:
#     print("THe number is odd")

# Q18. What are boolean operator?
# ans: Boolean operator return results either in true or false. and, or, not are 3 boolean operators in python

# Q19. What will the output of the following?
# ```
# Ans: 
# 1 or 0 = 1
# 0 and 0 = 0
# True and False and True = False
# 1 or 0 or 0 = 1
# ```

# # Q20. What are conditional statements in Python?
# Ans: conditional statements used to run a specific block of code when it satisfy a certain condition. For this we use 1f , elif and
# else 

# Q21. What is use of 'if', 'elif' and 'else' keywords?
# ans: if we have multiple conditions then we first start the conditions with 'if' statement then for following condtions we use
# elif statement and for all the conditions other than if and elif we use else statement.


# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
# age = int(input("Enter your age: "))
# if age >= 18 : 
#     print("I can vote")
# else:
#     print("I can't vote")


# # Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# ANS:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# sum = 0
# for i in numbers:
#     if(i%2 == 0):
#         sum = sum + i
# print(sum)


# # Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# Ans:
# no_1,no_2,no_3 = map(int13 14 1, input("Enter 3 no :").split())
# large = 0
# if no_1>no_2 : 
#     if no_1 > no_3:
#         large = no_1
#     else:
#         large = no_3
# elif no_2 > no_3:
#     large = no_2
# else:
#     large = no_3
# print("Largest no is :",large)


# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# Ans:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i % 5 == 0:
#         if i > 500 :
#             break
#         if i > 150:
#             continue
#         print(i)



# Q26. What is a string? How can we declare string in Python?
# Ans:
#  Strings are arrays of bytes representing Unicode characters.
#  eg: str1 = "Python"

# Q27. How can we access the string using its index?
# Ans:
# We can access string folloing ways: 1> string[index_no] 2>using for loop
# st1= "Python"
# print(st1[1])
# for i in st1:
#     print(i)


# Q28. Write a code to get the desired output of the following
# ```
# string = "Big Data iNeuron"
# desired_output = "iNeuron"
# ```
# Ans:
# string = "Big Data iNeuron"
# print("desired_output = ",string[9:])


# Q29. Write a code to get the desired output of the following
# ```
# string = "Big Data iNeuron"
# desired_output = "norueNi"
# ```
# # Ans:
# string = "Big Data iNeuron"
# print("desired_output = ",string[9:][::-1])

# Q30. Resverse the string given in the above question.
# # Ans:
# string = "Big Data iNeuron"
# print(string[::-1])


# Q31. How can you delete entire string at once?

# # Q32. What is escape sequence?
# Ans: If we want to use some special charecter inside a string we can do this with the help of escape sequence. To achieve this we just need to
# put a '\' before the charecter.
# eg: print("C:\\Desktop\\Game\\GTA")

# Q33. How can you print the below string?
# ```
# 'iNeuron's Big Data Course'
# ```
# Ans:
# print("'iNeuron's Big Data Course'")

# Q34. What is a list in Python?
# Ans: List is a mutable collection data type which is used to store multiple data either of same type or different types

# Q35. How can you create a list in Python?
# ans: We can create list either by [] or using list function. Below are the examples
# list1 = [1,2,"Python",4]
# print(list1)
# tup1=(5,6,"Program",10)
# list2 = list(tup1)
# print(list2)

# Q36. How can we access the elements in a list?
# ans: 
# we can access elements of a list either by index or for loop


# Q37. Write a code to access the word "iNeuron" from the given list.
# ```
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# ``` 
# ans:
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# print(lst[4][2])

# Q38. Take a list as an input from the user and find the length of the list.
# # Ans: 
# inputed_list = input("Please enter some item followed by space to create a list :").split()
# print(len(inputed_list))


# Q39. Add the word "Big" in the 3rd index of the given list.
# ```
# lst = ["Welcome", "to", "Data", "course"]
# ```
# Ans:
# lst = ["Welcome", "to", "Data", "course"]
# lst[2]="Big"
# print(lst)


# Q40. What is a tuple? How is it different from list?
# Ans:  Tuple is a collection datatype that can store multiple values of either same of different types in a single variable.
# () is used to create tuple variable. It is ordered and immutable where is list is immutable
# # eg: 
# tup1 = ("Ram", "Shayam",50,[40,9,"School"]) 
# print(tup1[3][2])#accessing tuple elements


# Q41. How can you create a tuple in Python?
# ans: We can create a tuple in the folloing way
# stuple1 = (1, 3, 4, 'test', 'red')

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
# Ans: We cannot add any element in tuple as tuple is immutable. 
# to add element in tuple first change it to list and add the require elements and change it back to tuple


# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
# tup1 = ("Ram", "Shayam",50,[40,9,"School"]) 
# stuple1 = (1, 3, 4, 'test', 'red')
# appended_tup = tup1 + stuple1
# print(appended_tup)
# print(sum((tup1,stuple1),()))


# # Q44. Take a tuple as an input and print the count of elements in it.
# Ans:inputed_tuple = tuple(input("Please enter some item followed by space to create a tuple :").split())
# print(len(inputed_tuple))

# Q45. What are sets in Python?
# Ans:  Set is collection data type which hold unordered, unindexed, unchangable, distinct values. 

# Q46. How can you create a set?
# Ans : We can define set either by {} or by passing an iterable to the set method.
# eg:
# set1 = {1,2,4,5,6}
# print(type(set1))
# list2 = [5,3,4,5]
# set2 = set(list2)
# print(type(set2))


# Q47. Create a set and add "iNeuron" in your set.
# Ans:
# set1 = {"Welcome","To"}
# set1.add("iNeuron")
# print(set1)

# Q48. Try to add multiple values using add() function.
# Ans: we cannot add multiple values using add() in set. add() is used to add only 1 element in the set. 

# Q49. How is update() different from add()?
# Ans: If we have 1 element to add in the set for that purpose we can use add() method. If we have some iterable like list, tuple,
# dictionary, set etc then in that senario we need to use update method().


# Q50. What is clear() in sets?
# Ans: It will remove all items from the set and create an empty set. 

# Q51. What is frozen set?
# ans: Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, 
# elements of the frozen set remain the same after creation.
# # eg:
# numbers2 = [1,2,3,4,5,7,8,9]
# frozen_set2 =frozenset(numbers2)


# Q52. How is frozen set different from set?
# ans: There are no methods like add,update, remove for frozenset like set

# Q53. What is union() in sets? Explain via code.
# Ans: if we have multiple sets union will merge those sets with the distinct values in those sets. 
# set1 = {1,2,3,4}
# set2 = {2,3,6,7}
# set3 = {11,2,6,12}
# set5=set1.union(set2).union(set3)
# print(set5)
# set4 = set1|set2|set3
# print(set4)

# Q54. What is intersection() in sets? Explain via code.
# Ans: if we have multiple sets intersection will merge those sets with the common values in those set. 
# set1 = {1,2,3,4}
# set2 = {2,3,6,7}
# set3 = {11,2,6,3,12}
# set4 = set1 & set2 & set3
# print(set4)
# set5 = set1.intersection(set2).intersection(set3)
# print(set5)

# Q55. What is dictionary ibn Python?
# Ans: Dictionary is a collection data type, which hold value in  the form of key value pair and uses {}.
# eg: cars = {
#             "Model":"Tata",
#             "Model_year": "2022",
#             "type":"Sedan",
#             "safety":5
# }


# Q56. How is dictionary different from all other data structures.
# Ans: 1. It uses key value pair to store data
#     2. It is mutable i.e we can change its data.
#     3. Keys must be unique. And it is used to access value of a dictionary
#     4. values can be duplicate
#     5. It is not ordered as list, tuple
#     6. It cannot be reversed as List as it is a key value pair

# Q57. How can we delare a dictionary in Python?
# Ans: we can create dictionary using {},dict() function and fromkeys() method.
# # eg: 
# dict1 = {'key1':'val1','key2':'val2'}
# dict2 = dict({'key1':'val1','key2':'val2'})
# fkeys = {'a','b','c'}
# fkey_value = '10'
# dict3 = dict.fromkeys(fkeys,fkey_value)
# print(dict1,dict2,dict3)

# Q58. What will the output of the following?
# ```
# var = {}
# print(type(var))
# # ```
# Ans: It will print type of the variable


# Q59. How can we add an element in a dictionary?
# Ans: we can add new element in the dictionary in the following way
# dict_1['new_key']= 'New Value'

# Q60. Create a dictionary and access all the values in that dictionary.
# ans: 
# cars = {
#             "Model":"Tata",
#             "Model_year": "2022",
#             "type":"Sedan",
#             "safety":5
# }
# for k,v in cars.items():
#     print("Key is ",k," And Value is ",v)


# Q61. Create a nested dictionary and access all the element in the inner dictionary.
# Ans:
# mother_dic ={
#     'child_dic_1' : {
#         'key1' : 'val1',
#         'key2' : 'val2'
#     },
#     'child_dic_2' : {
#         'key3' : 'val3',
#         'key4' : 'val4'
#     }
# }
# print(mother_dic['child_dic_2' ])


# Q62. What is the use of get() function?
# Ans: Python get method return the value of the given key if present in dictionary. If no value present in the dictionary it will
# return none.

# Q63. What is the use of items() function?
# ans: items() returns dictionary items as a view object with set of tuple as key value pairs in a list.

# Q64. What is the use of pop() function?
# Ans: pop() method removes the specified item form the dictionary and return the value of the spaecified item(key).

# Q65. What is the use of popitems() function?
# Ans: popitems() removes the last inserted key value pair from the dictionary and return it as a tuple.

# Q66. What is the use of keys() function?
# Ans: keys() object return a view objects that contains list of all keys in a dictionary in the same order as they were present in
# the dictionary.

# Q67. What is the use of values() function?
# Ans: values() object return a view objects that contains list of all values in a dictionary in the same order as they were present in
# the dictionary.

# Q68. What are loops in Python?
# Ans: If any task is required to be done multiple repeatative times then in that senario we use loop.

# Q69. How many type of loop are there in Python?
# Ans: In python there are 2 types of loops 1. for loop 2. while loop

# Q70. What is the difference between for and while loops?
# ans: for loop is suitable if we know exactly how many times a loop is going to execute. Whereas if we are not sure about no of
# times the loop will run in that senario while loop can be used. Then the while loop keeps on running until the given condition 
# is met.

# Q71. What is the use of continue statement?
# Ans: During looping if the program comes accross continue statement it will simply skip rest of code within the scope and check for 
# next item in the loop.

# Q72. What is the use of break statement?
# Ans: During looping if the program comes accross break statement it will simply stop the loop there and come out of the scope to
# run next line of code outside of the loop.

# Q73. What is the use of pass statement?
# Ans: After any condition or funtion declaration if the content of that section is empty then we can use pass statement to avoid 
# error reportin1g by the function

# # Q74. What is the use of range() function?
# Ans: A range function creates a sequence of numbers starting from 0 by default till n-1. If interval not mentioned explicitly then
# it will increment by 1

# Q75. How can you loop over a dictionary?
# Ans: we can loop throught items using for loop.
# eg:
# dict1 = {"Name":"Abhi", "Roll":"SPE","Company":"xyz"}
# for k,v in dict1.items():
#     print(k,v)


# ### Coding problems
# Q76. Write a Python program to find the factorial of a given number.
# Ans:
# user_input = int(input("Enter a no : "))
# fact = 1
# for i in range(1,user_input+1):
#     fact = fact*i
# print(f"Factorial of {user_input} is",fact)


# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100
# Ans:
# principal = float(input("Enter Pricipal :"))
# rate = float(input("Enter Rate :"))
# time = float(input("Enter Time :"))
# simple_interest = (principal*rate*time)/100
# print("Interest is ",simple_interest)


# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
# Ans:
# amount = 0
# principal = int(input("ENter Principal : "))
# time = int(input("Enter time : "))
# interest = int(input("Enter Interest :"))
# 
# amount = principal * pow((1+(interest/100)), time)
# print("Compound interst is : ",round(amount,2))



# Q79. Write a Python program to check if a number is prime or not.
# Ans:
# inputed_no = int(input("Please enter a no: "))
# count = 0
# 
# for i in range(1,inputed_no+1):
#     if i == 1 or i == inputed_no:
#         continue
#     elif inputed_no % i==0:
#         count = count + 1
# 
# if count > 0:
#     print("Not Prime")
# else:
#     print("Prime No")


# Q80. Write a Python program to check Armstrong Number.
# Ans:
# inputed_no = input("Please enter a no: ")
# arm = 0
# for i in inputed_no:
#     i_no = int(i)
#     arm = arm + (i_no*i_no*i_no)

# if arm == int(inputed_no):
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
    

# Q81. Write a Python program to find the n-th Fibonacci Number.
# Ans:
# usr_int = int(input("value of Nth fibo no :"))
# fb_no = 1
# fb_no_2 = 2
# if usr_int == 1 or usr_int == 2 :
#     print("Fibonacci no is : ",fb_no)
# elif usr_int == 3:
#     print("Fibonacci no is :",fb_no_2)
# else:
#     for i in range(4,usr_int+1):
#         tmp = fb_no_2
#         fb_no_2 = fb_no + fb_no_2
#         fb_no = tmp
# print("Fibo no is ",fb_no_2)

# # Q82. Write a Python program to interchange the first and last element in a list.
# list_ele = ["Start" ,19,22,10,256,245,1,85,"End"]
# list_ele[0],list_ele[len(list_ele)-1] = list_ele[len(list_ele)-1],list_ele[0]
# print(list_ele)


# Q83. Write a Python program to swap two elements in a list.
# list_no = [50 ,19,22,10]
# list_no[0],list_no[2]=list_no[2],list_no[0]
# print(list_no)

# Q84. Write a Python program to find N largest element from a list.
# Ans:
# list_no = [50 ,19,22,10,256,245,1,85]
# new_list_no = sorted(list_no,reverse = True)
# usr_inp_no = int(input("Which largerst element you want? Ans: "))
# print(new_list_no[usr_inp_no-1])


# Q85. Write a Python program to find cumulative sum of a list.
# Ans:
# list_no = [50 ,19,22,10]
# sum = 0
# for i in list_no:
#     sum = sum +i
# print(sum)


# # Q86. Write a Python program to check if a string is palindrome or not.
# # Ans:
# inp_str = input()
# rev_str = inp_str[::-1]
# print("The given string is Palindrome " if inp_str == rev_str else "The given string is Not Palindrome ")


# Q87. Write a Python program to remove i'th element from a string.
# Ans:
# str1 = "Python Programming"
# new_str = ""
# print(str1)
# element_to_remove = int(input("Enter position of the charecter :"))
# for i in range(len(str1)):
#     if i == (element_to_remove -1):
#         continue
#     else:
#         new_str = new_str + str1[i]
# print(new_str)


# Q88. Write a Python program to check if a substring is present in a given string.
# Ans: 
# str1 = "Python Programming Language"
# str2 = "Programming"
# print(True if str2 in str1 else False)

# Q89. Write a Python program to find words which are greater than given length k.
# Ans: Not able to understand question properly

# Q90. Write a Python program to extract unquire dictionary values.
# Ans: Not able to understand question properly

# Q91. Write a Python program to merge two dictionary.
# Ans:
# dic1 = {'a':1,'b':2}
# dic2 = {'c':3,'d':4}
# merge_dic = dic1
# for k,v in dic2.items():
#     merge_dic[k]=v
# print(merge_dic)


# Q92. Write a Python program to convert a list of tuples into dictionary.
# ```
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# ```
# Ans:
# list_tup = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# dic_final={}
# for i in list_tup:    
#     dic_final[i[0]]=i[1]
# print(dic_final)



# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
# ```
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
# ```
# Ans:
# list1 = [9, 5, 6]
# list_final=[]
# 
# for i in list1:
#     tup1 = (i,i*i*i)
#     list_final.append(tup1)
# 
# print(list_final)

# Q94. Write a Python program to get all combinations of 2 tuples.
# ```
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# Ans: ```
# test_tuple1 = (7, 2)
# test_tuple2 = (7, 8)
# list1=[]
# for i in test_tuple1:
#     for j in test_tuple2:
#         tup=(i,j)
#         list1.append(tup)
# 
# for i in test_tuple2:
#     for j in test_tuple1:
#         tup=(i,j)
#         list1.append(tup) 
# 
# print(list1)


# Q95. Write a Python program to sort a list of tuples by second item.
# ```
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# ```
# ans:
# list1 = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# list1.sort(key=lambda x:x[1])
# print(list1)

# Q96. Write a python program to print below pattern.
# ```
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# ```
# Ans:
# for i in range(1,6):
#     print('* '*i)


# Q97. Write a python program to print below pattern.
# ```
#     *
#    **
#   ***
#  ****
# *****
# ```
# Ans:
# ko=1
# for i in range(5,0,-1):
#     print(' '*i,end=" ")
#     for k in range(1,ko+1):
#         print("*",end="")
#     ko=ko+1
#     print("\n")

    
# Q98. Write a python program to print below pattern.
# ```
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# ```
# Ans:
# ko=1
# for i in range(5,0,-1):
#     print(' '*i,end=" ")
#     for k in range(1,ko+1):
#         print("* ",end="")
#     ko=ko+1
#     print("\n")


# Q99. Write a python program to print below pattern.
# ```
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# Ans:
# ```
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\n")


# Q100. Write a python program to print below pattern.
# ```
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# ```
# 
# str1="ABCDE"
# for i in str1:
#     print(f"{i} "*(str1.index(i)+1),end=" ")
#     print("\n")

    
