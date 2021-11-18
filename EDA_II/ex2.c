#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *v, *res,tam;

    printf("Qual o tamanho desejado do Vetor\n");
    scanf("%i",&tam);

    v= malloc(sizeof(int)*tam);
    res= malloc(sizeof(int)*tam);

    printf("Insira os valores\n");

    for(int i=0;i<tam;i++){
        printf("posicao %i: ",i);
        scanf("%i",&v[i]);
    }

    for(int i=0;i<tam;i++){
        int acumulador =1;
        for(int j=0;j<tam;j++){
            if(!(j==i)){
                acumulador *= v[j];
            }
            res[i] = acumulador;
        }
    }

    for(int i=0;i<tam;i++){
        printf("%i ",res[i]);
    }








    return 0;
}