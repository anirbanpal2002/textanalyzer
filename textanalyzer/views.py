from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login


def home(request):
    return render(request, 'textanalyzer/index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    
    if removepunc == "on" and fullcaps == "on" and newlineremover == "on" and extraspaceremover == "on" and charcount == "on":
        return render(request, 'textanalyzer/error.html')
    
    elif not djtext:
        return render(request, 'textanalyzer/error.html')
    
    
    elif removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%w^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'pur':'Your Text:', 'te':djtext, 'purpose':'Removed Punctuations:', 'analyzed_text': analyzed}
        return render(request, 'textanalyzer/index.html', params)
    
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'pur':'Your Text:', 'te':djtext, 'purpose':'Changed to Uppercase:', 'analyzed_text': analyzed}
        return render(request, 'textanalyzer/index.html', params)
    
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'pur':'Your Text:', 'te':djtext,'purpose':'Removed New Lines:', 'analyzed_text': analyzed}
        return render(request, 'textanalyzer/index.html', params)
    
    elif extraspaceremover == "on": 
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'pur':'Your Text:', 'te':djtext,'purpose':'Removed Extra Spaces:', 'analyzed_text': analyzed}
        return render(request, 'textanalyzer/index.html', params)
    
    elif charcount == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'pur':'Your Text:', 'te':djtext,'purpose':'Character Count:', 'analyzed_text': analyzed}
        return render(request, 'textanalyzer/index.html', params)
    
    
    
    else:
        return render(request, 'textanalyzer/error.html')
    
# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount")