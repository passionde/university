#include <stdio.h>
#include <stdlib.h>
void print_matrix(int i, int j, int arr[][j])
{
  for(int line = 0; line < i; line++)
  {
    for(int row = 0; row < j; row ++)
    {
      printf("% 4d ", arr[line][row]);
    }
  printf("\n");
  }
  printf("\n");
}

void sum_AB(int i, int j, int A[][j], int B[][j], int AB[][j])
{
  for(int line = 0; line < i; line++)
  {
    for(int row = 0; row < j; row ++)
    {
      AB[line][row] = A[line][row] + B[line][row];
    }
  }
}

// Функция генерации массива с слуяайными числами от -100 до 100
void generate_arr(int i, int j, int arr[][j])
{
  for(int line = 0; line < i; line++)
  {
    for(int row = 0; row < j; row ++)
    {
      arr[line][row] = rand() % 201 - 100;
    }
  }
}

int main()
{
  // Ввод с клавиатуры размерности матрицы
  int i, j;
  printf("Введите размерность матрицы:\n");
  printf("     Количество строк --> ");
  scanf("%d", &i);
  printf("  Количество столбцов --> ");
  scanf("%d", &j);

  // Генерация матриц A и B
  int A[i][j];
  printf("\nМатрица A:\n");
  generate_arr(i, j, A);
  print_matrix(i, j, A);

  int B[i][j];
  printf("Матрица B:\n");
  generate_arr(i, j, B);
  print_matrix(i, j, B);

  // Сложение матриц A и B
  int AB[i][j];
  printf("Матрица A+B:\n");
  sum_AB(i, j, A, B, AB);
  print_matrix(i, j, AB);

  return 0;
}
