FLAGS=-Wall
SUF_FLAGS=-lm

all: sync_var pth_var omp_var task

sync_var:
	gcc $(FLAGS) 6.c -o lab6_1 $(SUF_FLAGS)

pth_var:
	gcc $(FLAGS) 6pth.c -o lab6_2 $(SUF_FLAGS) -pthread

omp_var:
	gcc $(FLAGS) 6omp.c -o lab6_3 $(SUF_FLAGS) -fopenmp

task:
	gcc $(FLAGS) 6var.c -o lab6_task $(SUF_FLAGS)

run:
	time ./lab6_1
	time ./lab6_2
	time ./lab6_1

clean:
	rm lab6_1 lab6_2 lab6_3 lab6_task