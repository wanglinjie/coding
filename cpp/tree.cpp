#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <cmath>

using namespace std;

struct BinaryTreeNode
{
    int m_nValue;
    BinaryTreeNode* m_pLeft;
    BinaryTreeNode* m_pRight;
};

// 获取二叉树中节点数量
int GetNodeNum(BinaryTreeNode* pRoot)
{
    if (pRoot == NULL)
        return 0;
    return GetNodeNum(pRoot->m_pLeft) + GetNodeNum(pRoot->m_pRight) + 1;
}

// 获取二叉树的深度
int GetDepth(BinaryTreeNode* pRoot)
{
    if (pRoot == NULL)
        return 0;
    int depthLeft = GetDepth(pRoot->m_pLeft);
    int depthRight = GetDepth(pRoot->m_pRight);
    return depthLeft > depthRight ? (depthLeft + 1) : (depthRight + 1);
}

// 前序遍历
void PreOrderTraverse(BinaryTreeNode* pRoot)
{
    if (pRoot == NULL)
        return;
    cout<<pRoot->m_nValue;
    PreOrderTraverse(pRoot->m_pLeft);
    PreOrderTraverse(pRoot->m_pRight);
}

// 中序遍历
void InOrderTraverse(BinaryTreeNode *pRoot)
{
    if (pRoot == NULL)
        return;
    InOrderTraverse(pRoot->m_pLeft);
    cout<<pRoot->m_nValue;
    InOrderTraverse(pRoot->m_pRight);
}

// 后序遍历
void PostOrderTraverse(BinaryTreeNode* pRoot)
{
    if (pRoot == NULL)
        return;
    PostOrderTraverse(pRoot->m_pLeft);
    PostOrderTraverse(pRoot->m_pRight);
    cout<<pRoot->m_nValue;
}

// 分层遍历
void LevelTraverse(BinaryTreeNode* pRoot)
{
    if (pRoot == NULL)
        return;
    queue<BinaryTreeNode *> q;
    q.push(pRoot);
    while(!q.empty())
    {
        BinaryTreeNode* pNode = q.front();
        q.pop();
        cout<<pNode->m_nValue<<endl;
        if (pNode->m_pLeft != NULL)
            q.push(pNode->m_pLeft);
        if (pNode->m_pRight != NULL)
            q.push(pNode->m_pRight);
    }
}


// 将二叉查找树转换为有序的双向链表
void Convert(BinaryTreeNode *pRoot, BinaryTreeNode *&pFirstNode, BinaryTreeNode * & pLastNode)
{
    BinaryTreeNode * pFirstLeft, *pLastLeft, *pFirstRight, *pLastRight;
    if (pRoot == NULL)
    {
        pFirstNode = NULL;
        pLastNode = NULL;
        return;
    }

    if (pRoot->m_pLeft == NULL)
    {
        pFirstNode = pRoot;
    }
    else
    {
        Convert(pRoot->m_pLeft, pFirstLeft, pLastLeft);
        pFirstNode = pFirstLeft;
        pRoot->m_pLeft= pLastLeft;
        pLastLeft->m_pRight = pRoot;
    }

    if (pRoot->m_pRight == NULL)
    {
        pLastNode = pRoot;
    }
    else
    {
        Convert(pRoot->m_pRight, pFirstRight, pLastRight);
        pLastNode = pLastRight;
        pRoot->m_pRight = pFirstRight;
        pFirstRight->m_pLeft = pRoot;
    }
}

// 获取第K层元素个数
int GetNodeNumKthLevel(BinaryTreeNode *pRoot, int k)
{
    if (pRoot == NULL || k < 1)
        return 0;
    if (k == 1)
        return 1;
    int numLeft = GetNodeNumKthLevel(pRoot->m_pLeft, k-1);
    int numRight = GetNodeNumKthLevel(pRoot->m_pRight, k-1);
    return (numLeft + numRight);
}

// 获取二叉树中叶子节点数量
int GetLeafNodeNum(BinaryTreeNode *pRoot)
{
    if (pRoot == NULL)
        return 0;
    if (pRoot->m_pLeft == NULL && pRoot->m_pRight == NULL)
        return 1;
    int numLeft = GetLeafNodeNum(pRoot->m_pLeft);
    int numRight = GetLeafNodeNum(pRoot->m_pRight);
    return (numLeft + numRight);
}

