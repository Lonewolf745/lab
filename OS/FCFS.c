 #include<stdio.h>
struct process
{
    char name[10];
    int bt,wt,ft,tat,at;
}p[10],t;
void main()
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
        printf("Enter the arrival time of the %s process:",p[i].name);
        scanf("%d",&p[i].at);
        printf("\n");
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(p[i].at>p[j].at)
            {
                t=p[i];
                p[i]=p[j];
                p[j]=t;
            }
        }
    }
    printf("Sorted order is:");
    for(i=0;i<n;i++)
    {
        printf("\t%s",p[i].name);
    }
    printf("\n");
    for(i=0;i<n;i++)
    {
        if(i==0)
        {
            p[i].ft=p[i].bt;
            p[i].wt=0;
            p[i].tat=p[i].bt+p[i].wt;
        }
        else
        {
            p[i].ft=p[i-1].ft+p[i].bt;
            p[i].wt=p[i-1].ft-p[i].at;
            p[i].tat=p[i].wt+p[i].bt;
        }
    }
    for(i=0;i<n;i++)
    {
        ttat=ttat+p[i].tat;
        twt=twt+p[i].wt;
    }
    atat=(float)ttat/n;
    awt=(float)twt/n;
    printf("----------------------------------------------------------");
    printf("\n| pro-name\tbt\tat\t ft\t wt\t tat\t|\n");
    printf("----------------------------------------------------------\n");
    for(i=0;i<n;i++)
    {
        printf("| %s\t\t%d\t %d\t %d\t %d\t %d\t|",p[i].name,p[i].bt,p[i].at,p[i].ft,p[i].wt,p[i].tat);
        printf("\n----------------------------------------------------------");
        printf("\n");
    }
    printf("\n\nTotal turn around time is %d",ttat);
    printf("\nTotal waiting time is %d",twt);
    printf("\nAverage turn around time is %.2f",atat);
    printf("\nAverage waiting time is %.2f",awt);
}

