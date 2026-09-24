from django.http import HttpResponse
from django.shortcuts import render

def message(request):
    return HttpResponse("welcome user")


def handler404(request, exception):
    return HttpResponse("<h1 style='color: red;'>Page not found</h1>", status=404)



#template
def test_template(request):
    return render(request, 'test.html')