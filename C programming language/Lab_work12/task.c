#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#pragma warning(disable : 4996)

int count = 0;

typedef struct{
  char surname[255];
  char first_name[255];
  char midle_name[255];
  struct tm date_birth;
  char address[255];
  char phone_number[255];
} frend;

// Игнорирование символов
void flush_input(void) {
    char c;
    while (scanf("%c", &c) == 1 && c != '\n')
        ;
}

// Функция добавления записи
void add_note(frend frends[], int count){
  //int date;
  char data_input[255] = "";

  printf("Enter surname --> ");
  fgets(data_input, 100, stdin);
  data_input[strlen(data_input) - 1] = 0;
  sprintf(frends[count].surname, "%s", data_input);

  printf("Enter first name --> ");
  fgets(data_input, 100, stdin);
  data_input[strlen(data_input) - 1] = 0;
  sprintf(frends[count].first_name, "%s", data_input);

  printf("Enter midle name --> ");
  fgets(data_input, 100, stdin);
  data_input[strlen(data_input) - 1] = 0;
  sprintf(frends[count].midle_name, "%s", data_input);

  printf("Enter date birth (dd.mm.yyyy) --> ");
  int month, year;
  scanf("%d.%d.%d", &frends[count].date_birth.tm_mday, &month, &year);
  month--;
  year -= 1900;
  frends[count].date_birth.tm_mon = month;
  frends[count].date_birth.tm_year = year;
  flush_input();

  printf("Enter address --> ");
  fgets(data_input, 100, stdin);
  data_input[strlen(data_input) - 1] = 0;
  sprintf(frends[count].address, "%s", data_input);

  printf("Enter phone number --> ");
  fgets(data_input, 100, stdin);
  data_input[strlen(data_input) - 1] = 0;
  sprintf(frends[count].phone_number, "%s", data_input);
}

// Функция печати всех записей
void print_notes(frend frends[], int count){
  if(!count){
    printf("Список пуст\n");
  }
  else{
    for(int i = 0; i < count; i++){
      char date_b[15];
      strftime(date_b, 15, "%d.%m.%Y", &frends[i].date_birth);
      printf("%d. Фамилия: %s; Имя: %s; Отчество: %s; Дата рождения: %s; Адресс: %s; Номер телефона: %s\n", i + 1, frends[i].surname, frends[i].first_name, frends[i].midle_name, date_b, frends[i].address, frends[i].phone_number);
    }
  }
}

// Удаление записи по номеру
void del_note(frend frends[], int count, int del) {
  printf("%s %s %s удален (запись №%d)\n", frends[del].surname, frends[del].first_name, frends[del].midle_name, del + 1);
  for (int i = del; i < count - 1; i++) {
    frends[i] = frends[i + 1];
  }
}

// Вывод записей по месяцу рождения
void print_month_notes(frend frends[], int count, int month){
  if(!count){
    printf("Список пуст\n");
  }
  else if(month > 12){
    printf("Некорректно введен месяц (допустимые значения от 1 до 12)\n");
  }
  else{
    for(int i = 0; i < count; i++){
      if(frends[i].date_birth.tm_mon + 1 == month){
        char date_b[15];
        strftime(date_b, 15, "%d.%m.%Y", &frends[i].date_birth);
        printf("%d. Фамилия: %s; Имя: %s; Отчество: %s; Дата рождения: %s; Адресс: %s; Номер телефона: %s\n", i + 1, frends[i].surname, frends[i].first_name, frends[i].midle_name, date_b, frends[i].address, frends[i].phone_number);
      }
    }
  }
}

// Получение записей с файла
void file_input(FILE *f, frend frends[]) {
  char str[255];
  char *istr;

  while (fgets(str, 256, f) != NULL) {
    istr = strtok(str, "|");
    sprintf(frends[count].surname, "%s", istr);

    istr = strtok(NULL, "|");
    sprintf(frends[count].first_name, "%s", istr);

    istr = strtok(NULL, "|");
    sprintf(frends[count].midle_name, "%s", istr);

    istr = strtok(NULL, "|");
    frends[count].date_birth.tm_mday = atoi(istr);

    istr = strtok(NULL, "|");
    frends[count].date_birth.tm_mon = atoi(istr);

    istr = strtok(NULL, "|");
    frends[count].date_birth.tm_year = atoi(istr);

    istr = strtok(NULL, "|");
    sprintf(frends[count].address, "%s", istr);

    istr = strtok(NULL, "|");
    istr[strlen(istr) - 1] = 0;
    sprintf(frends[count].phone_number, "%s", istr);

    count++;
  }
}

// Запись данных в файл
void file_output(FILE *f, frend frends[], int count) {
  for (int i = 0; i < count; i++)
    fprintf(f, "%s|%s|%s|%d|%d|%d|%s|%s\n", frends[i].surname, frends[i].first_name, frends[i].midle_name, frends[i].date_birth.tm_mday, frends[i].date_birth.tm_mon, frends[i].date_birth.tm_year, frends[i].address, frends[i].phone_number);
}

int main(){
  int query, ret;
  frend frends[100];

  // Получение предыдущих данных
  FILE *file = fopen("database.txt", "r");
  file_input(file, frends);
  fclose(file);

  // Вывод кнопок управления
  system("chcp 65001");

  printf("Меню управления:\n");
  printf("    1 --> Добавить новую запись\n");
  printf("    2 --> Удалить запись\n");
  printf("    3 --> Просмотреть все записи\n");
  printf("    4 --> Выборка записей по месяцу рождения\n");
  printf("    5 --> Завершить программу\n");

  while (1) {
    // Получение запроса
    printf("Query --> ");
    ret = scanf("%d", &query);
    flush_input();

    // Диспетчер запросов
    if(ret != 1){
      printf("Введите число\n");
    }
    else if(query == 1){
      add_note(frends, count);
      count++;
    }
    else if(query == 2){
      int del;
      printf("Введите номер записи для удаления --> ");
      scanf("%d", &del);

      if(del > count){
        printf("Номер записи не найден\n");
      }
      else{
      del_note(frends, count, --del);
      count--;
      }
    }
    else if(query == 3){
      print_notes(frends, count);
    }
    else if(query == 4){
      int month;
      printf("Введите месяц для поиска (от 1 до 12)\n");
      scanf("%d", &month);
      print_month_notes(frends, count, month);
    }
    else if(query == 5){
      break;
    }
    else{
      printf("Неизвестный запрос\n");
    }
  }
  file = fopen("database.txt", "w");
  file_output(file, frends, count);
  fclose(file);
}
