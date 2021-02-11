#include<stdio.h>
struct process
{
    char name[10];
    int bt,ft,tat,wt,tft;
}p[10];
int main()
{
    int i,j=0,k=0,n,d,timeslice,ttat=0,tbt=0,twt=0;
    float avgwt,avgtat;
    printf("enter number of processes:");
    scanf("%d",&n);
    printf("enter time slice:");
    scanf("%d",&timeslice);
    for(i=0;i<n;i++)
    {
        printf("enter name of process %d :",i+1);
        scanf("%s",p[i].name);
        printf("enter burst time of process %d :",i+1);
        scanf("%d",&p[i].bt);
    }
    for(i=0;i<n;i++)
    {
        tbt=tbt+p[i].bt; 
        p[i].tft=0;
        p[i].wt=0;
    }
    while(j<tbt)
    {
        for(i=0;i<n;i++)
        {
            if(p[i].bt>0)
            {
                if(p[i].bt<=timeslice)
                {
                    if(k==0&&i==0)
                        p[i].wt=0;
                    else
                    {
                        d=j-p[i].tft;
                        p[i].wt+=d;
                    }
                    j+=p[i].bt;
                    p[i].ft=j;
                    p[i].bt=0;
                }
                else
                {
                    if(k==0&&i==0)
                        p[i].wt=0;
                    else
                    {
                        d=j-p[i].tft;
                        p[i].wt+=d;
                    }
                    j+=timeslice; p[i].bt-=timeslice; p[i].tft=j;
                }
            }
        }
        k++;
    }
    for(i=0;i<n;i++)
    {
        printf("\n\n");
        printf("waiting time of process %s :%d\n",p[i].name,p[i].wt);
        printf("turn around time of process %s :%d\n",p[i].name,p[i].ft);
        printf("finish time of process %s :%d\n",p[i].name,p[i].ft);
    }
    printf("Processes  Waiting Time  Turn Around Time  Finish Time\n");
    printf("---------------------------------------------------------\n");
    for(i=0;i<n;i++)
    {
        printf("   %s \t\t%d\t\t  %d\t\t %d",p[i].name,p[i].wt,p[i].ft,p[i].ft);
        printf("\n");
    }
    for(i=0;i<n;i++)
    {
        ttat+=p[i].ft;
        twt+=p[i].wt;
    }
    avgwt=(float)twt/n; avgtat=(float)ttat/n;
    printf("Total turn around time:%d\n",ttat);
    printf("Total waiting time:%d\n",twt);
    printf("Avg turn around time:%f\n",avgtat);
    printf("Avg waiting time:%f\n",avgwt);
    return 0;
}

