NAME = lab04
SQLITE = $(NAME)_sqlite

SRC = $(NAME).c
OBJ = $(NAME).o
SQLITE_SRC = $(SQLITE).c
SQLITE_OBJ = $(SQLITE).o

ifeq ($(OS),Windows_NT)
	EXEC := $(NAME).exe
	LDLIBS := -mwindows
else
	EXEC := $(NAME)
endif

CC = gcc
LDLIBS += -lsqlite3 `pkg-config --libs gtk+-3.0 gmodule-2.0`
CFLAGS = -Wall -g `pkg-config --cflags gtk+-3.0 gmodule-2.0`

$(EXEC): $(OBJ) $(SQLITE_OBJ)
	$(CC) $(OBJ) $(SQLITE_OBJ) -o $(EXEC) $(LDLIBS)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC)

$(SQLITE_OBJ): $(SQLITE_SRC)
	$(CC) -Wall -c $(SQLITE_SRC)


clean:
	rm -f $(EXEC)
	rm -f *.o
