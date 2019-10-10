from django.shortcuts import render
from functools import reduce

# Create your views here.

def index(request):
    return render(request, 'index.html')

def fibonacci(request):
    N=int(request.GET.get('N'))
    if N==0:
        result=0
    elif N==1:
        result=1
    else:
        fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-1), [0, 1])
        result=fib(N)[-1]
    print(N)
    return render(request, 'fib.html', {'result':result, 'N':N})
