#include <iostream>
#include <stack>
using namespace std;

struct ListNode
{
    int value;
    ListNode *next;
};

// 求单链表中节点个数
unsigned int GetListLength(ListNode *pHead)
{
    if (pHead == NULL)
        return 0;
    ListNode *temp;
    temp = pHead;
    int ret = 0;
    while (temp != NULL)
    {
        ret += 1;
        temp = temp->next;
    }
    return ret;
}

// 将单链表反转
ListNode * ReverseList(ListNode *pHead)
{
    /*if (pHead == NULL || pHead->next == NULL)
        return pHead;
    ListNode *first, *second, *head;
    first = pHead->next;
    second = pHead;
    head = first->next;
    second->next = NULL;
    while (true)
    {
        first->next = second;
        second = first;
        first = head;
        if (first == NULL)
            break;
        head = head->next;
    }
    head = second;
    return head;*/
    if (pHead == NULL || pHead->next == NULL)
        return pHead;
    ListNode *head = NULL;
    ListNode *current = pHead;
    ListNode *temp;
    while (current != NULL)
    {
        temp = current;
        current = current->next;
        temp->next = head;
        head = temp;
    }
    return head;
}

// 查找单链表中的倒数第k个节点
ListNode * RGetKthNode(ListNode *pHead, unsigned int k)
{
    if (pHead == NULL || k <= 0)
        return NULL;

    ListNode *first=pHead;
    ListNode *second=pHead;
    unsigned int temp = k;
    while ((first != NULL) && temp)
    {
        first = first->next;
        temp--;
    }
    if (temp > 0)
        return NULL;
    while (first != NULL)
    {
        first = first->next;
        second = second->next;
    }
    return second;
}

// 查找单链表的中间节点
ListNode *GetMiddleNode(ListNode *pHead)
{
    /*if (pHead == NULL)
        return pHead;
    int listLength = 0;
    ListNode *first = pHead;
    ListNode *second = pHead;
    while (first != NULL)
    {
        listLength++;
        first = first->next;
    }
    int middle;
    if (listLength & 0x1)
        middle = (listLength >> 2) + 1;
    else:
        middle = (listLength >> 2) - 1;

    first = pHead;
    while (middle > 0)
    {
        first = first->next;
        middle--;
    }
    while (first != NULL)
    {
        first = first->next;
        second = second->next;
    }
    return second;*/
    if (pHead == NULL || pHead->next == NULL)
        return pHead;
    ListNode *first = pHead;
    ListNode *second = pHead;
    while (first->next != NULL)
    {
        first = first->next;
        second = second->next;
        if (first->next != NULL)
            first = first->next;
    }
    return second;
}


// 从尾到头打印单链表
void PrintList(ListNode *pHead)
{
    /*if (pHead == NULL)
        return;
    PrintList(pHead->next);
    cout<<pHead->value;*/
    stack<ListNode *> s;
    ListNode *pNode = pHead;
    while (pNode != NULL)
    {
        s.push(pNode);
        pNode = pNode->next;
    }
    while (!s.empty())
    {
        pNode = s.top();
        cout<<pNode->value;
        s.pop();
    }
}

// 已知两个链表pHead1和pHead2各自有序，把他们合并成一个链表依然有序
ListNode * MergeSortedList(ListNode *pHead1, ListNode *pHead2)
{
    if (pHead1 == NULL)
        return pHead2;
    else if (pHead2 == NULL)
        return pHead2;
    ListNode *head, *last;
    // head = last = pHead1->value < pHead2->value ? pHead1 : pHead2;
    if (pHead1->value < pHead2->value)
    {
        head = last = pHead1;
        pHead1 = pHead1->next;
    }
    else
    {
        head = last = pHead2;
        pHead2 = pHead2->next;
    }
    while (pHead1 != NULL && pHead2 != NULL)
    {
        if (pHead1->value < pHead2->value)
        {
            last->next = pHead1;
            last = last->next;
            pHead1 = pHead1->next;
        }
        else
        {
            last->next = pHead2;
            last = last->next;
            pHead2 = pHead2->next;
        }
    }
    if (pHead1 != NULL)
        last->next = pHead1;
    else if (pHead2 != NULL)
        last->next = pHead2;
    return head;
}

// 判断一个单链表中是否有环
bool HasCircle(ListNode *pHead)
{
    /*if (pHead == NULL)
        return false;
    ListNode *first = pHead;
    ListNode *second = pHead;
    if (first != NULL)
        first = first->next;
    while (first != NULL)
    {
        if (second == first)
            return true;
        second = second->next;
        first = first->next;
        if (first != NULL)
            first = first->next;
    }
    return false;*/
    ListNode *first = pHead;
    ListNode *second = pHead;
    while (first != NULL && first->next != NULL)
    {
        first = first->next->next;
        second = second->next;
        if (first == second)
            return true;
    }
    return false;
}

// 判断两个单链表是否相交
bool IsIntersected(ListNode *pHead1, ListNode *pHead2)
{
    /*if (pHead1 == NULL || pHead2 == NULL)
        return false;
    ListNode *current1 = pHead1;
    while(current1->next != NULL)
    {
        current1 = current1->next;
    }
    current1->next = pHead1;
    ListNode *current2 = pHead2;
    while(current2 != NULL)
    {
        if (current2 = pHead1)
            return true;
        current2 = current2->next;
    }
    return false;*/
    if (pHead1 == NULL || pHead2 == NULL)
        return false;
    ListNode *current1 = pHead1;
    ListNode *current2 = pHead2;
    while(current1->next != NULL)
        current1 = current1->next;
    while (current2->next != NULL)
        current2 = current2->next;
    if (current1 == current2)
        return true;
    else
        return false;
}

