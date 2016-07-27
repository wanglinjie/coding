#include <iostream>
#include <queue>
using namespace std;

/**
date:20160727
 * Definition for binary tree with next pointer.

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL


思路：
将这道题按照层次遍历来看，每层节点从左到右如队列，每层结束节点next指向NULL
 */
struct TreeLinkNode {
 int val;
 TreeLinkNode *left, *right, *next;
 TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(root == NULL)
            return;
        queue<TreeLinkNode *> q;
        TreeLinkNode *p = NULL, *pre = NULL;
        q.push(root);
        q.push(NULL);
        while (!q.empty())
        {
            p = q.front();
            q.pop();
            if (pre != NULL)
                pre->next = p;
            pre = p;
            if(p != NULL)
            {
                if (p->left != NULL)
                    q.push(p->left);
                if (p->right != NULL)
                    q.push(p->right);
            }
            else
            {
               if (!q.empty())
                q.push(NULL);
            }
        }
    }
};


int main()
{
    return 0;
}