#include <stdio.h>
 //Compiler version gcc 6.3.0

 int main(void)
 {
 	int n,a,b;
 	scanf("%d %d %d", &n,&a,&b);
 	if(n-b-a <= 1)
 		printf("%d", n-a);
 	else
 		printf("%d", b+1);
 	return 0;
 }