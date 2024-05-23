#include <stdio.h>

int main() {
    int x;

    printf("Enter a number: ");
    scanf("%d", &x);

    switch(x) {
        case 1:
            printf("a");
        case 2:
            printf("b");
            break;
        case 3:
            printf("c");
        case 4:
            printf("d");
        case 5:
            printf("e");
    }

    printf("\n");

    return 0;
}
