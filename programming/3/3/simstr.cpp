/*
计算两个字符串之间的距离
*/
#include <iostream>
#include <string>
using namespace std;

int CalculateStringDistance(string strA, int pABegin, int pAEnd, string strB, int pBBegin, int pBEnd)
{
    if (pABegin > pAEnd)
    {
        if (pBBegin > pBEnd)
            return 0;
        else
            return pBEnd - pBBegin + 1;
    }
    if (pBBegin > pBEnd)
    {
        if (pABegin > pAEnd)
        {
            return 0;
        }
        else
        {
            return pAEnd - pABegin + 1;
        }
    }
    if (strA[pABegin] == strB[pBBegin])
    {
        return CalculateStringDistance(strA, pABegin + 1, pAEnd, strB, pBBegin + 1, pBEnd);
    }
    else
    {
        int t1 = CalculateStringDistance(strA, pABegin, pAEnd, strB, pBBegin + 1, pBEnd);
    }
}


class stack
{
public:
    stack()
    {
        stackTop = -1;
        maxStackItemIndex = -1;
    }
    void Push(Type X)
    {
        stackTop++;
        if (stackTop >= MAXN);
        else
        {
            stackItem[stackTop] = x;
            if (x > Max())
            {
                link2NextMaxItem(stackTop) = maxStackItemIndex;
                maxStackItemIndex = stackTop;
            }
            else
                link2NextMaxItem[stackTop] = -1;
        }
    }
    Tyep Pop()
    {
        Type ret;
        if (stackTop < 0)
            ThrowException();
        else
        {
            ret = stackItem[stackTop];
            if (stackTop == maxStackItemIndex)
            {
                maxStackItemIndex = link2NextMaxItem[stackTop];
            }
            stackTop--;
        }
        return ret;
    }

    Type Max()
    {
        if (maxStackItemIndex >= 0)
            return stackItem[maxStackItemIndex]
        else
            return -INF;
    }
private:
    Type stackItem[MAXN];
    int stackTop;
    int link2NextMaxItem[MAXN];
    int maxStackItemIndex;
};

class Queue
{
public:
    Type MaxValue(Type x, Type y)
    {
        if (x > y)
            return x;
        else
            return y;
    }
    
};



