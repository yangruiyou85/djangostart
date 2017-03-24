# -*- coding:utf-8 -*-

from django.shortcuts import render

from apps.message.models import UserMessage


# Create your views here.


def getform(request):
    # all_messages  = UserMessage.objects.filter(name='yangruiyou')

    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #    print message.name
    # user_message=UserMessage()
    # user_message.name='sz'
    # user_message.address='gd'
    # user_message.email='sz@163.com'
    # user_message.save()
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('address', '')
        address = request.POST.get('request', '')
        email = request.POST.get('email','')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.save()

    return render(request, 'message_form.html')
