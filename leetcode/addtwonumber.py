# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1
        num2 = l2
        one = 0
        returnnum = None
        now = 0
        returnnum = None
        while num1 and num2:
            sumnum = num1.val + num2.val + one
            one = sumnum / 10
            tempnode = ListNode(sumnum % 10)
            if returnnum:
                now.next = tempnode
                now = now.next
            else:
                returnnum = tempnode
                now = tempnode
            num1 = num1.next
            num2 = num2.next
        while num1:
            sumnum = num1.val + one
            one = sumnum / 10
            tempnode = ListNode(sumnum % 10)
            if returnnum:
                now.next = tempnode
                now = now.next
            else:
                returnnum = tempnode
                now = tempnode
            num1 = num1.next
        while num2:
            sumnum = num2.val + one
            one = sumnum / 10
            tempnode = ListNode(sumnum % 10)
            if returnnum:
                now.next = tempnode
                now = now.next
            else:
                returnnum = tempnode
                now = tempnode
            num2 = num2.next
        if one:
            tempnode = ListNode(one)
            now.next = tempnode
        return returnnum




            # tempnode = ListNode(sumnum % 10)
            # now.val = sumnum % 10
            # now.next = ListNode(0)
if __name__ == "__main__":
    so = Solution()
    l1 = 
