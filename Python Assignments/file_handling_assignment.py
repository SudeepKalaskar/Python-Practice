# 1.find no of characters, no  of words or number of lines in Python text file.
# Number of characters
# f=open('demo.txt','r')
# ch_no=len(f.read())
# print("Number of char. are:",ch_no)
# f.close()


# Number of words
# f=open('demo.txt','r')
# w_no=len(f.read().split())
# print("Number of words are:",w_no)
#f.close()

# Number of lines
# f=open('demo.txt','r')
# line_no=len(f.readlines())
# print('Number of lines are:',line_no)
#f.close()

# 2.Write a program to Count the number of upper-case alphabets present in a text file “PYTHON.TXT”.
# Ex: We Learn Python.   3 isupper()
# for creating a file namely python.txt and write something inside it, we have to write this code
# p=open('python.txt','w')
# p.writelines(['Hello All\n','We\n','Are\n','Learning PYthon'])

#type 1
# p1=open('python.txt','r')
# p2=p1.read()
# upper=0
# for i in p2:
#     if i.isupper():
#         upper+=1
# print("The number of upper-case alphabets are:",upper)
# p1.close()

# type 2 using function
# def uppercase_count():
#     p1 = open('python.txt', 'r')
#     p2 = p1.read()
#     upper = 0
#     for i in p2:
#         if i.isupper():
#             upper += 1
#     print("The number of upper-case alphabets are:", upper)
#     p1.close()
# uppercase_count()


# 3.A text file “PYTHON.TXT” contains alphanumeric text. Write a program that reads this text file
# and writes to another file “PYTHON1.TXT” entire file except the numbers or digits in the file.
# f_r=open('python.txt','r')
# f_w=open('python1.txt','w')
# new=f_r.read()
# for i in new:
#     if i.isdigit()==False:
#         print(i,end=' ')
#         f_w.write(i)
# f_r.close()
# f_w.close()

# 4.Write a program to count the words “to” and “the” present in a text file “python.txt”.
# total=0
# s=open('python.txt','r')
# word_count=s.read().split()
# for i in word_count:
#     if i=='to'or i=='the' or i=='To' or i=='The'or i=='TO'or i=='THE':
#         total=total+1
#     else:
#         pass
# print("count of 'to' and 'the' is:",total)
# s.close()

# 5.Write a program to display all the lines in a file “python.txt” along with line/record number.
# file_h=open('python.txt','r')
# total=0
# line_count=file_h.readlines()
# for j in line_count:
#     total=total+1
#     print(total,j)
# file_h.close()


