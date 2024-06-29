#include <stdio.h>

int main() {
    if (1) {
        int a = 200;
    } else {
        int a = 400;
    }
    /**********************************************/
    /* a is limited to the if statement scope, so */
    /* below line causes a compilation error      */
    /**********************************************/

    /*printf("%d\n", a);*/

    return 0;
}
