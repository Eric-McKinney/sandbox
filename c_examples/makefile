CC=gcc
CFLAGS= -ansi -Wall -g -O0 -Wwrite-strings -Wshadow -pedantic-errors \
	-fstack-protector-all

SRC=$(wildcard *_ex.c)
PROGS=$(patsubst %.c,%,$(SRC))

.PHONY: all clean ex example test

all: $(PROGS)

%_ex: %_ex.c
	$(CC) $(CFLAGS) -o $@ $<

readline_ex: readline_ex.c
	$(CC) $(CFLAGS) -o $@ $< -lreadline

test:
	@echo Source: $(SRC)
	@echo Progs: $(PROGS)

ex: example
example:
	@cp ./.ex_template new_ex.c
	@echo "Example new_ex.c made from template"

clean:
	rm -f a.out $(PROGS)
