#include <iostream>
using namespace std;
// date:20160725
/**
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (root == NULL)
            return ret;
        
        stack<TreeNode *> s;
        TreeNode *p = root;
        while (p != NULL || !s.empty())
        {
            if (p != NULL)
            {
                s.push(p);
                p = p->left;
            }
            else
            {
                p = s.top();
                ret.push_back(p->val);
                s.pop();
                p = p->right;
            }
        }
        return ret;
    }
};

int main()
{
    return 0;
}