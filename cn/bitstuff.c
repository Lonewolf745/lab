//18501A0581
#include<stdio.h>
#include<string.h>

int maxNumOfFrames = 100;
int frameMaxSize = 100;

int main(){
    int n;
    char frames[maxNumOfFrames][frameMaxSize];

    printf("enter no.of frames:");
    scanf("%d", &n);

    //input
    for(int i=0; i<n; i++){
        printf("enter frame %d:", i+1);
        scanf("%s", frames[i]);
    }

    //output
    printf("01111110");
    for(int i=0; i<n; i++){
        int ones_count=0;
        int frameSize = strlen(frames[i]);

        for(int j=0; j<frameSize; j++){
            char bit = frames[i][j];
            printf("%c", bit);

            if(bit=='1')
                ones_count += 1;
            else
                ones_count = 0;

            if(ones_count==5){
                printf("0");
                ones_count = 0;
            }
        }
    printf("01111110");
    }
}