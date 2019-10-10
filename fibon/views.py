import time
from django.shortcuts import render
from functools import reduce
from datetime import datetime, timedelta



# do your work here



def index(request):
    return render(request, 'index.html')

def fibonacci(request):
    start_time = datetime.now()
    N=int(request.GET.get('N'))
    if N==0:
        result=0
    elif N==1:
        result=1
    else:
        fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-1), [0, 1])
        result=fib(N)[-1]
    end_time = datetime.now()
    total=end_time-start_time
    context={'result':result, 'N':N, 'total':total*1000}
    return render(request, 'fib.html', context)

