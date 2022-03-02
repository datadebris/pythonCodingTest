#include <stdio.h>

void main(){
    int M, N;
    int ans = 0;

    scanf("%d", &N);
    scanf("%d", &M);

    for(int i = 0; i < N ; i++){
        if(i % M == 0){
            ans += i;
        }
    }

    printf("%d", ans);
}