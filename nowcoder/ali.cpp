#include <iostream>
using namespace std;

/*
降序数组，如{7,6,5,4,3,2,1}，将数组按最小最大次小次大顺序重新排列{1,7,2,6,3,5,4}
要求时间复杂度（n），空间复杂度（1）。
*/
void resort(int *nums, int n)
{
    if(nums == NULL)
        return;

    int mid = n / 2;

    // 从数字小的一侧开始往右遍历
    for(int i = (n-mid); i < n; i++)
    {
        // 记录当前位置
        int po = i;

        // 如果小于0，表示已经遍历过
        if(nums[po] < 0)
            continue;
        int record = -nums[po];
        do {
            // cout<<"1"<<endl;
            // 当前元素的需要存放的位置
            int new_po;
            if(po >= mid)
            {
                // 当元素位置在小的一侧
                new_po = 2 * (n - po - 1); 
            }
            else
            {
                // 当元素在大的一侧
                new_po = 2 * po + 1;
                // 避免超过数组
                if(new_po >= n)
                    new_po = n-1;
            }
            // 保存新位置元素值
            int temp = nums[new_po];
            // 更新
            nums[new_po] = record;
            record = -temp;
            po = new_po;
        }while(po != i);
    }
    // 将元素改正回来
    for(int i = 0; i < n; i++)
    {
        nums[i] = -nums[i];
    }
}

int main()
{
    int nums[] = {6, 5, 4, 3, 2, 1};
    resort(nums, 6);
    for(int i = 0; i < 6; i++)
    {
        cout<<nums[i]<<" "<<endl;
    }
    return 0;
}