//18501A0581
#include<stdio.h>
#include<string.h>

int frameMaxSize = 100;
int maxNumOfFrames = 100;

void printBin(int, int);

int main(){
    char frames[maxNumOfFrames][frameMaxSize];
    int frameLen[maxNumOfFrames];
    int n,i;

    printf("enter no.of frames:");
    scanf("%d", &n);

    //input
    for(i=0;i<n;i++){
        printf("enter frame %d:", i+1);
        scanf("%s", frames[i]);
        frameLen[i] = strlen(frames[i]);
        if(frameLen[i]&7){//checking if size of string is multiple of 8 or not
            printf("\n!!size of frame should be x8\n\n");
            i -= 1;
        }
    }

    //frames with character count output
    for(i=0;i<n;i++){
        printBin((frameLen[i]/8)+1, 8);
        printf("%s", frames[i]);
    }
    return 0;
}

void printBin(int num, int size){
    if(size==0)
        return;
    else{
        printBin(num/2, size-1);
        printf("%d", num&1);
    }
}