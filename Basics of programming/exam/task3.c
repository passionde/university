#include <stdio.h>
#include <stdlib.h>

// сумма первых членов последовательности 1 + 1/2^2 + 1/3^2 ...
int main(){
  int n;
  printf("Введите число: ");
  scanf("%d", &n);

  float sum = 0.0;
  for(int i = 1; i <= n; i++){
    sum += 1.0 / (i * i);
  }

  printf("Сумма первых %d членов последовательности = %f\n", n, sum);
  return 0;
}
