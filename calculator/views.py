from django.conf import settings
from django.shortcuts import render


def food(request):
    nameDish = request.path[1 : -1]
    servings = request.GET.get("servings", 1)
    # print(settings.DATA[nameDish])
    dish = {}
    for a, b in settings.DATA[nameDish].items():
        c = b*float(servings)
        dish[a] = c    
    context = {
        'recipe': dish,
        }
    return render(request, 'calculator/index.html', context)
