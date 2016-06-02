#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160602
Last Modified: 
获取一个句法依赖语法树的从根到叶子节点所有路径
'''


def depth_first(syntax_tree, nodename):
    if nodename not in syntax_tree:
        return [[]]
    ret = []
    for i in syntax_tree[nodename]:
        result = []
        result.append(i[1])
        childs = depth_first(syntax_tree, i[0])
        for child in childs:
            # result.extend(child)
            ret.append(result + child)
    return ret


# {0: [(5, 'HED')], 2: [(1, 'ATT'), (3, 'RAD')], 4: [(2, 'ATT')], 5: [(4, 'SBV'), (6, 'VOB')]}
def find_path(ins):
    '''
    查找路径
    '''
    syntax_tree = {}
    head_num = 0
    for i, j in enumerate(ins):
        if j[0] not in syntax_tree:
            syntax_tree[j[0]] = []
        syntax_tree[j[0]].append((i+1, j[1]))
        # if j[1] == 'HED':
        #     head_num = i
        #     break
    ret = []
    for i in syntax_tree[0]:
        result = ["HED"]
        childs = depth_first(syntax_tree, i[0])
        # result.extend(depth_first(syntax_tree, i[0]))
        for child in childs:
            ret.append(result + child)
    # for i in 
    print ret
    print syntax_tree
    
if __name__ == "__main__":
    ins = [(2, 'ATT'), (4, 'ATT'), (2, 'RAD'), (5, 'SBV'), (0, 'HED') ,(5, 'VOB')]
    find_path(ins)