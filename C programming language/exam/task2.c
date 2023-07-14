// день недели через swith

#include <stdio.h>
#include <stdlib.h>

int main(){
  int n;
  printf("Введите число: ");
  scanf("%d", &n);

  switch (n) {
    case 1:
      printf("Понедельник\n");
      break;
    case 2:
      printf("Вторник\n");
      break;
    case 3:
      printf("Среда\n");
      break;
    case 4:
      printf("Четверг\n");
      break;
    case 5:
      printf("Пятница\n");
      break;
    case 6:
      printf("Суббота\n");
      break;
    case 7:
      printf("Воскресенье\n");
      break;
    default:
      printf("Неизвестный день недели\n");
  }

  return 0;
}
