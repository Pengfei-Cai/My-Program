#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
chi = ['零','一','二','三','四','五','六','七','八','九']
num = input("请输入正整数：")

for lena in num:
    x = int(lena)
    print(chi[x],end='')
