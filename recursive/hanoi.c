
#include<stdio.h>
void hanoi(char A,char B,char C,int n){
    if(n==1){
        printf("%c-->%c\n",A,C);
    }
    else{
        hanoi(A,C,B,n-1);
        printf("%c-->%c\n",A,C);
        hanoi(B,A,C,n-1);
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    hanoi('A','B','C',n);
}