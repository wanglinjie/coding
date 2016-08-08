#include <iostream>
#include <vector>
#include <stack>
using namespace std;

/**
 * Definition for a binary tree node.
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode *> s;
        TreeNode *p = root;
        while (p != NULL or !s.empty())
        {
            if (p != NULL)
            {
                s.push(p);
                ret.push_back(p->val);
                p = p->left;
            }
            else
            {
                p = s.top();
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