from django.shortcuts import render

# Create your vie;ws here.
def homepage(request):
    return render(request, "template/index.html")