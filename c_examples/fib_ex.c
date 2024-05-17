#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long fib(unsigned long n) {
    unsigned long f;

    if (n == 0 || n == 1) {
        return n;
    } 

    f = fib(n - 1) + fib(n - 2);
    printf("fib(%lu) = %lu\n", n, f);

    return f;
}

unsigned long fib2(int n) {
    unsigned long *fibs;
    unsigned long f;
    int i;

    fibs = malloc(sizeof(unsigned long) * n);
    if (fibs == NULL) {
        printf("Malloc error\n");
        exit(1);
    }

    fibs[0] = 1;
    fibs[1] = 1;
    printf("fib(1) = 1\nfib(2) = 1\n");

    for (i = 2; i < n; i++) {
        fibs[i] = fibs[i - 1] + fibs[i - 2];
        printf("fib(%d) = %lu\n", i+1, fibs[i]);
    }

    f = fibs[n - 1];
    free(fibs);
    return f;
}

int main(int argc, char **argv) {
    int n, rec;
    unsigned long f;
    char use_rec[80] = {0};

    if (argc == 1) {
        printf("fibonacci(x), x = ");
        scanf("%d", &n);
        printf("Use the recursive implementation [y/n]? ");
        scanf("%s", use_rec);
        rec = strcmp(use_rec, "y") == 0 || strcmp(use_rec, "yes") == 0;
    } else if (argc == 3) {
        n = atoi(argv[1]);
        strcpy(use_rec, argv[2]);
        rec = strcmp(use_rec, "y") == 0 || strcmp(use_rec, "yes") == 0;
    } else {
        printf("Usage: %s <int> <y/n>\n", argv[0]);
        return 1;
    }

    f = rec? fib((unsigned long) n) : fib2((unsigned long) n);
    printf("Result: %lu\n", f);

    return 0;
}
