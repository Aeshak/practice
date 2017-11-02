#include <stdio.h>
// using namespace std;
//Compiler version g++ 6.3.0

int main()
{
	int n;
	scanf("%d", &n);
	int prev,next,x,i;
	for (i=0;i<n;++i) {
		scanf("%d",&next);
		if (i>=2) {
			if ((prev&1) != (x&1) && (x&1) != (next&1)) {
				break;
			} 
			else if ((prev&1) != (x&1) && (x&1) == (next&1)) {
				--i;
				break;
			}
			else if ((prev&1) == (x&1) && (x&1) != (next&1)) {
				++i;
				break;
			}
		}
		prev = x;
		x = next;
	}
	printf("%d",i);
	return 0;
}