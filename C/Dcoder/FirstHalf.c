#include <stdio.h>
#include <string.h>
//Compiler version gcc 6.3.0

int main(void)
{
	char s[] = "";
	scanf("%s", s);
	unsigned l = strlen(s)/2;
	s[l] = '\0';
	printf("%s", s);
	return 0;
}
