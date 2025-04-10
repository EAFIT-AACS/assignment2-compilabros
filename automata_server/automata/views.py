from django.shortcuts import render
from .algorithms.ALGORITHM_1_LFCO_2025_HA_MV import run as run_algorithm1
from .algorithms.ALGORITHM_2_LFCO_2025_HA_MV import run as run_algorithm2
from .algorithms.ALGORITHM_3_LFCO_2025_HA_MV import run as run_algorithm3


def index(request):
    return render(request, 'index.html')

def algorithm1_view(request):
    result = run_algorithm1()
    return render(request, 'algorithm1.html', result)

def algorithm2_view(request):
    results = run_algorithm2()
    return render(request, 'algorithm2.html', {'results': results})

def algorithm3_view(request):
    trees = run_algorithm3()
    return render(request, 'algorithm3.html', {'trees': trees})