from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordict = {}

    for word in wordlist:

        if word in wordict:
            #Increase
            wordict[word] += 1
        else:
            #add to the dictionary
            wordict[word] = 1

    sortedwords = sorted(wordict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
