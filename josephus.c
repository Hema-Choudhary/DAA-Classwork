#include<stdio.h>
#include<math.h>
int main(void)
{
 int x,y;
 
 printf("\nEnter x:");
 scanf("%d",&x);
 y=(log(x)/log(2));
 printf("\ny: %d",y);
 x=((x^(1<<y))<<1)+1;
 printf("\n Survivor  %d",x);
 return 0;
}
