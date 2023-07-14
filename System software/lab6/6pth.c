#include <stdio.h>
#include <math.h>
#include <pthread.h>

#define NUM_THREADS 4

typedef struct {
    int from, to;
    long double step, res, a;
} IntegrateTask;

long double f(long double x) {
    if (x <= 1) {
        return cos(x)*exp(-pow(x, 2));
    }
    return log(x + 1) - sqrt(4 - pow(x, 2));
}

long double integrate(int from, int to, long double h) {
    long double sum = 0.0;

    for (int i = from; i < to; i++) {
        long double x = from + (i + 0.5) * h;
        long double partial_sum = f(x) * h;
        sum += partial_sum;
    }
    return sum;
}

void * integrateThread(void * data) {
    IntegrateTask* task = (IntegrateTask *)data;

    long double sum = 0.0;
    for (int i = task->from; i < task->to; i++) {
        long double x = task->a + (i + 0.5) * task->step;
        long double partial_sum = f(x) * task->step;
        sum += partial_sum;
    }

    task->res=sum;
    pthread_exit(NULL);
}

long double integrateTreads(int n, int a, long double h) {
    pthread_t threads[NUM_THREADS];
    IntegrateTask tasks[NUM_THREADS];

    int distance = n / NUM_THREADS;

    for (int i=0; i < NUM_THREADS; ++i) { // создаем задания и потоки
        tasks[i].from = i*distance; // задаем "от"
        tasks[i].to = (i+1)*distance; // задаем "до"
        tasks[i].step = h; // задаем "шаг"
        tasks[i].a = a;

        if (i == NUM_THREADS - 1) {
            tasks[i].to = n;
        }

        pthread_create(&threads[i], NULL, integrateThread, (void*)&tasks[i]); // создание потоков и передача параметров (задания)
    }

    long double res = 0;
    for (int i=0; i < NUM_THREADS; ++i) {
        pthread_join(threads[i], NULL);
        res += tasks[i].res;
    }
    return res;
}

int main() {
    long double a = 0.0; 
    long double b = 2.0; 
    long double eps = 1e-13;

    int n = 1000;
    long double h = (b - a) / n;
    long double prev_sum = 0.0;
    long double sum = 0.0;

    do {
        prev_sum = sum;
        sum = integrateTreads(n, a, h);

        n *= 2;
        h /= 2;
    } while (fabsl(sum - prev_sum) > eps);


    printf("%.20Lf\n\n", sum);
    return 0;
}