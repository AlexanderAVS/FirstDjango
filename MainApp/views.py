from django.shortcuts import render, HttpResponse

author = {
    "name": "Alexander",
    "surname": "Saveliev",
    "email": "asaveliev_@inbox.ru"
}
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