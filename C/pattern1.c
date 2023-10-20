#include<stdio.h>
#include<conio.h>

int main(){
	int n,i,j;
	char ch='*';
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(i==1 || j==1 || i==n || j==n)
			{
				printf("%c",ch);
			}
			else{
				printf(" ");  
			}
		}
		printf("\n");
	}
}
