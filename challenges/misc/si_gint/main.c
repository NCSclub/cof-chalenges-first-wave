#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
char* messages[] = {" don't do that", " Stop", " No", " cof{ju5T_5t0p_m4N}"};
int i = 0;
void catchsig(){ puts(messages[i++]); if(!(4-i)) exit(0); }
int main(int argc, char *argv[]) {
    signal(SIGINT, catchsig); puts("what is you name?");
    scanf(" %s", NULL);       puts("that's crazy man");
    return 0;
}