bool StructureCmp(BinaryTreeNode *pRoot1, BinaryTreeNode *pRoot2)
{
    if (pRoot1 == NULL && pRoot2 == NULL)
        return true;
    else if (pRoot1 == NULL || pRoot2 != NULL)
        return false;
    bool resultLeft = StructureCmp(pRoot1->m_pLeft, pRoot2->m_pLeft);
    bool resultRight = StructureCmp(pRoot1->m_pRight, pRoot2->m_pRight);
    return (resultLeft && resultRight);
}

bool IsAVL(BinaryTreeNode *pRoot, int & height)
{
    if (pRoot == NULL)
    {
        height = 0;
        return true;
    }
    int heightLeft;
    bool resultLeft = IsAVL(pRoot->m_pLeft, heightLeft);
    int heightRight;
    bool resultRight = IsAVL(pRoot->m_pRight, heightRight);
    if (resultLeft && resultRight && abs(heightLeft - heightRight) <= 1)
    {
        height = max(heightLeft, heightRight) + 1;
        return true;
    }
    else
    {
        height = max(heightLeft, heightRight) + 1;
        return false;
    }
}


// 求二叉树的镜像
BinaryTreeNode * Mirror(BinaryTreeNode *pRoot)
{
    if (pRoot == NULL)
        return NULL;
    BinaryTreeNode * pLeft = Mirror(pRoot->m_pLeft);
    BinaryTreeNode * pRight = Mirror(pRoot->m_pRight);
    pRoot->m_pLeft = pRight;
    pRoot->m_pRight = pLeft;
    return pRoot;
}

//
/*bool FindNode(BinaryTreeNode* pRoot, BinaryTreeNode * pNode)
{
    if (pRoot == NULL || pNode == NULL)
        return false;
    if (pRoot == pNode)
        return true;
    bool found = FindNode(pRoot->m_pLeft, pNode);
    if (!found)
        found = FindNode(pRoot->m_pRight, pNode);
    return found;
}

BinaryTreeNode * GetLastCommonParent(BinaryTreeNode * pRoot, BinaryTreeNode *pNode1, BinaryTreeNode *pNode2)
{
    if (pRoot == NULL)
        return NULL;
    if (FindNode(pRoot->m_pLeft, pNode1))
    {
        if (FindNode(pRoot->m_pRight, pNode2))
            return pRoot;
        else
            return GetLastCommonParent(pRoot->m_pLeft, pNode1, pNode2);
    }
    else
    {
        if (FindNode(pRoot->m_pLeft, pNode2))
            return pRoot;
        else
            return GetLastCommonParent(pRoot->m_pRight, pNode1, pNode2);
    }
}*/

bool GetNodePath(BinaryTreeNode *pRoot, BinaryTreeNode *pNode, list<BinaryTreeNode *> &path)
{
    if (pRoot == pNode)
    {
        path.push_back(pRoot);
        return true;
    }
    if (pRoot == NULL)
        return false;
    path.push_back(pRoot);
    bool found = false;
    found = GetNodePath(pRoot->m_pLeft, pNode, path);
    if (!found)
        found = GetNodePath(pRoot->m_pRight, pNode, path);
    if (!found)
        path.pop_back();
    return found;
}

// 求二叉树中两个节点的最低公共祖先节点
BinaryTreeNode * GetLastCommonParent(BinaryTreeNode *pRoot, BinaryTreeNode *pNode1, BinaryTreeNode *pNode2)
{
    if (pRoot == NULL || pNode1 == NULL || pNode2 == NULL)
        return NULL;
    list<BinaryTreeNode *> path1;
    bool bResult1 = GetNodePath(pRoot, pNode1, path1);
    list<BinaryTreeNode *> path2;
    bool bResult2 = GetNodePath(pRoot, pNode2, path2);
    if (!bResult1 || !bResult2)
        return NULL;
    BinaryTreeNode *pLast = NULL;
    list<BinaryTreeNode *>::const_iterator iter1 = path1.begin();
    list<BinaryTreeNode *>::const_iterator iter2 = path2.begin();
    while (iter1 != path1.end() && iter2 != path2.end())
    {
        if (*iter1 == *iter2)
            pLast = *iter1;
        else
            break;
        iter1++;
        iter2++;
    }
    return pLast;
}


