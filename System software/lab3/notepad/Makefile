# x86_64-w64-mingw32-gcc notebook.c -o notebook.exe -Wall -mwindows -lcomctl32

NAME = notebook
SRC = $(NAME).c
EXEFILE = $(NAME).exe

CC = x86_64-w64-mingw32-gcc
CFLAGS = -Wall -mwindows -lcomctl32

build_and_run: $(EXEFILE)
	wine $(EXEFILE)

$(EXEFILE): $(SRC)
	$(CC) $(SRC) -o $(EXEFILE) $(CFLAGS)

clean:
	rm -f $(EXEFILE)