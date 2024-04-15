"""s1={"monday","tuesday","monday","friday"}
print(type(s1))
print(s1)
if "monday" in s1:
    print("yes")
else:
    print("no")
for t in s1:
    print(t)"""
#print(s1[2])

"""s1={"monday","tuesday","friday"}
print(s1)
#s1.add("wednesday")
#s1.update({'saturday','tuesday','sunday'})
#s1.remove('friday')
s1.clear()
print(s1)"""

#set operations
"""s1={45,89,23,18,79,45}
s2={45,79,900,800,600}
#union operation
#s3=s1|s2 (union operator | used to combine 2 values can be done by union function or union operator)
#s3=s1.union(s2)
#print(s3)"""

#difference operator(it determines the values which are similar with s1-s2)
"""s1={45,89,23,18,79,45}
s2={45,79,900,800,600}
#s3=s1-s2
#s3=s1.difference(s2)
print(s3)"""

#intersection operator (to find the common value)
"""s1={45,89,23,18,79,45}
s2={45,79,900,800,600}
#s3=s1&s2
s3=s1.intersection(s2)
print(s3)"""

#symmetric difference (it ignores common values)
"""s1={45,89,23,18,79,45}
s2={45,79,900,800,600}
#s3=s1^s2
s3=s1.symmetric_difference(s2)
print(s3)"""















