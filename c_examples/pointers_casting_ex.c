#include <stdio.h>
#include <strings.h>

int main() {
    float m = 7.0;
    int *a = (int *) &m;
    float *a2 = &m;
    
    printf("m: %f\na: %p\n*a: %d\n(int) *a: %d\na2: %p\n*a2: %f\n(int) *a2: %d\n", 
           m, (void *) a, *a, (int) *a, (void *) a2, *a2, (int) *a2);

    return 0;
}