// 求二叉树中节点的最大距离
int GetMaxiDistance(BinaryTreeNode *pRoot, int &maxLeft, int &maxRight)
{
    if (pRoot == NULL)
    {
        maxLeft = 0;
        maxRight = 0;
        return 0;
    }
    int maxLL, maxLR, maxRL, maxRR;
    int maxDistLeft, maxDistRight;
    if (pRoot->m_pLeft != NULL)
    {
        maxDistLeft = GetMaxiDistance(pRoot->m_pLeft, maxLL, maxLR);
        maxLeft = max(maxLL, maxLR) + 1;
    }
    else
    {
        maxDistLeft = 0;
        maxLeft = 0;
    }
    if (pRoot->m_pRight != NULL)
    {
        maxDistRight = GetMaxiDistance(pRoot->m_pRight, maxRL, maxRR);
        maxRight = max(maxRL, maxRR) + 1;
    }
    else
    {
        maxDistRight = 0;
        maxRight = 0;
    }
    return max(max(maxDistLeft, maxDistRight), maxLeft+maxRight);
}


// 由前序遍历序列和中序遍历序列重建二叉树
BinaryTreeNode * RebuildBinaryTree(int * pPreOrder, int* pInOrder, int nodeNum)
{
    if (pPreOrder == NULL || pInOrder == NULL || nodeNum <= 0)
        return NULL;
    BinaryTreeNode *pRoot = new BinaryTreeNode;
    pRoot->m_nValue = pPreOrder[0];
    pRoot->m_pLeft = NULL;
    pRoot->m_pRight = NULL;
    int rootPositionInOrder = -1;
    for (int i = 0; i < nodeNum; i++)
    {
        if (pInOrder[i] == pRoot->m_nValue)
        {
            rootPositionInOrder = i;
            break;
        }
    }
    if (rootPositionInOrder == -1)
    {
        // exit(-1);
        throw "Invalid input.";
    }
    int nodeNumLeft = rootPositionInOrder;
    int *pPreOrderLeft = pPreOrder + 1;
    int *pInOrderLeft = pInOrder;
    pRoot->m_pLeft = RebuildBinaryTree(pPreOrderLeft, pInOrderLeft, nodeNumLeft);

    int nodeNumRight = nodeNum - nodeNumLeft - 1;
    int *pPreOrderRight = pPreOrder + 1 + nodeNumLeft;
    int *pInOrderRight = pInOrder + nodeNumLeft + 1;
    pRoot->m_pRight = RebuildBinaryTree(pPreOrderRight, pInOrderRight, nodeNumRight);
    return pRoot;
}


// 判断一棵二叉树是否是完全树
bool IsCompleteBinaryTree(BinaryTreeNode *pRoot)
{
    if (pRoot == NULL)
        return false;
    queue<BinaryTreeNode *> q;
    q.push(pRoot);
    bool mustHaveNoChild = false;
    bool result = true;
    while (!q.empty())
    {
        BinaryTreeNode *pNode = q.front();
        q.pop();
        if (mustHaveNoChild)
        {
            if (pNode->m_pLeft != NULL || pNode->m_pRight != NULL)
            {
                result = false;
                break;
            }
        }
        else
        {
            if (pNode->m_pLeft != NULL && pNode->m_pRight != NULL)
            {
                q.push(pNode->m_pLeft);
                q.push(pNode->m_pRight);
            }
            else if (pNode->m_pLeft != NULL && pNode->m_pRight == NULL)
            {
                mustHaveNoChild = true;
                q.push(pNode->m_pLeft);
            }
            else if (pNode->m_pLeft == NULL && pNode->m_pRight != NULL)
            {
                result = false;
                break;
            }
            else
            {
                mustHaveNoChild = true;
            }
        }
    }
    return result;
}


int main()
{
    return 0;
}