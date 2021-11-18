#include <stdio.h>

void fpos(double (*f) (double),double a, double b, int n ){
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0){
        printf("nao sei se dizer se f possui uma raiz no intervalo [%f][%f]",a,b);
        return;
    }
    else{
        for (int i=0;i<n;i++){
            double x = (a*fb-b*fa) / (fb-fa);
            printf("x_%d=%.16f\n",i+1,x);
            double fx = f(x);

            if (fx ==0){
                printf("A raiz procurada e: x= %.16f",x);
                return;
            }
            else{
                if(fa*fx <0){
                    b=x;
                    fb= fx;
                }
                else{
                    a=x;
                    fa=fx;
                }} 
        }
    }
}




double f(double x){
    return x*x -4*x +2 -log; //function
}

int main(void){

    double a = 1.0;
    double b = 2.0;
    int n =10;

    fpos(f,a,b,n);

    return 0;

}