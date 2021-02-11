#include<stdio.h>
struct process
{
    char name[10];
    int bt,wt,ft,tat;
}p[10],temp;

int main()
{
    int i,j,n,ttat=0,twt=0;
    float atat,awt;
    printf("Enter the number of processes:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("\nEnter the name of the process:");
        scanf("%s",p[i].name);
        printf("Enter the burst time of the %s process:",p[i].name);
        scanf("%d",&p[i].bt);
        printf("\n");
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(p[i].bt>p[j].bt)
            {
                temp=p[i];
                p[i]=p[j];
                p[j]=temp;
            }
        }
    }
    printf("Sorted order is:");
    for(i=0;i<n;i++)
        printf("    %s",p[i].name);

    for(i=0;i<n;i++)
    {
        if(i==0)
        {
            p[i].wt=0;
            p[i].ft=p[i].bt;
        }
		else
        {
            p[i].wt=p[i-1].bt+p[i-1].wt;
            p[i].ft=p[i].wt+p[i].bt;
        }
    }
    for(i=0;i<n;i++)
    {
        p[i].tat=p[i].ft;
        ttat=ttat+p[i].ft;
        twt=twt+p[i].wt;
    }
   atat=(float)ttat/n;
   awt=(float)twt/n;
   printf("\n\n");

   printf("p.name\t bt\t wt\t ft\t tat\n");
   printf("----------------------------------------------");
   printf("\n");

   for(i=0;i<n;i++)
  {
   printf("  %s\t%d\t %d\t %d\t %d\t",p[i].name,p[i].bt,p[i].wt,p[i].ft,p[i].tat);
   printf("\n");
  }
   printf("\n\n\n");
   printf("The total turn around time is %d\n",ttat);
   printf("\nThe total waiting time is %d\n",twt);
   printf("\nThe average turn around time is %f\n",atat);
   printf("\nThe average waiting time is %f\n",awt);
 }

