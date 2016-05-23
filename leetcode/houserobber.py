#-*-coding:utf-8-*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass

def feibo(n):
    if n == 0:
        print 0
        return
    elif n == 1:
        print 1
        return
    a = 0
    b = 1
    res = 0
    for i in xrange(2, n+1):
        res = a + b
        a = b
        b = res
    print res

# feibo(13)
def zuhe(list1, sumnum):
    list1 = sorted(list1)
    i = 0
    j = len(list1) - 1
    while (i < j):
        if (list1[i] + list1[j]) == sumnum:
            print list1[i], list1[j]
            i += 1
            j -= 1
        elif (list1[i] + list1[j]) < sumnum:
            i += 1
        elif (list1[i] + list1[j]) > sumnum:
            j -= 1

# zuhe([1, 2, 3, 4, 5, 6, 7], 8)




def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            # 如果节点超过总节点数则退出
            if child > end:
                break
            # 选择大的孩子节点
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            # 如果根节点值小于孩子节点则交换
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst
            
def main():
    l = [9,2,1,7,6,8,5,3,4]
    heap_sort(l)
    for i in l:
        print i

if __name__ == "__main__":
    main()

