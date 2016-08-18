#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;


int apples()
{
    /*
分苹果
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，使得最后所有奶牛拥有的苹果数

都相同，每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，问最少需要移动多少次可以平分苹

果，如果方案不存在输出 -1。 
输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100），接下来的一行包含 n 

个整数 ai（1 <= ai <= 100）。


输出描述:
输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。

输入例子:
4
7 15 9 5

输出例子:
3
    */
    // 思路：就是和平均值相差应该为2的倍数
    int n;
    vector<int> a;
    cin>>n;
    int total = 0;
    int temp;
    for(int i = 0; i < n; ++i)
    {
        cin>>temp;
        a.push_back(temp);
        // 计算总的苹果数
        total += temp;
    }
    // 如果总苹果数和牛的数量不能整除，则返回-1
    if (total % n != 0)
        return -1;
    int avg = total / n;
    int ret = 0;
    for(int i = 0; i < n; ++i)
    {
        a[i] -= avg;
        // 如果相差为奇数，则不存在
        if (a[i] & 0x1)
            return -1;
        // 计算总的需要移动的次数
        if (a[i] > 0)
            ret += (a[i] / 2);
    }
    return ret;
}


int fly()
{
    /*
    航天飞行器是一项复杂而又精密的仪器，飞行器的损耗主要集中在发射和降落的过程，
    科学家根据实验数据估计，如果在发射过程中，产生了 x 程度的损耗，
    那么在降落的过程中就会产生 x^2 程度的损耗，
    如果飞船的总损耗超过了它的耐久度，飞行器就会爆炸坠毁。
    问一艘耐久度为 h 的飞行器，假设在飞行过程中不产生损耗，
    那么为了保证其可以安全的到达目的地，只考虑整数解，
    至多发射过程中可以承受多少程度的损耗？ 
输入描述:

每个输入包含一个测试用例。每个测试用例包含一行一个整数 h （1 <= h <= 10^18）。


输出描述:

输出一行一个整数表示结果。

输入例子:

10

输出例子:

2

解方程组：
x+x^2 <= h
而x应该是整数
    */
    int h;
    cin>>h;
    int ret;
    ret = int((-1+sqrt(1+4*h))/2);
    return ret;
}


const int N = 10010;
char str[100];
int a[110][110];
int sum[110][110], n, m;

// // 求左上顶点(i,j)到右下顶点(x,y）确定的田地的价值和
int calc(int x, int y, int i, int j)
{
    return sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j];
}

bool judge(int x)
{
    for(int i = 1; i <= m-3; i++)
    {
        for(int j = i+1; j <= m-2; k++)
        {
            for(int k = j+1; k<= m-1; k++)
            {
                int last = 0, cnt = 0;
                for(int r=1; r<=n; r++)
                {
                    int s1 = calc(r, i, last, 0);
                    int s2 = calc(r, j, last, i);
                    int s3 = calc(r, k, last, j);
                    int s4 = calc(r, m, last, k);
                    // 当前横一刀满足条件
                    if (s1 >= x && s2 >= x && s3 >= x && s4 >= x)
                    {
                        last = r;
                        cnt++;
                    }
                }
                //表明当前x是16块田地中最小的，返回true
                if(cnt >= 4)
                    return true;
            }
        }
    }
    return false;
}

int land()
{
    /*
    牛牛和 15 个朋友来玩打土豪分田地的游戏，牛牛决定让你来分田地，地主的田地可以看成是一个矩形，每个位

置有一个价值。分割田地的方法是横竖各切三刀，分成 16 份，作为领导干部，牛牛总是会选择其中总价值最小

的一份田地， 作为牛牛最好的朋友，你希望牛牛取得的田地的价值和尽可能大，你知道这个值最大可以是多少吗

？ 
输入描述:
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 75），表示田地的大

小，接下来的 n 行，每行包含 m 个 0-9 之间的数字，表示每块位置的价值。


输出描述:
输出一行表示牛牛所能取得的最大的价值。

输入例子:
4 4
3332
3233
3332
2323

输出例子:
2

二分答案，判断可行性时暴力枚举三列的情况，然后横着贪心地扫一遍，每当四个都满足时就砍一刀，满足四次

即可，复杂度O(N^4logN)
    */
    
    while(scanf("%d%d", &n, &m) > 0)
    {
        for(int i = 1; i <= n; i++)
        {
            scanf("%s", str+1);
            for(int j = 1; j <= m; j++)
                a[i][j] = str[j] - '0';
        }
        memset(sum, 0, sizeof sum);
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= m; j++)
                // sum[i][j]表示坐标(i,j)左上方价值总和
                sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + a[i][j];
        }

        int l = 0, r = sum[n][m], ans = 0;
        // sum[n][m]表示所有价值总和
        while (l <= r)
        {
            int m = (l + r) >> 1;

            // 表明m是16块田地最小的
            if(judge(m))
            {
                l = m + 1;
                ans = m;
            }
            else
            {
                r = m - 1;
            }
        }
        cout<<ans<<endl;
    }
}



int main()
{
    int result = fly();
    cout<<result<<endl;
    return 0;
}