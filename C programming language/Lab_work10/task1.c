#include <stdio.h>
#include <stdlib.h>
// Функция динамического выделения памяти
int *gen_adrr(int i, int j) {
  int *A = (int *)malloc(i * j * sizeof(int));
  if (!A) {
    printf("Memory allocation error!\n");
    exit(EXIT_FAILURE);
  }
  return A;
}

// Функция печати матрицы
void print_matrix(int i, int j, int arr[]) {
  for (int line = 0; line < i; line++) {
    for (int row = 0; row < j; row++) {
      printf("% 4d ", arr[line * j + row]);
    }
    printf("\n");
  }
  printf("\n");
}

// Функция суммирования двух матриц
void sum_AB(int i, int j, int A[], int B[], int AB[]) {
  for (int line = 0; line < i; line++) {
    for (int row = 0; row < j; row++) {
      AB[line * j + row] = A[line * j + row] + B[line * j + row];
    }
  }
}

// Функция генерации массива с случайными числами от -100 до 100
void generate_arr(int i, int j, int arr[]) {
  for (int line = 0; line < i; line++) {
    for (int row = 0; row < j; row++) {
      arr[line * j + row] = rand() % 201 - 100;
    }
  }
}

int main() {
  // Ввод с клавиатуры размера матрицы
  int i, j;
  printf("Введите размер матрицы:\n");
  printf("     Количество строк --> ");
  scanf("%d", &i);
  printf("  Количество столбцов --> ");
  scanf("%d", &j);

  // Генерация матриц A и B
  int *A = gen_adrr(i, j);
  printf("\nМатрица A:\n");
  generate_arr(i, j, A);
  print_matrix(i, j, A);

  int *B = gen_adrr(i, j);
  printf("Матрица B:\n");
  generate_arr(i, j, B);
  print_matrix(i, j, B);

  // Сложение матриц A и B
  int *AB = gen_adrr(i, j);
  printf("Матрица A+B:\n");
  sum_AB(i, j, A, B, AB);
  print_matrix(i, j, AB);

  // Освобождение памяти
  free(A);
  free(B);
  free(AB);
  return 0;
}
