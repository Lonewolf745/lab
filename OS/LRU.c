#include<stdio.h>
struct page
{
    int name,time,frequency;
}p[100];
struct frame
{
    int name,time,frequency;
}f[100],temp;
void main()
{
    int count=0,clock=0,nf,j,n,h,i,z,s,l,k=0,pagefault=0;
    printf("enter the number of frames in physical memory:");
    scanf("%d",&nf);
    printf("enter the number of pages in memory reference string:");
    scanf("%d",&n);
    for(i=1;i<=nf;i++)
        f[i].name=-1;
    printf("enter the memory reference string:(0-9 only)\n");
    for(i=1;i<=n;i++)
    {
        printf("m%d:",i);
        scanf("%d",&p[i].name);
    }
    i=0;
    while(count<n)
    {
        i++;
        count++;
        k=0;
        if(i<=nf)
        {
            if(i==1)
            {
                clock=clock+1;
                f[i].name=p[count].name;
                f[i].time=clock;
                f[i].frequency=1;
                pagefault=pagefault+1;
            }
     		else
            {
                for(j=1;j<=nf;j++)
                {
                    if(f[j].name==p[count].name)
                    {
                        z=j;
                        j=i;
                        k=1;
                    }
                }
                if(k==0)
                {
                    clock=clock+1;
                    f[i].name=p[count].name;
                    f[i].time=clock;
                    f[i].frequency=1;
                    pagefault=pagefault+1;
                }
                if(k==1)
                {
                    clock=clock+1;
                    f[z].time=clock;
                    i=i-1;
                }
            }
        }
        else
        {
            for(s=2;s<=nf;s++)
            {
                for(l=1;l<s;l++)
                {
                    if(f[l].time>f[s].time)
                    {
                        temp=f[l];
                        f[l]=f[s];
                        f[s]=temp;
                    }
                }
            }
            for(j=1;j<=nf;j++)
            {
                if(f[j].name==p[count].name)
                {
                     z=j;
                     j=i;
                     k=1;
                }
            }
	if(k==0)
            {
                	clock=clock+1;
		f[1].name=p[count].name;
		f[1].time=clock;
		f[1].frequency=1;
		pagefault=pagefault+1;
            }
	if(k==1)
            {
                clock=clock+1;
                f[z].time=clock;
                i=i-1;
                i=i-1;
            }
        }
        printf("\nPages in frames are:: ");
        if(k==1)
            printf("page fault is not occured");
        else
        {
            for(h=1;h<=nf;h++)
            {
                printf("%d  ",f[h].name);
            }
        }
    };
    printf("\n\nAt end of memory stream the pages in frames are::");
    for(i=1;i<=nf;i++)
        printf("page%d\t",f[i].name);
    printf("\n\nThe total pagefaults for given memory reference string are::%d",pagefault);
    return 0;
}

