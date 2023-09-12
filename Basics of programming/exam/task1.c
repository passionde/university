//Скалярное произведение векторов
#include <stdio.h>
#include <stdlib.h>

int skl_mul(int vektr1[], int vektr2[], int n){
  int mul_vectr = 0;
  for(int i = 0; i < n; i++){
    mul_vectr += vektr1[i] * vektr2[i];
  }
  return mul_vectr;
}

int main(){
  int n;
  printf("Введите количество координат вектора: ");
  scanf("%d", &n);

  int vektr1[n];
  int vektr2[n];
  int vektr_i;

  for(int i = 0; i < n; i++){
    printf("Введите %d координату--> ", i+1);
    scanf("%d", &vektr_i);
    vektr1[i] = vektr_i;
  }

  for(int i = 0; i < n; i++){
    printf("Введите %d координату--> ", i+1);
    scanf("%d", &vektr_i);
    vektr2[i] = vektr_i;
  }

  printf("Скалярное произведение = %d\n", skl_mul(vektr1, vektr2, n));

  return 0;
}
