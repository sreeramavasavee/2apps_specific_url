from django.shortcuts import render

# Create your views here.
def app2_first(request):
    return render(request,'app2_first.html')

def app2_second(request):
    return render(request,'app2_second.html')