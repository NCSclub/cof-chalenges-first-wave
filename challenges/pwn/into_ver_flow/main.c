#include <stdio.h>
int main(){
    int xtal = 4294967200; int tha; 
    scanf("%d", &tha); for(; tha!=0; tha--) xtal++;
    if(xtal==1) puts("<flag>"); return 0;
}
