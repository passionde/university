#include <stdio.h>
#include <stdlib.h>
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

// Функция поиска индексов максимумов
void find_max(int idx_max[], int max_val[], int arr[], int i) {
  int idx_m = 0;
  int max_v = arr[0];

  for(int iter = 0; iter < 3; iter++){
    for(int idx = 1; idx < i; idx++){
      if(arr[idx] > max_v && idx != idx_max[0] && idx != idx_max[1]){
        max_v = arr[idx];
        idx_m = idx;
      }
    }
    idx_max[iter] = idx_m;
    max_val[iter] = max_v;
    max_v = arr[0];
  }
}

// Функция перезаписи массива по заданию
void rewrite_arr(int max_val[], int idx_max[], int arr[], int i){
  int sum = max_val[0] + max_val[1] + max_val[2];
  int mul = max_val[0] * max_val[1] * max_val[2];
  int write_idx = (idx_max[0] + idx_max[1] + idx_max[2]) % i;

  printf("%d\n", mul);
  printf("%d\n", sum);
  arr[write_idx] = mul - sum;
}

int main()
{
  // Ввод с клавиатуры размера массива
  int i;
  printf("Введите размер массива --> ");
  scanf("%d", &i);

  // Генерация массива arr
  printf("Сгенерированный массив:\n");
  int arr[i];
  generate_arr(i, arr);
  print_arr(i, arr);

  // Массив с индексами максимумов, массив с максимумами
  int max_val[3];
  int idx_max[3] = {0};
  find_max(idx_max, max_val, arr, i);
  printf("Массив максимумов:\n");
  print_arr(3, max_val);
  printf("Массив их индексов:\n");
  print_arr(3, idx_max);

  rewrite_arr(max_val, idx_max, arr, i);
  printf("Измененный массив\n");
  print_arr(i, arr);

  return 0;
}
