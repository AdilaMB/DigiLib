from django.shortcuts import render

# Create your views here.
def index_list(request):
    return render(request, 'list/index_list.html', {''})