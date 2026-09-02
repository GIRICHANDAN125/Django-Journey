from django.http import HttpResponse

def message(request):
    return HttpResponse("welcome user")


def handler404(request, exception):
    return HttpResponse("<h1 style='color: red;'>Page not found</h1>", status=404)