#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>

#define NUM_THREADS 4

typedef struct
{
    unsigned int low;
    unsigned int high;
    int * res;
} thread_data;

thread_data thread_data_arr[NUM_THREADS];

int * res;

void *calc_part(void *threadarg)
{
    thread_data *my = (thread_data *)threadarg;
    unsigned int i, j;
    int flag = 0;
    
    for (i = my->low; i < my->high + 1; i++)
    {
        double sq = sqrt(i);
        flag = 0;
        for (j = 2; j <= sq; j++)
            {
                if (i % j == 0 || i == 2)
                {
                    flag = 1;
                    break;
                }
            }
            if (!flag) 
            {
                //printf("%d\n", i);
                my->res[i - my->low]++;
            }
    }

    pthread_exit(NULL);
}

int main()
{
    unsigned int i;
    int low, high;
    scanf("%ud", &low);  
    scanf("%ud", &high); 
    pthread_t threads[NUM_THREADS];
    pthread_attr_t attr;
    int rc;
    void *status;
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for (i = 0; i < NUM_THREADS; i++)
    {
        thread_data_arr[i].low = low; 
        thread_data_arr[i].high = high; 
        thread_data_arr[i].res = (int *)malloc(sizeof(int) * (high - low + 1));
        rc = pthread_create(&threads[i], &attr, calc_part, (void *)&thread_data_arr[i]);
        if (rc)
        {
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            exit(EXIT_FAILURE);
        }
    }
    pthread_attr_destroy(&attr);
    for (i = 0; i < NUM_THREADS; i++)
    {
        rc = pthread_join(threads[i], &status);
        if (rc)
        {
            printf("ERROR; return code from pthread_join() is %d\n", rc);
            exit(EXIT_FAILURE);
        }
    }
    for (i = 0; i <= high - low + 1; i++ )
    {
        if (thread_data_arr[0].res[i])
            printf("%d\n", i + 1);
    }
    return 0;
}
