#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	scanf("%d",&n);
	vector<int> ar(n);
	vector<int> freq(100,0); // frequency of numbers from 0 to 99
	for(int i=0; i < n; ++i) {
		int temp;
		scanf("%d",&temp);
		ar[i] = temp;
		freq[temp]++;
	}
	for (const int& i: freq) {
		printf("%d ",i);
	}
	return 0;
}