// 求两个单链表相交的第一个节点
ListNode *GetFirstCommonNode(ListNode *pHead1, ListNode *pHead2)
{
    if (pHead1 == NULL || pHead2 == NULL)
        return NULL;
    int head1_len = 1;
    int head2_len = 1;
    ListNode *current1 = pHead1;
    ListNode *current2 = pHead2;
    while(current1->next != NULL)
    {
        current1 = current1->next;
        head1_len++;
    }
    while(current2->next != NULL)
    {
        current2 = current2->next;
        head2_len++;
    }
    if (current1 != current2)
        return NULL;
    current1 = pHead1;
    current2 = pHead2;
    if (head1_len < head2_len)
    {
        int diff = head2_len - head1_len;
        while (diff)
        {
            current1 = current1->next;
            diff--;
        }
    }
    else
    {
        int diff = head1_len - head2_len;
        while (diff)
        {
            current2 = current2->next;
            diff--;
        }
    }
    while(current1 != NULL)
    {
        if (current1 == current2)
            return current1;
        current1 = current1->next;
        current2 = current2->next;
    }
}


// 已知一个单链表中存在环，求进入环中的第一个节点
ListNode * GetFirstNodeInCircle(ListNode *pHead)
{
    if (pHead == NULL || pHead->next == NULL)
        return pHead;
    ListNode *oldNode = pHead;
    ListNode *commonNode = NULL;
    ListNode *first = pHead->next;
    ListNode *second = pHead;
    while (first->next != NULL && first->next->next != NULL)
    {
        first = first->next->next;
        second = second->next;
        if (first == second)
        {
            commonNode = first;
            break;
        }
    }
    if (first->next == NULL || first->next->next == NULL)
        return NULL;
    ListNode *newNode = commonNode->next;
    commonNode->next = NULL;
    int list1_len = 0;
    int list2_len = 0;
    ListNode *temp = pHead;
    while (temp != NULL)
    {
        temp = temp->next;
        list1_len++;
    }
    temp = newNode;
    while (temp != NULL)
    {
        temp = temp->next;
        list2_len++;
    }
    temp = newNode;
    int diff;
    if (list1_len < list2_len)
    {
        diff = list2_len - list1_len;
        while (diff)
        {
            oldNode = oldNode->next;
            diff--;
        }
    }
    else
    {
        diff = list1_len - list2_len;
        while(diff)
        {
            temp = temp->next;
            diff--;
        }
    }
    while (temp != NULL)
    {
        if (temp == oldNode)
            return temp;
        temp = temp->next;
        oldNode = oldNode->next;
    }
}


// 给出一单链表头指针pHead和一节点指针pToBeDeleted, O(1)时间复杂度删除节点pToBeDeleted
void Delete(ListNode *pHead, ListNode *pToBeDeleted)
{
    if (pToBeDeleted == NULL)
        return;
    if (pToBeDeleted->next != NULL)
    {
        if (pToBeDeleted == pHead)
        {
            pHead = pHead->next;
            delete pToBeDeleted;
        }
        else
        {
            ListNode *temp = pToBeDeleted->next;
            pToBeDeleted->value = temp->value;
            pToBeDeleted->next = temp->next;
            delete temp;
        }
    }
    else
    {
        if (pToBeDeleted == pHead)
        {
            pHead = NULL;
            delete pToBeDeleted;
        }
        else
        {
            ListNode *temp;
            temp = pHead;
            while (temp->next != pToBeDeleted)
            {
                temp = temp->next;
            }
            temp->next = NULL;
            delete pToBeDeleted;
        }
    }
}

int l_child(int i)
{
    return 2 * i;
}

int r_child(int i)
{
    return 2 * i + 1;
}

int parent(int i)
{
    return i / 2;
}

void min_heapify_recur(int *array, int i, int k)
{
    int l = l_child(i);
    int r = r_child(i);
    int smallest = l;
    if ((r <= k) && (array[r] < array[l]))
    {
        smallest = r;
    }
    if (array[smallest] < array[i])
    {
        int temp = array[i];
        array[i] = array[smallest];
        array[smallest] = temp;
    }

}

void insert_min_heap(int *array, int k)
{
    int p = 1;
    int l, r;
    while (p < k)
    {
        l = l_child(p);
        r = r_child(p);
        int smallest;
        if ((r <= k) && (array[r] < array[l]))
            smallest = r;
        else if (l <= k && array[l] < array[smallest])
            smallest = l;
        else
            return;
        int temp;
        temp = array[p];
        array[p] = array[smallest];
        array[smallest] = temp;
        p = smallest;
    }
}

void build_heap_min(int *array, int k)
{
    int start = k / 2;
    for (int i = start; i >= 1; i--)
        min_heapify_recur(array, i, k);
    return;
}

void top_k(int *nums, int length, int k, int *res)
{
    if (length < k || k <= 0)
        return;
    int *new_array = new int[length + 1];
    new_array[0] = 0;
    for (int i = 0; i < length; i++)
        new_array[i + 1] = nums[i];
    build_heap_min(new_array, k);
    for (int i = k+1; i < length; i++)
    {
        if (new_array[i] < new_array[1])
            new_array[1] = new_array[i];
        insert_min_heap(new_array, k);
    }
}


int main()
{
    return 0;
}