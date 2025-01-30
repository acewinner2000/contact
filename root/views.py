from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

def contact(request):
    if request.method=='GET':
        return render(request,'root/contact.html')
    elif request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message sent')
            return redirect(request.path_info)
        else:
            messages.add_message(request,messages.ERROR,'your message did not send')
            return redirect(request.path_info)



    