from django.shortcuts import render

# Create your views here.
def ShowIndex(request):
    return render(request,"index.html")


def contact_us(request):
    return render(request,'contact_us.html')