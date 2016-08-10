#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL or headB == NULL)
            return NULL;
        int nodeA_num = 0;
        int nodeB_num = 0;
        ListNode *nodeA = headA;
        ListNode *nodeB = headB;
        nodeA_num++;
        while (nodeA->next != NULL)
        {
            nodeA_num++;
            nodeA = nodeA->next;
        }
        nodeB_num++;
        while (nodeB->next != NULL)
        {
            nodeB_num++;
            nodeB = nodeB->next;
        }
            
        if (nodeA != nodeB)
            return NULL;
        nodeA = headA;
        nodeB = headB;
        if (nodeA_num > nodeB_num)
        {
            int diff = nodeA_num - nodeB_num;
            while (diff > 0)
            {
                nodeA = nodeA->next;
                diff--;
            }
        }
        else
        {
            int diff = nodeB_num - nodeA_num;
            while (diff > 0)
            {
                nodeB = nodeB->next;
                diff--;
            }
        }
        while (nodeA != nodeB)
        {
            nodeA = nodeA->next;
            nodeB = nodeB->next;
        }
        return nodeA;
    }
};

int main()
{
    return 0;
}