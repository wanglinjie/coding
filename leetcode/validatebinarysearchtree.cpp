#include <iostream>
using namespace std;

/*
考虑中序遍历，则这个遍历列表是一个递增序列
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == NULL || (root->left == NULL && root->right == NULL))
            return true;
        int low, high;
        bool ret = isValidsubTree(root, low, high);
        return ret;
    }
    bool isValidsubTree(TreeNode *root, int &low, int &high)
    {
        if (root == NULL)
            return true;
        if (root->left == NULL && root->right == NULL)
        {
            low = root->val;
            high = root->val;
            return true;
        }
        int ll, lh, rl, rh;
        bool isValidLeft = false;
        bool isValidRight = false;
        if (root->left != NULL)
        {
            isValidLeft = isValidsubTree(root->left, ll, lh);
            if ((isValidLeft && (lh >= root->val)) || (! isValidLeft))
                return false;
            low = ll;
        }
        else
            low = root->val;
        if (root->right != NULL)
        {
            isValidRight = isValidsubTree(root->right, rl, rh);
            if ((isValidRight && (rl <= root->val)) || (!isValidRight))
                return false;
            high = rh;
        }
        else
            high = root->val;
        // low = min(ll, lh);
        // high = max(rl, rh);
        return true;
    }
};

int main()
{
    return 0;
}


/*TreeNode* prev = NULL;
        return validate(root, prev);
    }
    bool validate(TreeNode* node, TreeNode* &prev) {
        if (node == NULL) return true;
        if (!validate(node->left, prev)) return false;
        if (prev != NULL && prev->val >= node->val) return false;
        prev = node;
        return validate(node->right, prev);*/