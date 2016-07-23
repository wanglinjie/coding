#include <iostream>  
#include <string>  
#include <cstdio>  
#include <cstring>  
#include <cstdlib>  
#include <queue>  
#include <stack>  
  
using namespace std;  
  
const int SIZE = 102;  
  
//边界数组,四个方向，按照下、右、上、左的顺序  
int coordinate[4][2] = {1,0, 0,1, -1,0, 0,-1};  
  
stack<int> sx;  
stack<int> sy;  
stack<int> sxCopy;  
stack<int> syCopy;  
  
int mazeBfs[SIZE][SIZE];  //广搜用的迷宫  
int mazeDfs[SIZE][SIZE];  //深搜用的迷宫  
  
int oddEven[SIZE][SIZE];  //奇偶剪枝状态数组  
  
int n;  //迷宫行数  
int m;  //迷宫列数  
int k;  //封闭房间数  
int kr, kl; //每个封闭房间的行号和列号  
int p, q;  //小鼠a的行号和列号  
int r, s;  //小鼠b的行号和列号  
int ShortestPathLength; //最短路径的长度  
int ShortestPahtNumber; //最短路径的条数  
int ans = 1; //输出第ans条最短路径  
  
//广搜求最短路径长度  
//int BFS(int p, int q, int r, int s, int len, int n, int m);  
int BFS();  
  
//深搜求最短路径条数  
//void DFS(int x, int y, int r, int s, int len, int n, int m, int shortlength);  
void DFS(int x, int y, int len);  
  
int main()  
{  
    while (scanf("%d%d%d", &n, &m, &k) != EOF)  
    {  
        memset(mazeBfs, 0, sizeof(mazeBfs));  //初始化迷宫  
        memset(mazeDfs, 0, sizeof(mazeDfs));  
  
        //奇偶剪枝数组初始化  
        for (int i=0; i<=n; i++)  
        {  
            if (i%2 == 1)  
            {  
               for (int j=0; j<=m; j++)  
               {  
                   if (j%2 == 1)  
                   {  
                       oddEven[i][j] = 1;  
                   }  
                   else  
                   {  
                       oddEven[i][j] = 0;  
                   }  
               }  
            }  
            else  
            {  
                for (int j=0; j<=m; j++)  
                {  
                    if (j%2 == 1)  
                    {  
                        oddEven[i][j] = 0;  
                    }  
                    else  
                    {  
                        oddEven[i][j] = 1;  
                    }  
                }  
  
            }  
        }  
  
        for (int i=1; i<=k; i++)  
        {  
            scanf("%d%d", &kr, &kl);  //输入封闭房间的坐标  
  
            //存入迷宫中，迷宫中，1代表封闭房间，0代表可以走  
            mazeBfs[kr][kl] = 1;  
            mazeDfs[kr][kl] = 1;  
        }  
  
        scanf("%d%d", &p, &q);  //小鼠a的坐标  
        scanf("%d%d", &r, &s);  //小鼠b的坐标  
  
        //求最短路径长度  
        ShortestPathLength = BFS();  
        if (ShortestPathLength == -1) //没路可走时  
        {  
            printf("No Solution!\n");  
            continue;  
        }  
  
        //求最短路径条数及输出所有的最短路径  
        ShortestPahtNumber = 0;  
        sx.push(p);  
        sy.push(q);  
        DFS(p, q, 0);  
  
        //输出结果  
        printf("最短路径长度： %d\n\n", ShortestPathLength);  
        printf("最短路径条数： %d\n\n", ShortestPahtNumber);  
    }  
  
    return 0;  
}  
  
int BFS()  
{  
    queue<int> qx;  //存横坐标的队列  
    queue<int> qy;  //存纵坐标的队列  
    queue<int> qlen;  //存长度的队列  
    int xa, ya; //当前节点坐标  
    int length; //到达当前节点长度  
  
    qx.push(p);  
    qy.push(q);  
    qlen.push(0);  
  
    mazeBfs[p][q] = 1;  
  
    while (!qx.empty())  
    {  
        if ((qx.front()==r) && (qy.front()==s)) //判断是否到达小鼠b  
        {  
            return qlen.front();  
        }  
  
        //临时保存队头值  
        int xx, yy ,ll;  
        xx = qx.front();  
        yy = qy.front();  
        ll = qlen.front();  
  
        //保存完之后，出队  
        qx.pop();  
        qy.pop();  
        qlen.pop();  
  
        for (int i=0; i<4; i++)  
        {  
            //算第i方向上的新值  
            xa = xx + coordinate[i][0];  
            ya = yy + coordinate[i][1];  
            length = ll;  
  
            //新的点在迷宫内，且没有走过  
            if ((xa>=1) && (xa<=n) && (ya>=1) && (ya<=m) && (mazeBfs[xa][ya]==0))  
            {  
                //入队  
                qx.push(xa);  
                qy.push(ya);  
                length += 1;  
                qlen.push(length);  
  
                //标记新点  
                mazeBfs[xa][ya] = 1;  
            }  
        }  
    }  
  
    return -1;  //如果没有路，返回0  
}  
  
void DFS(int x, int y, int len)  
{  
    if ((x==r) && (y==s) && (len==ShortestPathLength))  //找到一条最短路径  
    {  
        ShortestPahtNumber++;  
  
        //输出最短路径  
        printf("最短路径 %3d :\n", ans++);  
        int j = sx.size();  
        for (int i=1; i<=j; i++)  
        {  
           sxCopy.push(sx.top());  
           sx.pop();  
  
           syCopy.push(sy.top());  
           sy.pop();  
        }  
        for (int i=1; i<=j; i++)  
        {  
            printf("(%d, %d) ", sxCopy.top(), syCopy.top());  
            sx.push(sxCopy.top());  
            sxCopy.pop();  
  
            sy.push(syCopy.top());  
            syCopy.pop();  
        }  
        printf("\n\n");  
        return ;  
    }  
  
    //一般剪枝  
    int theoryShortestLength; //当前节点到终点的理论最小值  
    theoryShortestLength = (abs(x-r)) + (abs(y-s));  
    if ((len+theoryShortestLength) > ShortestPathLength) //当前长度+理论最小值>最短路径长度  
    {  
        return ;  
    }  
  
    //奇偶剪枝  
    if ((ShortestPathLength-len)%2 != ((abs(oddEven[x][y]-oddEven[r][s])) % 2))  
    {  
        return ;  
    }  
  
    for (int i=0; i<4; i++)  
    {  
        int xx, yy;  
        xx = x + coordinate[i][0];  
        yy = y + coordinate[i][1];  
  
        if ((xx>=1) && (xx<=n) && (yy>=1) && (yy<=m) && (mazeDfs[xx][yy]==0))  
        {  
            sx.push(xx);  
            sy.push(yy);  
            mazeDfs[xx][yy] = 1;  
            DFS(xx, yy, len+1);  
  
            //回溯  
            sx.pop();  
            sy.pop();  
            mazeDfs[xx][yy] = 0;  
        }  
    }  
}