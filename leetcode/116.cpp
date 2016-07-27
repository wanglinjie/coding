#include <iostream>
#include <stack>
using namespace std;

/**
 * Definition for binary tree with next pointer.

 Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, 
and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
 */

// 一个思路是层次遍历，同一层的节点相连
// 另一个思路是左孩子连向右孩子，右孩子连向本节点的下一节点的左孩子
struct TreeLinkNode {
 int val;
 TreeLinkNode *left, *right, *next;
 TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL)
            return;
        stack<TreeLinkNode *> s;
        TreeLinkNode *p;
        s.push(root);
        while (!s.empty())
        {
            p = s.top();
            s.pop();
            if (p->left != NULL)
            {
                // 左孩子next指向右孩子
                p->left->next = p->right;
                if (p->next != NULL)
                    // 右孩子next指向本节点下一节点的左孩子
                    p->right->next = p->next->left;
                else
                    p->right->next = NULL;
                // 左右孩子入栈
                s.push(p->left);
                s.push(p->right);
            }
        }
    }
};

int main()
{
    return 0;
}