from django.shortcuts import render, HttpResponse
from django.http import Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def home(request):
    return render(request, 'index.html')




def page_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={id} не найден")
    context = {
        "item": item
    }
    return render(request, "item_page.html", context)



def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)

