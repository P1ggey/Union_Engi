from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect , HttpResponse

# Create your views here.

def send(request):
    name = request.POST['name']
    tel = request.POST['tel']
    message='Заказ от' + name + '/n Контактный телефон: ' + tel + 'Ожидает звонка'
    send_mail('Поступление нового заказа',message, 'antonn818@gmail.com',['antonn818@gmail.com'],fail_silently=False)

    return render(request,'send.html')
   
        