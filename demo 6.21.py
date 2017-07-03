# -*- coding: utf-8  -*-
import re  #根据多个分隔符进行切片
str1=raw_input("请输入学生姓名年龄信息:") #默认输入Jack Green ,   21  ;  Mike Mos,
str2=re.split(',|;|\n',str1)

for one in  range(0,len(str2)-1,2):
    print"{0:20}:{1:>02};".format(str2[one],str2[one+1])#{1:>02};  jack,15;tom,  15;  4,28;


# print  '{:010}'.format(56) 后面只能用数字，否则报错
