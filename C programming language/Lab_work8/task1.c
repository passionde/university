#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int main(){
  unsigned char c1, c2;
  while (1) {
    c1 = getch();
    if(!c1 || c1 == 224){
      c2 = getch();
      if(c2 == 83){
        break;
      }
      printf("(%d %d) ", c1, c2);
    }
    else{
      if(c1 == 13){
        printf("\n");
      }
      else if(c1 == 8 || c1 == 27){
        printf("(%d) ", c1);
      }
      else{
        printf("%c ", c1);
      }
    }
  }
}
