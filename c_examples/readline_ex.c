#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>

/*
 * Compile this file with the -lreadline flag
 */

int not_empty(char *str) {
    return (str != NULL && *str != '\0');
}

int main() {
    char line1[1024];
    char *line2;

    printf("Using fgets. Hit Ctrl+D to proceed to readline.\n");
    printf("> ");
    while (fgets(line1, 1024, stdin)) {
        printf("you said \"%s\"\n", line1);
        printf("> ");
    }

    printf("\nUsing readline. Hit Ctrl+D to exit.\n");
    while ((line2 = readline("> "))) {
        printf("you said \"%s\"\n", line2);

        if (not_empty(line2)) {
            add_history(line2);
        }
    }

    return 0;
}
