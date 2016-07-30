#include <iostream>
using namespace std;

/**
date:20160730
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if (root == NULL)
            return -2147483648;
        int maxSum = INT_MIN;
        int ret = maxSubTree(root, maxSum);
        return maxSum;
        
    }
    int maxSubTree(TreeNode* root, int &maxSum)
    {
        if (root == NULL)
        {
            return 0;
        }
        int ret;
        int leftPathValue, rightPathValue;
        leftPathValue = maxSubTree(root->left, maxSum);
        rightPathValue = maxSubTree(root->right, maxSum);
        // 只有当左子树值大于0时才进入判断
        if (leftPathValue > 0 && leftPathValue > rightPathValue)
        {
            ret = leftPathValue+root->val;
            if ((leftPathValue+root->val) > maxSum)
                maxSum = leftPathValue+root->val;
        }
        else if (rightPathValue > 0)
        {
            ret = rightPathValue+root->val;
            if ((rightPathValue+root->val) > maxSum)
                maxSum = rightPathValue+root->val;
        }
        else
        {
            ret = root->val;
            if (root->val > maxSum)
                maxSum = root->val;
        }
        if ((leftPathValue+root->val + rightPathValue) > maxSum)
            maxSum = leftPathValue+root->val+rightPathValue;
        return ret;
    }
};

int main()
{
    return 0;
}