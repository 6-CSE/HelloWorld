#include<stdio.h>

int main(){
    printf("Hello World!\n");
    int number,i,j;
    printf("\n\nEnter the integer number in decimal number system\n");
    scanf("%d",&number);
    
    printf("%d in binary number is : \n",number);
    for (i=31;i>=0;i--)
    {
        j = number >> i;
        if (j & 1)
            printf("1");
        else
            printf("0");
    }
    printf("\n");
    return 0;
}
