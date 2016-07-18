#include <iostream>
using namespace std;


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    TreeNode* recursiveFlatten(TreeNode *root)
    {
        if ((root != NULL) && (root->left == NULL) && (root->right == NULL))
            return root;
        TreeNode *left = root->left;
        TreeNode *right = root->right;
        TreeNode *left_ret = NULL;
        TreeNode *right_ret = NULL;
        if (left != NULL)
        {
            root->right = left;
            root->left = NULL;
            left_ret = recursiveFlatten(left);
            left_ret->right = right;
        }
        if (right != NULL)
        {
            right_ret = recursiveFlatten(right);
        }
        if (right_ret != NULL)
            return right_ret;
        else
        {
            return left_ret;
        }
    }
    void flatten(TreeNode* root) {
        if (root == NULL)
            return;
        recursiveFlatten(root);
    }
};

int main()
{
    Solution so;
    return 0;
}