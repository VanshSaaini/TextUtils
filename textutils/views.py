# i have created this file - Vansh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    # get the text
    djtext = request.POST.get('text','default')

    # check checkbox values
    removepunc = request.POST.get('removepunc','default')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover','off')
    charCount = request.POST.get('charCount','off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose' : 'Remove Punctuations',
            'analyzed_text' : analyzed
        }
        djtext = analyzed
        #return render(request,'analyze.html', parmas)
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'purpose' : 'Change to Uppercase',
            'analyzed_text' : analyzed
        }
        djtext = analyzed
        # analyze the text
        #return render(request,'analyze.html', parmas)
    
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose' : 'Remove New Lines',
            'analyzed_text' : analyzed
        }
        djtext = analyzed
       #return render(request,'analyze.html',params)

    if(extraSpaceRemover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {
            'purpose' : 'Extra Space Remover',
            'analyzed_text' : analyzed
        }
        djtext = analyzed
       #return render(request,'analyze.html',params)
    
    if(charCount=="on"):
        count = 0
        for index, char in enumerate(djtext):
            count = index + 1

        params = {
            'purpose' : 'Character Count',
            'analyzed_text' : count
        }
        
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraSpaceRemover != "on" and charCount !="on"):
        error = '''<div class="alert alert-danger" role="alert">
                    Error!! Please select at least one operation.
                    </div>'''
        return render(request,'index.html',{'error':error})

    
    return render(request,'analyze.html',params)
