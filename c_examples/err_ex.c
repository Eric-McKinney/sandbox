#include <stdio.h>
#include <err.h>   /* used by err funcs & warn funcs */
#include <error.h> /* used by error */
#include <errno.h> /* used to define errno */

/* perror(str)						prints str followed by the error msg associated w/errno value to stderr
 * error(status, errnum, fmt_str)	exit w/status as exit code if status != 0, print msg same as err does
 * error_at_line(status, errnum, fname, lineno, fmt_str)	like error, but includes fname and lineno in msg
 *
 * err family of functions:		 	flush stdout, print a msg to stderr, & exit w/status as exit code
 * err(status, fmt_str)			 	prints prog name, fmt_str, & error msg associated w/errno value
 * errx(status, fmt_str)		 	same as err, but without the error msg associated w/errno value
 * verr(status, fmt_str, va_list)	same as err, but fmt_str variables are passed in as va_list type
 * verrx(status, fmt_str, va_list) 	same as errx, but fmt_str variables are passed in as va_list type
 *
 * warn family of functions:		same as err functions but don't exit
 * warn(fmt_str)
 * warnx(fmt_str)
 * vwarn(fmt_str, va_list)
 * vwarnx(fmt_str, va_list)
 */

void a_func() {
    errno = 1;
    printf("errno set: %d\n", errno);
}

void print_separator(const char *header) {
    printf("\n---%s---\n", header);
}

int main() {
    int a = 10;
    char s[] = "a string";

    a_func();

    if (errno != 0) {
        print_separator("perror");
        perror("(regular str here since format str not supported)");

        print_separator("error");
        error(0, errno, "(format str here: a = %d, s = %s)", a, s);

        print_separator("error_at_line");
        /* __FILE__ and __LINE__ are preprocessor values for the current file & line
         * other values can be used, but I used them because it's cool that they exist
         */
        error_at_line(0, errno, __FILE__, __LINE__, "(format str here: a = %d, s = %s)", a, s);
        
        print_separator("warn");
        warn("(format str here: a = %d, s = %s)", a, s);

        print_separator("warnx");
        warnx("(format str here: a = %d, s = %s)", a, s);

        print_separator("err");
        err(0, "(format str here: a = %d, s = %s)", a, s);

        /* doesn't get run bc err exits */
        print_separator("errx");
        errx(0, "(format str here: a = %d, s = %s)", a, s);
    }

    return 0;
}
