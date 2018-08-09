# coding=utf-8
import random


#	************************************	#
#	首先选出list的第一个数，再取出第二个数和	#
#	第一个数比较，将第二个数“插入”第一个数前	#
#	后，再取出第三个数，将第三个数和前两个数	#
#	比较...依次将所有数都排好序。          	#
#	************************************	#


print('*' * 50)
a = [random.randint(0, 100) for x in range(10)]
print(a)
print('*' * 50)
for i in range(len(a)):
	temp = a[i]
	j = i + 1
    while i < len(a):
        if a[i] > a[i + 1]:
        	
