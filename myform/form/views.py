from django.shortcuts import render
from .forms import AuthorForm,BookForm,ContactForm
from django.http import request,HttpResponse
from django.core.mail import send_mail

# Create your views here.
def manage_authors(request):

    if request.method=="POST":
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Data Inserted!.")
    else:
        form=AuthorForm()
    return render(request,"author.html",{"form":form})

def email(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            sender=form.cleaned_data['sender']
            cc_myself=form.cleaned_data['cc_myself']
            return render(request,'email_send.html',{"form":form,"result":form.cleaned_data})
        recipients=["rohit123code@gmail.com"]
        if cc_myself:
            recipients.append(sender)
        send_mail(subject, message, sender, recipients)
    else:
        form=ContactForm()
    return render(request,"email_send.html",{"form":form})
        



