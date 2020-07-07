#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import  time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()#计时
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    dur =  time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')#3.0f输出前三位整数
    time.sleep(0.1)
print("执行结束".center(scale//2,"-"))