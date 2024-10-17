from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.GET, request.method)
    print(request.GET.keys())
    params = request.GET
    a = int(params.get('a'))
    b = int(params.get('b'))
    c = a + b
    # return HttpResponse(f"{a} + {b} = {c}")
    return render(request, 'index.html', {'a': a, 'b': b, 'c': c})
