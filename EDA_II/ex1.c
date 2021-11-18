#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *v, tam, k;

    printf("Qual o tamanho desejado do Vetor\n");
    scanf("%i",&tam);

    v= malloc(sizeof(int)*tam);
    printf("Insira os valores\n");

    for(int i=0;i<tam;i++){
        printf("posicao %i: ",i);
        scanf("%i",&v[i]);
    }

    printf("Qual o valor de k: \n");
    scanf("%i",&k);


    for(int i=0;i<tam;i++){
        for(int j=i;j<tam;j++){
            if(v[i]+v[j]==k){
                printf("True\n");
                return 0;
            }
        }
    }
    printf("False\n");


    return 0;
}
