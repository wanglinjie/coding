#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160828

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