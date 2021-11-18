#include <stdio.h>
#include <math.h>

void bisection(double(*f)(double),double a,double b,int n){
    if (f(a)*f(b)>=0) {
        printf("o medoto de bolzano nao sabe dizer se existe uma raiz no intervalo {%.12f,%.12f}",a,b);
        return;
    }
    else{
        for(int k=0;k<n;k++){
            double m = 0.5*(a+b);
            printf("x_%d = %.7f\n", k+1,m);
            if(f(m)==0){
                printf("voce encontrou uma raiz pra f: z= %.7f",m);
            }
            if(f(a)*f(m)<0){
                b=m;
            }
            else{
                a=m;
            }
    }
    }

}

double f(double x){
    //return x*x*x-2; // funcao
    return (2*71*pow(x,(5/2.0)))/(5.0)+(1/2.0)*42000*x*x - 92*9.81*x -92*9.81*0.55;
}

int main(void){
    double a = 0.0; // incio do intervalo de analize
    double b = 1.59; // fim do intervalo de analize
    int n = 12; // quantidade de interacoes
    
    bisection(f,a,b,n);

    return 0;
}