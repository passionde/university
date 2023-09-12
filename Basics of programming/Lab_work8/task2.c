#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <conio.h>

int main()
{
  system("chcp 65001");
  printf("Введите строку: \n");
  int count_alpha = 0;
  unsigned char c;
  while(1){
    // Обработка PageUP
    c = getch();
    if(c == 0){
      c = getch();
      if(c == 73){
        break;
      }
    }
    // Обработка F10-F12
    else if(c == 224){
      c = getch();
      continue;
    }
    // Подсчет букв и вывод символов
    else{
      if(isalpha(c))
        count_alpha++;
      if(c != 13)
        printf("%c", c);
    }
  }
  printf("\nВведено букв: %d\n", count_alpha);
  return 0;
}
