#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160812

'''
有 n 个字符串，每个字符串都是由 A-J 的大写字符构成。
现在你将每个字符映射为一个 0-9 的数字，不同字符映射为不同的数字。
这样每个字符串就可以看做一个整数，
唯一的要求是这些整数必须是正整数且它们的字符串不能有前导零。
现在问你怎样映射字符才能使得这些字符串表示的整数之和最大？

输入描述:
每组测试用例仅包含一组数据，每组数据第一行为一个正整数 n ， 
接下来有 n 行，每行一个长度不超过 12 且仅包含大写字母 A-J 的字符串。 
n 不大于 50，且至少存在一个字符不是任何字符串的首字母。


输出描述:
输出一个数，表示最大和是多少。

输入例子:
2
ABC
BCA

输出例子:
1875
'''
def maxMap():
    while True:
        n = input()
        strings = []
        char_num = {}
        char_dic = {}
        start_char = set()
        for i in xrange(n):
            temp = raw_input()
            strings.append(temp)

        # 获取每个字符的权重
        for string in strings:
            # 记录首字母
            start_char.add(string[0])
            string_len = len(string)
            value = 1
            for i in xrange(string_len-1, -1, -1):
                if string[i] not in char_dic:
                    char_dic[string[i]] = 0
                char_dic[string[i]] += value
                value *= 10
        # 按照权重将字母排序
        sorted_list = sorted(char_dic, key=char_dic.__getitem__)
        char_len = len(char_dic)
        if char_len == 10:
            # 如果有10个不同字母
            for i in xrange(char_len):
                if sorted_list[i] in start_char:
                    continue
                char_num[sorted_list[i]] = "0"
                del sorted_list[i]
                break
            for i in xrange(char_len - 1):
                char_num[sorted_list[i]] = str(i + 1)
        else:
            # 如果少于10个不同字母，则不需要判断0
            for i in xrange(char_len):
                char_num[sorted_list[i]] = str(9 - char_len + i + 1)
        total = 0
        for string in strings:
            num_string = ""
            for i in string:
                num_string += char_num[i]
            total += int(num_string)
        print total