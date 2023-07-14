#include <stdio.h>
#include <stdlib.h>

// Факториал
int factorial(int n){
    int r = 1;
    for (int i = 1; i <= n; i++)
        r *= i;
    return r;
}

// печать массива arr длиной i
void print_arr(int i, int arr[])
{
  for(int idx = 0; idx < i; idx++)
  {
    printf("% 4d ", arr[idx]);
  }
  printf("\n");
}

// Функция генерации массива с случайными числами от -100 до 100
void generate_arr(int i, int arr[])
{
  for(int idx = 0; idx < i; idx++)
  {
    arr[idx] = rand() % 201 - 100;
  }
}

int main(){
  int n;
  printf("Введите число: ");
  scanf("%d", &n);

  printf("%d - результат\n", factorial(n));
  return 0;
}
