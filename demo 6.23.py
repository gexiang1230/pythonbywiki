# -*- coding: utf-8  -*-
def mySort(num):# 存储最小值
   newlist=[]
   while len(num)>0:
         newnum=min(num)
         index=num.index(min(num))
         newlist.append(newnum)
         num.pop(index)
   print newlist
number=[12,5,4,78,6,74,2,14]
mySort(number)