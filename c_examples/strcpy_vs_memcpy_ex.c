#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_char_arr(char *arr, int len) {
    int i;

    printf("_");
    for (i = 0; i < len; i++) {
        printf("%c_", arr[i]);
    }
    printf("\n");
}

int main() {
    char *s = NULL, *s2 = NULL;
    const char *s3 = "abcd";

    s = malloc(strlen(s3) + 1);
    strcpy(s, s3);

    s2 = malloc(strlen(s3) + 1);
    memcpy(s2, s3, strlen(s3) + 1);

    printf("w/strcpy: %s\nw/memcpy: %s\n", s, s2);

    printf("strcpy:\n");
    print_char_arr(s, strlen(s) + 1);
    printf("memcpy:\n");
    print_char_arr(s2, strlen(s2) + 1);

    free(s);
    free(s2);

    return 0;
}
