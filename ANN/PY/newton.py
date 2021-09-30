def f(x):
    return x*x-2 # function

def df(x):
    return 2*x # derivada de f

def newton(x0,n):
    for i in range(0,n):
        x1 = x0-(f(x0)/df(x0))
        print(f'x_{i+1} = {x1:.16f}')
        x0=x1

def main():
    x0=1.0
    n=5
    newton(x0,n)

main()

