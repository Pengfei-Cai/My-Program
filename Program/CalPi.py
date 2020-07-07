#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
'''
pi = 0
N =  100
for k in range(N):
    pi += 1/pow(16,k)*(\
        4/(8*k+1) - 2/(8*k+4) - \
        1/(8*k+5) - 1/(8*k+6)
        )
print("PI:{}".format(pi))



from random import  random
from time import perf_counter
DARTS = 1000*100
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/。    6DARTS)
print("圆周率：{}".format(pi))
print("时间：{:.5f}s".format(perf_counter() - start))
'''
'''
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate':
        if password == '666666':
            print("登录成功！")
            break
    else:
        count += 1
    if count == 3:
        print("3次用户名或者密码均有误！退出程序。")
        break
'''
'''
count = 0
k=10000
while k>1:
    print(k)
    k=k/2
    count += 1
print(count)
'''
sum = 0

for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum += i
print(sum)


