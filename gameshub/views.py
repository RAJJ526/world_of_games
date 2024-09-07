from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def snake_xenzia(request):
    return render(request, 'snake_xenzia.html')
def ludo(request):
    return render(request, 'ludo.html')
# Create your views here.
