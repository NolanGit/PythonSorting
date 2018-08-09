# coding=utf-8
import random


#	************************************	#
#	每次比较两个元素，第一层循环次数为需要归	#
#	位的元素个数，第二次循环可以使一个元素归	#
#	位，因为每一次第二层循环都使得一个元素归	#
#	位完成，所以每次可以少循环一次。        	#
#	************************************	#


print('*' * 50)
a = [random.randint(0, 100) for x in range(10)]
print(a)
print('*' * 50)
for i in range(len(a)):
    for y in range(len(a) - i - 1):
        if a[y] > a[y + 1]:
            a[y], a[y + 1] = a[y + 1], a[y]
print(a)
print('*' * 50)
