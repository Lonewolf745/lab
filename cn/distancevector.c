#include<stdio.h>
struct node
{
int dis[20];
int from[20];
}rt[10];
int main()
{
int n;
printf("Enter Number Of Nodes : ");
scanf("%d",&n);
int costmat[n][n],i,j,k;
printf("Enter Adjacency Matrix : \n");
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
scanf("%d",&costmat[i][j]);//reading adjacency matrix
costmat[i][i]=0;
if(costmat[i][j]>100)
{
rt[i].from[j]=-1;
rt[i].dis[j]=costmat[i][j];
continue;
}
rt[i].from[j]=j;
rt[i].dis[j]=costmat[i][j];
}
}
int itr=1,count=0;
printf("iteration : %d",itr++);
for(i=0;i<n;i++)
{
printf("\n\n For router %c \n",i+97);
printf("\nDestination\tNext Hop\tDistance\n");
for(j=0;j<n;j++)
{
printf("%c\t\t%c\t\t%d\n",j+97,rt[i].from[j]+97,rt[i].dis[j]);
}
}
do
{
count=0;
printf("iteration : %d",itr++);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
for(k=0;k<n;k++)
{
if(rt[i].dis[j]>costmat[i][k]+rt[k].dis[j])//computing shortest path at each routers
{
rt[i].dis[j]=costmat[i][k]+rt[k].dis[j];
rt[i].from[j]=k;
count=1;
}
}
}
}
for(i=0;i<n;i++)
{
printf("\n\n For router %c \n",i+97);
printf("\nDestination\tNext Hop\tDistance\n");
for(j=0;j<n;j++)
{
printf("%c\t\t%c\t\t%d\n",j+97,rt[i].from[j]+97,rt[i].dis[j]);
}
}
}while(count!=0);
return 0;
}
