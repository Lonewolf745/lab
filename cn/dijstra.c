#include<stdio.h>
#include<limits.h>
int adj_mat[10][10],n,distance;
struct node
{
    int predecessor;
    int length;
    enum {permanent,tentative} label;
};
int shortestPath(int src,int dest,int path[])
{
    int i,min,k;
    struct node ele[n];
    for(i=0;i<n;i++)
    {
        ele[i].predecessor=-1;
        ele[i].length=INT_MAX;
        ele[i].label=tentative;
    }
    k=src;
    ele[k].length=0;
    do
    {
        for(i=0;i<n;i++)
        {
            if(adj_mat[k][i]!=0&&ele[i].label==tentative)
            {
                if(adj_mat[k][i]+ele[k].length<ele[i].length)
                {
                    ele[i].length=ele[k].length+adj_mat[k][i];
                    ele[i].predecessor=k;
                }
            }
        }
        min=INT_MAX;
        for(i=0;i<n;i++)
        {
            if(ele[i].label==tentative&&ele[i].length<min)
            {
                k=i;
                min=ele[i].length;
            }
        }
        ele[k].label=permanent;
    }while(k!=dest);
    distance=ele[k].length;
    i=0;
    k=dest;
    do
    {
        path[i++]=k;
        k=ele[k].predecessor;
    }while(k>=src);
    return i;
}
int main()
{
    int i,j,src,dest,path[10];
    printf("Enter Number Of Nodes : ");
    scanf("%d",&n);
    printf("Enter Adjacency Matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&adj_mat[i][j]);
        }
    }
    printf("Enter Source : ");
    scanf("%d",&src);
    printf("Enter Destination : ");
    scanf("%d",&dest);
    int len=shortestPath(src,dest,path);
    for(i=len-1;i>=0;i--)
    {
        if(i==0)
        {
            printf("%d",path[i]);
        }
        else
        {
            printf("%d-->",path[i]);
        }
    }
    printf("\nDistance :  %d",distance);
    return 0;
}
