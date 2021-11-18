#include <stdio.h>
#include <math.h>


double f(double x){
    //return (-34.14+((9.81*x)/17.78)*(1-(pow(M_E,-(17.78/x)*9.61))));
    return (2*71*pow(x,(5/2.0)))/(5.0)+(1/2.0)*42000*x*x - 92*9.81*x -92*9.81*0.55;
}

void secante(double x0, double x1, int n){
    double x2;
    for(int i=0; i<n; i++){
        double fx0 = f(x0);
        double fx1 = f(x1);
        if(fx1 == fx0){
            printf("Divisao por 0 na iteracao \n");
        }
        double x2 = (x0 * fx1 - x1 * fx0)/(fx1 - fx0);
        printf("x_%d = %.7f\n", i+2,x2);
        x0 = x1;
        x1 = x2;
    }
}

int main(void){

    double x0 = 1.02;
    double x1 = 2.12;
    int n = 8;

    secante(x0, x1, n);
    return 0;
}