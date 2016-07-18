#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int middle;
        int low_val, middle_val, high_val;
        while(low <= high)
        {
            middle = low + (high - low)/2;
            low_val = nums[low];
            middle_val = nums[middle];
            high_val = nums[high];
            cout<<low<<" "<<high<<" "<<middle<<" "<<endl;
            cout<<"value: "<<low_val<<" "<<middle_val<<" "<<high_val<<" "<<target<<endl;
            if ((low_val<target && target<middle_val) || (middle_val<low_val && low_val<target) || (target<middle_val && middle_val<low_val))
                high = middle - 1;
            // else if ((middle_val<target && target< high_val) || (target<high_val && high_val<middle_val) || (low_val<middle_val && middle_val<target))
            else if ((middle_val<target && target< high_val) || (target<high_val && high_val<middle_val) || (high_val<middle_val && middle_val<target))
                low = middle + 1;
            else
                break;
        }
        if (nums[low] == target)
            return low;
        else if (nums[middle] == target)
            return middle;
        else if (nums[high] == target)
            return high;
        else
            return -1;
    }
};

int main()
{
    /*int array[] = {3, 4, 5, 1, 2};
    vector<int> nums;
    int target = 2;
    for (int i = 0; i < sizeof(array)/sizeof(int); i++)
        nums.push_back(array[i]);
    cout<<sizeof(array)/sizeof(int)<<endl;
    cout<<nums.size()<<endl;
    Solution so;
    cout<<so.search(nums, target)<<endl;*/
    /*int a = 2;
    int b = 1;
    int c = 3;
    if (a<b<c)
    {
        cout<<"True"<<endl;
    }
    else
        cout<<"False"<<endl;*/
    string a = "hello";
    cout<<a.substr(1, 3)<<endl;
    return 0;
}