#include <iostream>
#include <cmath>
using namespace std;


string findk(int k, int position)
{
    cout<<k<<" "<<position<<endl;
    string ret(position, '4');
    for(int i = 0; i < position; i++)
    {
        if(k & 0x1)
            ret[position-i-1] = '7';
        k >>= 1;
    }
    return ret;
}


int main()
{
    int k;
    cin>>k;
    int i = 1;
    int temp = 0;
    while(true)
    {
        temp = pow(2, i);
        if(k > temp)
        {
            k -= temp;
            i++; 
        }
        else
            break;
    }
    string ret = findk(k-1, i);
    cout<<ret<<endl;
}