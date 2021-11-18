#include <stdio.h>
#include <math.h>

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
            printf("x_%d=%.7f\n",i+1,x);
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
    //return (-35.6+((9.81*x)/22.39)*(1-(pow(M_E,-(22.39/x)*9.36)))); //function;
       return (2*71*pow(x,(5/2.0)))/(5.0)+(1/2.0)*42000*x*x - 92*9.81*x -92*9.81*0.55;
}

int main(void){

    double a =  0.0;
    double b = 1.18;
    int n =11;

    fpos(f,a,b,n);

    return 0;
}