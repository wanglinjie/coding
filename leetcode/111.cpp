#include <iostream>
#include <cmath>
using namespace std;

/**
 * Definition for a binary tree node.
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        int left, right;
        left = minDepth(root->left);
        right = minDepth(root->right);
        // 注意当左右子树为0时，当前节点未必是叶子节点
        if (left == 0)
            return right+1;
        else if (right == 0)
            return left+1;
        return min(left, right)+1;
    }
};

int main()
{
    return 0;
}