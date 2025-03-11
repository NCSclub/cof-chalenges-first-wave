#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc<2) return 0;
    char* s; sprintf(s, "echo %s", argv[1]);
    system(s);
    return 0;
}
