#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>

/*
 * SIGCHLD sent when child exits regardless if parent is waiting on it or not
 */
void sigchld_handler(int sig) {
    printf("parent: received signal (SIGCHLD = 17): %d\n", sig);
}

int main(int argc, char **argv) {
    pid_t fork_result;
    unsigned int parent_delay, child_delay;

    if (argc != 3) {
        fprintf(stderr, "usage: %s parent_delay_in_seconds child_delay_in_seconds\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    parent_delay = (unsigned int) atoi(argv[1]);
    child_delay = (unsigned int) atoi(argv[2]);

    signal(SIGCHLD, sigchld_handler);

    fork_result = fork();
    if (fork_result < 0) {
        printf("fork failed\n");
        exit(EXIT_FAILURE);
    } else if (fork_result != 0) {  /* parent */
        int status;
        printf("parent: sleeping %u\n", parent_delay);
        sleep(parent_delay);
        printf("parent: done sleeping\n");
        wait(&status);
    } else {  /* child */
        printf("child: sleeping %u\n", child_delay);
        sleep(child_delay);
        printf("child: done sleeping\n");
        exit(EXIT_SUCCESS);
    }

    return 0;
}
