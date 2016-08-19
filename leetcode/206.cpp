#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 
 reverse a singly linked list.
 */


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *newhead = NULL;
        ListNode *node = head;
        ListNode *temp = NULL;
        while(node != NULL)
        {
            temp = node->next;
            node->next = newhead;
            newhead = node;
            node = temp;
        }
        return newhead;
    }
};

int main()
{
    return 0;
}