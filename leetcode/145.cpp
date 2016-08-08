#include <iostream>
#include <vector>
#include <stack>
using namespace std;
// date:20160808
/**
 * Definition for a binary tree node.
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

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
    //下面思路和无递归前序遍历类似，只是先将右节点入栈
    /*vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode *> s1;
        stack<TreeNode *> s2;
        TreeNode *p = root;
        while ((p != NULL) or (!s1.empty()))
        {
            if (p != NULL)
            {
                s1.push(p);
                s2.push(p);
                p = p->right;
            }
            else
            {
                p = s1.top();
                s1.pop();
                p = p->left;
            }
        }
        while (!s2.empty())
        {
            p = s2.top();
            s2.pop();
            ret.push_back(p->val);
        }
        return ret;
    }*/
    // 下面代码比上面代码速度快
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (root == NULL)
            return ret;
        stack<TreeNode *> s1;
        stack<TreeNode *> s2;
        TreeNode *p;
        s1.push(root);
        while (!s1.empty())
        {
            p = s1.top();
            s2.push(p);
            s1.pop();
            if (p->left != NULL)
                s1.push(p->left);
            if (p->right != NULL)
                s1.push(p->right);
                
        }
        while (!s2.empty())
        {
            p = s2.top();
            s2.pop();
            ret.push_back(p->val);
        }
        return ret;
    }
};

int main()
{
    return 0;
}