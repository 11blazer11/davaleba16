from django.shortcuts import render
from django.db.models import Q, F
from .models import Product


def view(request):
    #Q
    ragaca_Q1 = Product.objects.filter(Q(price__gt=50) | Q(quantity__lt=10))
    ragaca_Q2 = Product.objects.filter(Q(name__icontains="phone") & Q(price__gte=100) & Q(price__lte=500))
    ragaca_Q3 = Product.objects.filter(~Q(price__lt=200))

    #F
    Product.objects.update(price=F("price") + 10)
    ragaca_F1 = Product.objects.filter(price__gt=F("quantity"))
    Product.objects.update(quantity=F("quantity") + 1)

    context = {
        "qsQ1": ragaca_Q1,
        "qsQ2": ragaca_Q2,
        "qsQ3": ragaca_Q3,

        "qsF1":ragaca_F1,

        
    }

    return render(request, "lookup_queries.html", context)
