#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int main()
{    
	int num,guess, nguesses=1; // imp formula 
	srand(time(0));
	num = rand()%100 + 1;
//	printf("the number is %d",num);
	
	do{
		printf("guess the number btw 1 to 100");
		scanf("%d",&guess);
		if(guess>num)
		{
			printf("enter a lower number pl! \n");
		}	else if(guess<num)
		{
			printf("enter a higher number pl!\n");	
		}
		else
		printf("u guessed in %d attempt\n",nguesses);
		nguesses++;
	}while(guess != num);
	return 0;
}
