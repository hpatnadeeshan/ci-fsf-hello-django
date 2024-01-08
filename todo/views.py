from django.shortcuts import render

# Create your views here.


def get_to_do_list(request):
    return render(request,'todo/to_do.html')
