from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.http import HttpResponse
from polls.forms import KakikomiForm
def index(request):
    if request.method == 'POST':
        f = KakikomiForm(request.POST)
    else:
        f = KakikomiForm()
    return render(
        request,
        'polls/index.html',
        {'form1':f})
    #return HttpResponse(f.as_table())
    #return render(request, 'polls/index.html',{'form1':f})
    #return HttpResponse('polls/index.html')
    