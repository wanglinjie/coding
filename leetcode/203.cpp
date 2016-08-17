#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *newhead = head;

        // 寻找新链表头
        while(newhead && (newhead->val == val))
        {
            ListNode *temp = newhead;
            newhead = newhead->next;
            delete temp;
        }
        if ((newhead == NULL) || (newhead->next == NULL))
            return head;
        ListNode *first = head->next;
        ListNode *second = head;
        while (first)
        {
            if (first->val == val)
            {
                // 如果是需要移除的节点
                second->next = first->next;
                delete first;
                first = second->next;
            }
            else
            {
                // 不需要移除，则两个指针同时向右移动
                first = first->next;
                second = second->next;
            }
        }
        return newhead;
    }
};

int main()
{
    return 0;
}