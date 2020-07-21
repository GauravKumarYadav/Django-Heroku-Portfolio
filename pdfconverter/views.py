import os, shutil
from django.shortcuts import render
from django.http import HttpResponse , Http404
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import default_storage
from . import forms
from .functions import *
from . import settings

def index(request):
    form = forms.displayform()
    form1 = forms.contactform()
    delete_spec(settings.BASE_DIR+'/media')
    delete_spec(settings.BASE_DIR+'/media/processed') 
    return render(request,'body.html',{"form":form,"form1":form1})

def doclist(request):
    
    if request.method == 'POST':
        form = forms.displayform(request.POST,request.FILES)
        if form.is_valid():
            varq = request.POST.get('func','')
            file = request.FILES['file_field']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)

            folder_with_item_name = str(str(file).split('.')[0])
            if not (os.path.isdir(folder_with_item_name)):
                try:
                    os.mkdir(folder_with_item_name)
                except OSError as error:  
                    print(error)
            if varq == 'pdf2image':
                pdf2image(str(file),folder_with_item_name)
            if varq == 'pdf2text':
                pdf2text(str(file),folder_with_item_name)
            # if varq == 'pdf2docx':
            #     pdftodocx(str(file),folder_with_item_name)
            
            makezipfile(folder_with_item_name)
            shutil.move(str(str(file).split('.')[0]) + '.zip',settings.BASE_DIR + '/media/processed')
            shutil.rmtree(folder_with_item_name)
            
            posts = os.listdir(settings.BASE_DIR + '/media/processed')
            return render(request,'body.html',{'post' : posts,'path': '../../media/processed/' ,"form":form})

def sendcontactmail(request):
    sub = forms.contactform()
    form = forms.displayform()
    form1 = forms.contactform()
    if request.method == 'POST':
        sub = forms.contactform(request.POST)
        # send to person on website
        subject = 'Thank you For visiting my website'
        message = 'Glad you were here'
        recepient = str(sub['email'].value())
        send_mail(subject,message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
        
        #send to self
        subject = str(request.POST.get('subject')) +" - " +str(request.POST.get('name'))
        message = request.POST.get('message') + " from : " + str(sub['email'].value())
        recepient = settings.EMAIL_HOST_USER
        send_mail(subject,message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)

    return render(request,'body.html',{"form":form,"form1":form1})