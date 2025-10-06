#include <stdio.h>
#include <stddef.h>

int main() {
    size_t size = 0;
    int negative_int = -4;
    size--;  /* wrap around to max value */

    printf("negative integer before cast: %d\n", negative_int);
    printf("negative integer after cast to unsigned int: %u\n", (unsigned int) negative_int);
    printf("size_t max value: %lu\n", size);
    printf("size_t max value after cast to int: %d\n", (int) size);

    return 0;
}
