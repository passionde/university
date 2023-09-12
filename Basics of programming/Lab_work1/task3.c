#include <stdio.h>
int main()
{
  //Получение значений от пользователя
  int a, b, c, x, min;
  printf("Введите через пробел значения a, b, c, x\n");
  scanf("%d %d %d %d", &a, &b, &c, &x);

  //Нахождение минимума
  if ((a < b) && (a < c))
    min = a;
  else if (b < c)
    min = b;
  else
    min = c;

  //Вывод результата
  if (!(min % 7) && min <= x)
    printf("%d\n", min);
  else
    printf("%f\n", min / (float)(a + b + c - min));

  return 0;
}
