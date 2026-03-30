#include<stdio.h>

int main(){
	char a[1000001];
	int g = 0;
	fgets(a, 1000001, stdin);
    bool first=0;
	for (int i = 0;a[i]!='\0'; i++)
	{
        if (!first&&a[i]!=' '){
            g++;
            first=1;
        }
		else if (first&&a[i]==' '){
		    first=0;
        }
		
	}
	printf("%d", g);
}