from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'name':'loic'})
    
def about(request):
    return render(request, 'about.html', {'name':'loic'})
    
def count(request):
    fullText = request.GET['fulltext']
    wordList = fullText.split()
    
    wordDict = {}
    
    for word in wordList:
        word = word.lower()
        word = word.replace(',', '')
        word = word.replace('.', '')
        if word in wordDict:
            #increase
            wordDict[word] += 1
        else:
            #add
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fullText, 'count':len(wordList), 'sortedWords':sortedWords})