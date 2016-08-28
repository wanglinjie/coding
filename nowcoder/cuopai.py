#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160828

'''
[编程题]发邮件
NowCoder每天要给很多人发邮件。有一天他发现发错了邮件，把发给A的邮件发给了B，
把发给B的邮件发给了A。于是他就思考，要给n个人发邮件，在每个人仅收到1封邮件的情况下，
有多少种情况是所有人都收到了错误的邮件？
即没有人收到属于自己的邮件。

输入描述:

输入包含多组数据，每组数据包含一个正整数n（2≤n≤20）。


输出描述:

对应每一组数据，输出一个正整数，表示无人收到自己邮件的种数。

输入例子:

2
3

输出例子:

1
2



思路：
这个就是求错排个数
错排计算公式
D = n! * (1 - 1/1! + 1/2! ... + (-1)^n*1/n!)
'''
try:
    while True:
        n = input()
        factorials = [1] * (n + 1)
        label = -1
        number = 1
        for i in xrange(1, n+1):
            number *= i
            factorials[i] = number * label
            label *= -1
        ret = number
        for i in xrange(1, n+1):
            ret += (number / factorials[i])
        print ret
except:
    pass