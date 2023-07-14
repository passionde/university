#include <stdio.h>
int check1(int n, int div)
{
  if (div == 1)
    return 1;

  if (!(n % div))
    return 0;
  else
    return check1(n, div-1);
}

int check2(int n)
{
  for (int div = 2; div < n; div ++)
  {
    if (!(n % div))
     return 0;
  }

  return 1;
}

int main()
{
  //Получение числа
  int n;
  printf("Введите натуральное число --> ");
  scanf("%d", &n);

  if (n == 1)
  {
    printf("Число 1 не является ни простым, ни составным\n");
    return 0;
  }

  // Вывод результата первой функции
  printf("Результат первой функции: число %d - ", n);
  check1(n, n-1) ? printf("простое\n") : printf("составное\n");

  // Вывод результата второй функции
  printf("Результат второй функции: число %d - ", n);
  check2(n) ? printf("простое\n") : printf("составное\n");
  return 0;
}
