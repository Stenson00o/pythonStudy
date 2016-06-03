#!/usr/bin/env python
# coding=utf-8

#w--weigh
#v--the value of goods
#i, array index
#aw, the rest of availabe weigh
def maxvalue(w, v, i, aw):
    if i == 0:
        #如果背包的剩余空间可以装得下物品
        if w[i] <= aw:
            return v[i]
        return 0
    #不选择该物品，继续下一个物品
    without_i = maxvalue(w, v, i-1, aw)
    #选择该物品，判断背包是否可以装得下
    #如果可以装得下，继续下一个物品，同时减去该重量
    if w[i] <  aw :
        with_i = v[i] + maxvalue(w, v, i - 1, aw - w[i])
    else: 
        with_i = v[i]

    return max(without_i, with_i)

def max(a, b):
    if a > b:
        return a

    return b
#
#test the value
w = [5, 3, 2, 32, 3, 1, 4, 123, 425, 213]
v = [9, 7, 8, 3, 33, 34, 2, 23, 2, 23]
s = [3, 6, 7, 23, 1, 67, 23, 3, 2, 123]
#print maxvalue(w, v, 2, 5)

#this time w, v, s, i , aw , as)
def fastmaxvalue(w, v, s, i, aw, rs):
    meno = {}
    try :
        return meno[(i,aw, rs)]
    except KeyError, e:
        if i == 0:
            #如果背包的剩余空间可以装得下物品
            if (w[i] <= aw)  and (s[i] <= rs):
                return v[i]
            return 0
        #不选择该物品，继续下一个物品
        without_i = fastmaxvalue(w, v, s, i-1, aw, rs)
        #选择该物品，判断背包是否可以装得下
        #如果可以装得下，继续下一个物品，同时减去该重量
        if w[i] <  aw and s[i] < rs :
            with_i = v[i] + fastmaxvalue(w, v, s, i - 1, aw - w[i], rs - s[i])
        else: 
            with_i = v[i]

        res =  max(without_i, with_i)
        meno[(i,aw)] = res

        return res


#test 

#test the value
#w = [5, 3, 2]
#v = [9, 7, 8]
#s = [3, 6, 7]
print fastmaxvalue(w, v, s,  9, 60, 70)
