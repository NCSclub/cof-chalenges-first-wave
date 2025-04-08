#include <stdio.h>
#include <stdlib.h>

int main(){
    srand(0xface); int j = 0; scanf("%d", &j);
    if(j==rand()) puts("<flag>");
    else puts("hint: face");
    return 0;
}
