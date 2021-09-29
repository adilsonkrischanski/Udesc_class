#include <stdio.h>

int main(void){
   
    double x0 = 1.0;
    int n = 5;
    newton(x0,n);

    return 0;
}

void newton(double x0, int n){
    double x1;
    for(int i = 0; i< n; i++){
        x1 = x0 - f(x0)/df(x0);
        printf("x_%d - %.16f",i+1, x1);
        x0=x1;
    }
}

double df(double x){
    return 2*x;
}

double f(double x){
    return x*x - 2;
}