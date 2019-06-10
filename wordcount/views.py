from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() #.split() 자체가 리스트다.
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})

def credit(request):
    return render(request, 'credit.html')