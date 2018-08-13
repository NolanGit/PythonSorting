# coding=utf-8
import random


#	************************************	#
#	希尔排序属于插入排序的扩展	#
#	第一个数比较，将第一个数“插入”第零个数前	#
#	后，再取出第二个数，将第三个数和前两个数	#
#	比较...依次将所有数都排好序。          	#
#	************************************	#


print('*' * 50)
a = [random.randint(0, 100) for x in range(10)]
print(a)
print('*' * 50)
step = 0
while step <= len(a) / 3:
    step = step * 3 + 1
print(step)
while step >= 1:
    for i in range(step, len(a)):
        temp = a[i]
