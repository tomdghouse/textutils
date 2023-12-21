# This file is created by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Check checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    countchar = request.POST.get('countchar', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    print(removepunc)
    print(djtext)

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        #rem = "Your text after removing punctuations: "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed,}
        djtext = analyzed

        # Analyze the Text
        #return render(request, 'analyze.html', params)

    if countchar == "on":
        analyzed = len(djtext.replace(" ",""))
        #text = "Character Count is: "
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed,}
        djtext = analyzed

        # Analyze the Text
        #return render(request, 'analyze.html', params)

    if uppercase == "on":
        analyzed = djtext.upper()
        #text = "Your text after UpperCase: "
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed,}
        djtext = analyzed

        # Analyze the Text
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)

    if(removepunc != "on" and countchar != "on" and uppercase != "on"):
        return HttpResponse("Please Check the box")


