#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
from random import *


def printInfo():
    print("程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的值表示)")

def getInputs():
    a = eval(input("请输入A选手的能力值(0-1):"))
    b = eval(input("请输入B选手的能力值(0-1):"))
    n = eval(input("模拟比赛的场次:"))
    return a,b,n


def simNGames(n,probA,probB):
    winA,winB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGam(probA,probB)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1
    return winA,winB

def simOneGam(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB

def gameOver(a,b):
    return a == 15 or b ==15


def printSummary(winA,winB):
    n = winA + winB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场，占比{:0.1%}".format(winA, winA / n))
    print("选手B获胜{}场，占比{:0.1%}".format(winB, winB / n))

def main():
    printInfo()
    probA,probB,n = getInputs()
    winA,winB = simNGames(n,probA,probB)
    printSummary(winA,winB)

main()