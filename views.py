from django.shortcuts import render
from .models import SonnetModel
from django.db.models import Q

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def user_query_view(request):
    query = request.GET.get('q')
    object_list = SonnetModel.objects.filter(line__iregex=r"\y{0}\y".format(query))
    if len(object_list) == 0:
        return render(request, "no_results.html", {})
    else:
        results = {
            'lines': object_list,
            'term': query
        }
        return render(request, "results.html", results)

def poem_view(request, *args, **kwargs):
    return render(request, "poem.html", {})

def sonnet_query_view(request):
    query = request.GET.get('q')
    object_list_s = SonnetModel.objects.filter(Q(sonnet_nb__icontains=query))[:14]
    if len(object_list_s) == 0:
            return render(request, "poem.html", {})
    else:
        results_s = {
        'lines_s': object_list_s,
        'nb': query
        }
        return render(request, "read.html", results_s)

def info_view(request, *args, **kwargs):
    return render(request, "info.html", {})
