#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/**
 * Definition for a binary tree node.
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].


思路：
从树的右侧看，记录看到的节点
这样就是每一层只有最右侧的节点被记录
层次遍历树中节点，记录每一层节点
每层节点中有右侧节点被存储值
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        if (root == NULL)
            return ret;
        TreeNode *node = root;
        queue<TreeNode *> q;
        TreeNode *last;
        q.push(node);
        // NULL记录一层结束
        q.push(NULL);
        while(!q.empty())
        {
            node = q.front();
            q.pop();
            if (node == NULL)
            {
                // 如果为NULL，则代表该层遍历结束

                // 存储上次遍历节点的值
                ret.push_back(last->val);
                // 如果q不为空，则代表q中还有其它节点
                if (!q.empty())
                    q.push(NULL);
            }
            else
            {
                // 将当前节点左右节点如队列
                if (node->left != NULL)
                    q.push(node->left);
                if (node->right != NULL)
                    q.push(node->right);
            }
            // 保存当前节点
            last = node;
        }
        return ret;
    }
};

int main()
{
    return 0;
}