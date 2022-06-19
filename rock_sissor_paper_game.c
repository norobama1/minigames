#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int game(char you,char comp){
    // for game draw
    if(you==comp)
    return 0;
    if(you=='s'&& comp=='p')
    return 1;
    else if(you=='s'&& comp=='r')
    return -1;
     if(you=='p'&& comp=='r')
    return -1;
    else if(you=='p'&& comp=='s')
    return 1;
     if(you=='r'&& comp=='s')
    return 1;
    else if(you=='r'&& comp=='p')
    return -1;
}

int main(){

    printf("r stands for rock \t p stands for paper \t s stands for scissor\n");
    char you,comp;
    int number;
    srand(time(0));
    number = rand()%100 +1;
      if(number<33)
      comp = 's';
      else if(33<number<66)
      comp = 'p';
      else
      comp = 'r';
      scanf("%c",&you);
      int result = game(you,comp);

    printf("you choose %c and computer choose %c\n",you,comp);
    if(result==0)
    printf("DRAW GAME");
    else if(result == 1)
    printf("YOU WIN");
    else
    printf("YOU LOSE");

return 0;
}
