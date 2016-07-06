#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160706
# 格式转换

import json

def unicode2utf(datas):
    '''
    将unicode列表转换为utf-8
    '''
    ret = []
    for data in datas:
        if type(data) == unicode:
            ret.append(data.encode("utf-8"))
        elif type(data) == list:
            temp = unicode2utf(data)
            ret.append(temp)
        elif type(data) == str:
            ret.append(data)
        else:
            print type(data)
            raise TypeError
    return ret


if __name__ == "__main__":
    datas = [u"卧室", [u"好的", ["现代", u"什么"]], u"模型"]
    ret = unicode2utf(datas)
    for i in ret:
        if type(i) == str:
            print i
        elif type(i) == list:
            print json.dumps(i, encoding="utf-8", ensure_ascii=False)
