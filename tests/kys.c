#include <stdio.h>
#include <signal.h>

void catchsig(){
    puts("here's the flag man");
}

int main(int argc, char *argv[]) {
    signal(SIGTERM, catchsig);
    while(1){}
    return 0;
}
