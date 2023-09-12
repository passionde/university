#include <stdio.h>
#include <math.h>
int main()
{
  // Считывание и проверка значений X и a
  float a, x;
  printf("Введите число a ∈ (-∞; 0) ⋃ (0; +∞) --> ");
  scanf("%f", &a);

  if(a == 0.0)
  {
    printf("Неправильное значение параметра a\n");
    return 0;
  }
  else if(a < 0.0)
  {
    printf("Введите число x ∈ {Z} -> ");
    scanf("%f", &x);
    if (((int)x != x) && isnormal(x))
    {
      printf("Неправильное значение аргумента x\n");
      return 0;
    }
  }
  else
  {
    printf("Введите число x ∈ {R}--> ");
    scanf("%f", &x);
  }

  // Вывод значения функции y(x)
  double y = (pow(a,x)+pow(a,-x))/2.0;
  printf("y(x) = %lf\n", y);

  // Проверка и вывод функции z(y)
  if (y < -1.0 || y > 2)
  {
    printf("Функция z(y), при y = %lf неопределена\n", y);
  }
  else
  {
    double z = sqrt(2.0 + y - pow(y, 2));
    printf("z(y) = %lf\n", z);
  }
  return 0;
}
