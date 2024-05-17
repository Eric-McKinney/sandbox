#include <stdio.h>
#include <string.h>

int main() {
    int x, y;
    int *p1 = &x, *f;
    int **p2, **p2_initial;
    int **p3, **p3_initial;
    
    /* 
     * Assignment below guarantees no segfault occurs (let's pretend p2 was
     * assigned this memory by chance) 
     *
     * You can comment it out to see what happens when p2 is truly 
     * uninitialized (potential segfault)
     */
    p2 = &f;

    p2_initial = p2;
    p3_initial = p3;

    printf("Initial values\np2: %p\np3: %p\n", (void *) p2, (void *) p3);

    *p2 = p1;
    p3 = &p1;
    
    printf("\nAfter assignments\n");
    printf("%s\n", (p2 == p2_initial)? "p2 did not change" : "p2 changed");
    printf("%s\n", (p3 == p3_initial)? "p3 did not change" : "p3 changed");
    
    printf("\nBefore changing p1\n");
    printf("*p2: %p\n*p3: %p\n", (void *) *p2, (void *) *p3);

    p1 = &y;

    printf("\nAfter changing p1\n");
    printf("*p2: %p\n*p3: %p\n", (void *) *p2, (void *) *p3);
    printf("%s\n", (*p2 == *p3)? 
        "Change in p1 reflected in both *p2 and *p3" : 
        "Change in p1 not reflected in *p2");

    return 0;
}
