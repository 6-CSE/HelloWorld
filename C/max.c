#include <stdio.h>
int main(){
	int i,n,max,pos;
	printf("Enter the number of elements in the array: ");
	scanf("%d",&n);
	int a[n];
	printf("Enter array elements: ");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	pos=0;
	max=a[0];
	 	for(i=1;i<n;i++){
		if(a[i]>a[0]){
			pos=i;
			max=a[i];
		}
	}
	printf(" The maximum element of the array is %d",max);
}
