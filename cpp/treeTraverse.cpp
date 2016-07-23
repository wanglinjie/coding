#include <iostream>
#include <stack>
#include <queue>
using namespace std;

struct BinaryTreeNode {
    int value;
    BinaryTreeNode *left;
    BinaryTreeNode *right;
};

void preOrderTraverse(BinaryTreeNode *root)
{
    if (root == NULL)
        return;
    stack<BinaryTreeNode *> s;
    BinaryTreeNode *p = root;
    s.push(root);
    while (!s.empty())
    {
        p = s.top();
        s.pop();
        cout<<p->value<<endl;
        if (p->right != NULL)
            s.push(p->right);
        if (p->left != NULL)
            s.push(p->left);
    }
}

void preOrderTraverse2(BinaryTreeNode *root)
{
    if (root == NULL)
        return;
    stack<BinaryTreeNode *> s;
    BinaryTreeNode *p;
    p = root;
    while (p != NULL || !s.empty())
    {
        if (p != NULL)
        {
            cout<<p->value<<endl;
            s.push(p);
            p = p->left;
        }
        else
        {
            p = s.top();
            p = p->right;
            s.pop();
        }
    }
}

void inOrderTraverse(BinaryTreeNode *root)
{
    if (root == NULL)
        return;
    BinaryTreeNode *p = root;
    stack<BinaryTreeNode *> s;
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
            cout<<p->value<<endl;
            s.pop();
            p = p->right;
        }
    }
}


void postOrderTraverse(BinaryTreeNode *root)
{
    if (root == NULL)
        return;
    stack<BinaryTreeNode *> s1, s2;
    BinaryTreeNode *p = root;
    s1.push(p);
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
        cout<<p->value<<endl;
        s2.pop();
    }
}

void levelOrderTraversal(BinaryTreeNode *root)
{
    if (root == NULL)
        return;
    queue<BinaryTreeNode *> q1, q2;
    BinaryTreeNode *p = root;
    q1.push(p);
    q1.push(NULL);
    while (!q1.empty())
    {
        p = q1.front();
        q1.pop();
        if (p == NULL)
        {
            if (!q1.empty())
                q1.push(NULL);
            while(!q2.empty())
            {
                BinaryTreeNode *temp;
                temp = q2.front();
                q2.pop();
                cout<<temp->value;
            }
            continue;
        }
        q2.push(p);
    }
}

int main()
{
    BinaryTreeNode *root;
    root = new BinaryTreeNode;
    root->value = 10;
    cout<<root->value<<endl;
    delete root;
    return 0;
}