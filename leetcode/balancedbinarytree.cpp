#include <iostream>
#include <cmath>
using namespace std;

/**
 * Definition for a binary tree node.
Given a binary tree, determine if it is height-balanced.

For this problem, 
a height-balanced binary tree is defined as a binary tree in which 
the depth of the two subtrees of every node never differ by more than 1.
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == NULL)
            return true;
        int high;
        bool ret = isBalancedSubtree(root, high);
        return ret;
    }
    bool isBalancedSubtree(TreeNode *root, int &high)
    {
        if (root == NULL)
        {
            high = 0;
            return true;
        }
        int left, right;
        bool isBalancedLeft = false;
        bool isBalancedRight = false;
        // 判断左子树是否为平衡树
        isBalancedLeft = isBalancedSubtree(root->left, left);
        // 判断右子树是否为平衡树
        isBalancedRight = isBalancedSubtree(root->right, right);
        // 如果左子树或者右子树不是平衡树，或者左右子树层数相差超过1,则这棵树就不是平衡树
        high = max(left, right) + 1;
        if((!isBalancedLeft) || (!isBalancedRight) || abs(left - right) > 1)
        {
            return false;
        }
        // 这棵树是平衡树
        return true;
    }
};

int main()
{
    return 0;
}