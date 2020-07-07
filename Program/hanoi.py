#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
count = 0
def hanot(n,src,dst,mid):
    global count        #基例
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:               #链条
        hanot(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanot(n-1,mid,dst,src)
hanot(3,'A','C','B')
print(count)