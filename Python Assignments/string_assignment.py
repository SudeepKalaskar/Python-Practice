# #1.Write a program to print your entered name in reverse order.
# name=input("Enter your first name:")
# print(name[::-1])
#
# #2.Write a program to print every third character of entered string.
# #type 1
# s = 'psdywwtddhqqoppn'
# print(s[0],s[3],s[6],s[9],s[12],s[15])
# # using slicing
# print("Every third character", s[0::3])
#
# #type 2 using for loop and slicing
# for i in s[0::3]:
#      print(i)
#
# #3.Write a program to find the number of characters present in string without using len()
# str="sudeepkalaskar"
# c=0
# for i in str:
#      c+=1
# print(c)
#
# #type 2
# l= input("Enter any string:")
# c=0
# for i in l:
#      c+=1
# print(c)
#
#
#
# #4.Write a program to print the number of vowels present in entered string.
# str1 = input("Enter any string:")
# c=0
# for j in str1:
#      if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
#          c += 1
#      else:
#         pass
# if c==0:
#      print('Number of vowel in entered string is 0')
# else:
#      print('Total number of vowels is', c)


#5.Write a program to find a character present in string or not?
#if present, in which index it is present .and how many times it is present.
str2 = input("Enter any string:")
char = input("Enter the character you want to check:")
if char in str2:
     print("Yes, it's present")
else:
     print("No,it's not present")
print(str2.index(char))
print(str2.count(char))
