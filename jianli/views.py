from django.shortcuts import render
from django.shortcuts import HttpResponse
import json


# Create your views here.
# # for local 'rb', for aws 'r' Caution Please!!!
def index(request):    
    with open('jianli/data.json', 'r') as f:
        data = json.load(f)
    dic = {}
    for k, v in data.items():
        dic[k] = v
    
    return render(request, 'jianli/index.html', dic)


def index_en(request):
    with open('jianli/data_en.json', 'r') as f:
        data = json.load(f)
    dic = {}
    for k, v in data.items():
        dic[k] = v

    return render(request, 'jianli/index_en.html', dic)


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>This is Tao Orwell's Website, Welcome!!</h1>")


