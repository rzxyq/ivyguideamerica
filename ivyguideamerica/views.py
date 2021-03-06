from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    context = {    
        'request' : request,   
    }
    return render(request, 'index.html', context)

def languages(request):
    context = {    
        'request' : request,   
    }
    return render(request, 'languages.html', context)

def about(request):
    return render(request, 'about.html', {
        'request' : request, })


def faq(request):
    return render(request, 'faq.html', {
        'request' : request, })


def contact(request):
    return render(request, 'contact.html', {
        'request' : request, })


