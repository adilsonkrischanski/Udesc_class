def f(x):
    return x*x*x-2 #funcao

def bisection(f,a,b,n):
    if f(a)*f(b)>=0:
        print(f'o metodo de bolzano nao sabe dizer se existe')
        return
    else:
        for i in range(0,n):
            m = 0.5*(a+b)
            print(f'x_{i+1} = {m:.16f}')
            if f(m)==0:
                print(f'voce achou uma raiz exata para f:z = {m:.16f}')
            if(f(a)*f(m)<0):
                b=m
            else:
                a=m

def main():
    a=0.0
    b=2.0
    n=12
    bisection(f,a,b,n)

main()
