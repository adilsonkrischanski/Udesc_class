#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define S 8


int main(void){
    int v[]= {6,5,2,2,5,2,2,1};
    int i,j,k,cont, cont2,pares;

    for(i=0;i<S;i++){
        cont =0;
        cont2 =0 ;
        for(j=i;j<S;j++){
            if (v[i]==v[j]){
                cont++;
            }

        for(k=0;k<i;k++){
            if(v[k]==v[i]){
                cont2++;

            }
        }
        }

        if (cont2 ==0)
        {
            pares = cont/2;
            if (pares !=0){
                printf("tamanho %i, %i pares \n",v[i],pares);
            }
            
        }
       
    }

    return 0;
}
