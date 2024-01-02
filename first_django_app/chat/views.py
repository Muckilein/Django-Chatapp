from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Chat,Message
# from .form import CreateUserForm

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print("Received data "+ request.POST['textmessage']) 
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text = request.POST['textmessage'],chat = myChat, author = request.user, receiver = request.user) 
    chatMessages = Message.objects.filter(chat__id = 1)
    return render(request,'chat/index.html',{'username':'Julia','messages':chatMessages})

def loginView(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'),password = request.POST.get('password'))
        if user:
              login(request, user)
              return HttpResponseRedirect(request.POST.get('redirect')) #http://127.0.0.1:8000/login/?next=/chat/
        else:
             return render(request,'auth/login.html',{'wrongPassword':True,'redirect' : redirect})
    return render(request,'auth/login.html',{'redirect':redirect})

def register(request): 
    print('kick register') 
    form = UserCreationForm()  
    if request.method == 'POST':
        form = UserCreationForm(request.POST())
        if form.is_valid():
             form.save()
             return redirect("login/")
        else:
            return render(request,'auth/register.html',{'invalidData':True})

    context = { 'registerForm': form}     
    return render(request,'auth/register.html',context = context)
