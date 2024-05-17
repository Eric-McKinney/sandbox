#include <stdio.h>

int main() {
    int a = 0xabcd;
    int b = 0x0dc0;
    
    /* (a << 8) = 0xcd00 */
    int part1 = (a << 8) & 0x0F00; /* 0x0d00 */

    int part2 = a & 0x00F0; /* 0x00c0 */

    int result = part1 | part2;

    printf("%x\n", result);

    return 0;
}

