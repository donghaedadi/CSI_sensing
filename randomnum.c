#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
     
    int i;
    int b;
    srand(time(NULL));


    for (i = 1; i <= 10; i++){
        b =rand() % 100 +1;
        printf("%d ", b);
        }
    printf("\n");
}