from django.shortcuts import render
import json


# Create your views here.
# # for local 'rb', for aws 'r' Caution Please!!!
def index(request):    
    with open('jianli/data.json', 'rb') as f:
        data = json.load(f)
    dic = {}
    for k, v in data.items():
        dic[k] = v
    
    return render(request, 'jianli/index.html', dic)


def index_en(request):
    with open('jianli/data_en.json', 'rb') as f:
        data = json.load(f)
    dic = {}
    for k, v in data.items():
        dic[k] = v

    return render(request, 'jianli/index_en.html', dic)
