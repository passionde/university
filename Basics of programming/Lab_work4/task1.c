#include <math.h>
#include <stdio.h>

// Функция для нахождения интеграла с n шагами
double f(int n)
{
  // Начальная точка 1.0 / n, далее увеличивается на шаг 2.0 / n, при этом это
  // середина прямоугольника
  double I = 0.0;
  for (double x = 1.0 / n; x <= 2.0; x += 2.0 / n)
  {
    double y;
    if (x <= 1.0)
      y = cos(x)*exp(-pow(x, 2));
    else
      y = log(x + 1) - sqrt(4 - pow(x, 2));
    I += y;
  }
  I = (2.0 / n) * I;
  return I;
}

int main()
{
  // Запрос точности
  double e;
  printf("Введите точность --> ");
  scanf("%lf", &e);

  // Запуск цикла до нужной точности
  int n = 1;
  double In = f(n);
  double I2n = f(2*n);

  while((fabs(I2n - In) / 3) >= e)
  {
    printf("%lf для n = %d\n", I2n, n*2);
    n = n * 2;
    In = I2n;
    I2n = f(2*n);
  }

  // Вывод результата
  printf("%lf\n", I2n);

  return 0;
}
