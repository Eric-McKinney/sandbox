#include <stdio.h>
#include <stdlib.h>

int main() {
    char *ptr = malloc(0);

    /* will either print NULL or an address which is fine to free() */
    printf("malloc(0) = %p\n", ptr);

    free(ptr);
    return 0;
}
