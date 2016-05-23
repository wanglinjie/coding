/*
* Author: MSRP
* Create Time  : 20160127
* Last Modified: 
* 中国象棋将帅问题
*/
//#include <stdio.h>
#include <iostream>
using namespace std;

struct {
    unsigned char a:4;
    unsigned char b:4;
} i;

int main()
{
    for(i.a = 1; i.a <= 9; i.a++)
        for(i.b = 1; i.b <= 9; i.b++)
            if(i.a % 3 != i.b % 3)
                cout<<"A = "<<int(i.a)<<", B = "<<int(i.b)<<endl;
    return 0;
}