from django.shortcuts import render

def index(request):
    ''' Página principal del proyecto '''
    
    title = "Index"
    if request.user.is_authenticated():
        title = "Bienvenido {}".format(request.user)
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)
