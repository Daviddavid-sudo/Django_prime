from django.shortcuts import render

def team_view(request):
    return render(request, 'team.html')

def map_view(request):
    return render(request, 'maps.html')