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

void sort_arr(int i, int neg_num, int pos_num, int A[], int P[], int N[])
{
  for(int idx = i - 1; idx >= 0; idx--)
  {
    A[idx] < 0 ? (N[--neg_num] = A[idx]) : (P[--pos_num] = A[idx]);
  }
}

int main()
{
  // Ввод с клавиатуры размера массива
  int i;
  printf("Введите размер массива --> ");
  scanf("%d", &i);

  // Генерация массива A
  int A[i];
  generate_arr(i, A);

  int pos_num = 0, neg_num = 0;
  for(int idx = 0; idx < i; idx++)
  {
    A[idx] < 0 ? neg_num++ : pos_num++;
  }

  int P[pos_num];
  int N[neg_num];
  sort_arr(i, neg_num, pos_num, A, P, N);

  printf("\nМассив A:\n");
  print_arr(i, A);
  printf("Массив P:\n");
  print_arr(pos_num, P);
  printf("Массив N:\n");
  print_arr(neg_num, N);

  return 0;
}
