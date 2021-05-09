from django.shortcuts import render

# Create your views here.
def index(reequest):
    params = {
        'param':'homeのindexです'
    }
    return render(reequest, 'home/index.html', params)