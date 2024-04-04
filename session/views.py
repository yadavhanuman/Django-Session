from django.shortcuts import render

def setsession(request):
    request.session['name']='hanuman'
    #request.session['course']='adit'
    return render(request,'setsession.html')

def getsession(request):
    a=request.session['name']
    return render(request,'getsession.html',{'x':a})

def deletesession(request):
    request.session.flush()
    #del request.session['name']
    return render(request,'deletesession.html')
        

