# I have created this file - Mihir!

from django .http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #check which box is on
    if removepunc == "on":
#       analyzed = djtext

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params ={'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to UpeerCase', 'analyzed_text': analyzed}
            # analyze the text
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
            # analyze the text
        djtext = analyzed


    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed



    if charcounter == "on":
        analyzed = ""
        count = 0
        for char in djtext:
            count = count+1
            #print(count)
            analyzed = count
        params = {'purpose': 'CharCounter', 'analyzed_text': analyzed}


    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcounter != "on":
        return HttpResponse("Please select the operations")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html', {})

def contact (request):
    return render(request, 'contact.html', {})