#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
'''
height,weight = eval(input("身高和体重逗号隔开"))
bmi = weight / pow(height,2)
print("BMI:{:.2f}".format(bmi))
who, nat = "",""
if bmi < 18.5:
    who,nat = "偏瘦","偏瘦"
elif 18.5 <= bmi < 24:
    who,nat = "正常","正常"
elif 24 <= bmi < 25:
    who,nat = "正常", "偏旁"
elif 25 <= bmi <28:
    who,nat = "偏胖", "肥胖"
elif 28 < bmi <= 30:
    who,nat  = "肥胖", "肥胖"
print("国际'{0}',国内'{1}'".format(who,nat))

'''
d={"a":1, "b":2}
print(type(d.values()))
