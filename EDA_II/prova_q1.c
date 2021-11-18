#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    char s1[50], s2[50]; 
    int i, cont;
    cont=0;

    printf("Insira a primeira string: \n");
    scanf(" %s", s1);
    printf("Insira a segunda string: \n");
    scanf(" %s", s2);

    if(strlen(s1) > strlen(s2)){
        for(i = 0; i < strlen(s1); i++){
            if(i < strlen(s2)){
                if(s1[i] != s2[i])
                    cont++;
            }else{
                cont++;
            }
        }
        //printf("%i",cont);
    }
    else{
        for(int i = 0; i < strlen(s2); i++){
            if(i < strlen(s1)){
                if(s1[i] != s2[i])
                    cont++;
            }else{
                cont++;
            }
        }
    }

    printf("sao necessarias %i alteracoes\n", cont);

    return 0;
}