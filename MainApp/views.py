from django.shortcuts import render, HttpResponse
from django.http import Http404


author = {
    "name": "Alexander",
    "surname": "Saveliev",
    "email": "asaveliev_@inbox.ru"
}
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 3, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    return HttpResponse("Main page")


def about(request):
    text = f"""
    Имя: <b>{author["name"]}</b><br>
    Фамилия: <b>{author["surname"]}</b><br>
    email: <b>{author["email"]}</b>   
    """
    return HttpResponse(text)


def page_item(request, id):
    for item in items:
        if item['id'] == id:
            text = f"""
            Товар {item['name']}<br>
            Кол-во: {item['quantity']}
            """
            return HttpResponse(text)
    raise Http404(f"Товар с id={id} не найден")

def items_list(request):
    text = "<ol>"
    for item in items:
        text += f"<li>{item['name']}</li>"
    text += "</ol>"
    return HttpResponse(text)

