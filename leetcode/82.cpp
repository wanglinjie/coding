#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode newhead(0);
        ListNode *first, *second, *tail;
        first = second = NULL;
        tail = &newhead;
        first = head->next;
        second = head;
        while(first != NULL)
        {
            // cout<<first->val<<endl;
            if(second->val == first->val)
            {
                int value = second->val;
                ListNode *temp = NULL;
                while((second != NULL) && (second->val == value))
                {
                    // cout<<second->val<<endl;
                    temp = second;
                    second = second->next;
                    //delete temp;
                }
                if(second != NULL)
                {
                    first = second->next;
                    if(first == NULL)
                        tail->next = second;
                }
                else
                {
                    first = NULL;
                    tail->next = NULL;
                }
                
            }
            else
            {
                tail->next = second;
                tail = tail->next;
                second = second->next;
                first = first->next;
            }
        }
        return newhead.next;
    }
};


int main()
{
    int nums[] = {1, 1, 2, 2, 3, 4, 4};
    ListNode head(0);
    ListNode *tail = &head;
    for(int i = 0; i < 7; ++i)
    {
        ListNode *temp = new ListNode(nums[i]);
        tail->next = temp;
        tail = tail->next;
    }
    Solution so;

    ListNode *ret = so.deleteDuplicates(head.next);
    while(ret != NULL)
    {
        cout<<ret->val<<endl;
        ret = ret->next;
    }

    return 0;
}