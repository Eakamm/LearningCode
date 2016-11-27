#include<stdio.h>
int main(){
  unsigned long long l,k,n,j,t,m,x,y;
  scanf ("%lld",&n);
  t=0;
  k=1;
  x=0;
  y=0;
  for (;n>0;){
    t=t+n%10;
    n=n/10;
  }
  printf("%lld",t);
  l=t;
  for(;t>=10;){
  	t=t/10;
  	k=k*10;
  	y++;
  }
  while (k>0){
  	m=l/k;
    switch (m){
      case 0:printf("ling");break;
      case 1:printf("yi");break;
      case 2:printf("er");break;
      case 3:printf("san");break;
      case 4:printf("si");break;
      case 5:printf("wu");break;
      case 6:printf("liu");break;
      case 7:printf("qi");break;
      case 8:printf("ba");break;
      case 9:printf("jiu");break;
      }
    if (y==x){
    	printf("");
    }else{
      printf(" ");
     }
     x++;
     l=l-m*k;
     k=k/10;
  }*/
return 0;
}
