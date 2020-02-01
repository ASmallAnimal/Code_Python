#include<stdio.h>
int main()
{
    FILE* fp1=fopen("D:/txt/output.txt","w+");
    char* s;
    fscanf(fp1,"%s",s);
    printf("%s",s);
}