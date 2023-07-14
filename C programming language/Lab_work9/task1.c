#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include  <termios.h>
#include  <unistd.h>

int main()
{
  // Считывание строки с консоли
  char str[1000]="";
  char *rstr;
  rstr = gets (str);

  // Создание массива для записи новой строки
  int qnt = 0;
  for (int i = 0; str[i] != '\0'; i++)
  {
    if (str[i] == ' ')
      qnt++;
  }
  char str2[qnt];

  // Заполнение последними символами исходной строки
  char delim[] = ",.;:!?- ";
  char *p = strtok(str, delim);
  int len = strlen(p);
  str2[0] = p[len-1];
  int idx = 1;
  while (p = strtok(NULL, delim))
  {
    len = strlen(p);
    str2[idx++] = p[len-1];
  }
  str2[idx] = '\0';
  puts(str2);
  return 0;
}
