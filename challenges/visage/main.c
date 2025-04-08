#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
    int j = 0; scanf("%d", &j);
    srand(j); j = rand();
    srand(0xface);
    if(j==rand())puts("<flag>");
    else puts("hint: face");
    return 0;
}
