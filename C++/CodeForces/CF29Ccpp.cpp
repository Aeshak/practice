#include <bits/stdc++.h>
using namespace std;
//Compiler version g++ 6.3.0
typedef unordered_map<string,vector<string>> dictionary;
void addEdge(dictionary& dict,const string& v,const string& w) {
	dict[v].push_back(w);
	dict[w].push_back(v);
}

int main()
{
	dictionary dict;
	int n;
	scanf("%d", &n);
	for(int i=0; i<n;++i) {
		char a[20],b[20];
		scanf("%s %s",a,b);
		addEdge(dict,string(a),string(b));
	}
	string root;
	for(const auto& i: dict){
		if (i.second.size() == 1) {
			root = i.first;
		}
	}
	printf("%s ",root.c_str());
	string out = root;
	string p = root;
	while(1) {
		for (const auto& i: dict[p]) {
			if (i == out) {
				continue;
			}
			if (p != root) {
				out = p;
				printf("%s ",out.c_str());
			}
			p = i;
			break;
		}
		if (dict[p].size() == 1) {
			break;
		}
	}
	printf("%s",p.c_str());
	
	return 0;
}