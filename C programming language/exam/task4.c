#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
  int n;
  printf("Введите n: ");
  scanf("%d", &n);

  double b = 1.0;
  double a1 = 1.0;
  double a2 = 1.0;
  for(int i = 2; i <= n; i++){
    a2 = (sqrt(b) + sqrt(a1) / 2.0) / 2.0;
    b = 2 * a1 * a1 + b;
    a1 = a2;
  }

  printf("b(%d) = %f; a(%d) = %f \n", n, b, n, a1);
  return 0;
}
