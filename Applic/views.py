from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from Applic.models import *
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def Home(request):

    content1 = Client.objects.all()
    content2 =  Market.objects.all()
    content3 = Worker.objects.all()
    content = {
                'content1':content1,
                'content2':content2,
                'content3':content3,
                'query':''
               }
    
    return render(request, 'Applic/index.html', content)

@login_required
def Acerca(request):
    return render(request, 'Applic/acerca.html')
    
@login_required
def Contacto(request):
    return render(request, 'Applic/contacto.html')

@login_required
def Form(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        market_form = MarketForm(request.POST)
        worker_form = WorkerForm(request.POST)
        
        if client_form.is_valid():
            Client.objects.create(**client_form.cleaned_data)
            return redirect('home')
        elif market_form.is_valid():
            Market.objects.create(**market_form.cleaned_data)
            return redirect('home')
        elif worker_form.is_valid():
            Worker.objects.create(**worker_form.cleaned_data)
            return redirect('home')
    else:
        client_form = ClientForm()
        market_form = MarketForm()
        worker_form = WorkerForm()
    
    return render(request, 'Applic/form.html', {
        'form': client_form,
        'form2': market_form,
        'form3': worker_form
    })

@login_required
def Search (request):
    return render(request, 'Applic/search.html')

@login_required
def Find(request):
    query = request.GET.get('search_term', '')
    clients = Client.objects.filter(money__icontains=query) | Client.objects.filter(product__icontains=query)
    markets = Market.objects.filter(money__icontains=query) | Market.objects.filter(client__icontains=query)
    workers = Worker.objects.filter(pay__icontains=query) | Worker.objects.filter(hours__icontains=query)
    
    context = {
        'clients': clients,
        'markets': markets,
        'workers': workers,
        'query': query
    }

    return render(request, 'Applic/index.html', context)

@login_required
def Actualizacion(request, model_type, id_data):
    
    if model_type == 'client':
        data = Client.objects.get(id=id_data)
        FormClass = ClientForm
        template_name = 'Applic/client_form.html'
    elif model_type == 'market':
        data = Market.objects.get(id=id_data)
        FormClass = MarketForm
        template_name = 'Applic/market_form.html'
    elif model_type == 'worker':
        data = Worker.objects.get(id=id_data)
        FormClass = WorkerForm
        template_name = 'Applic/worker_form.html'
    else:
        return redirect('home')

    if request.method == 'POST':
        form = FormClass(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormClass(instance=data)

    return render(request, template_name, {'form': form})

@login_required
def Eliminacion(request, model_type, id_data):
    if model_type == 'client':
        data = get_object_or_404(Client, id=id_data)
    elif model_type == 'market':
        data = get_object_or_404(Market, id=id_data)
    elif model_type == 'worker':
        data = get_object_or_404(Worker, id=id_data)
    else:
        return redirect('home')

    data.delete()
    return redirect('home')


def Loguear(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        passworld = request.POST['password']
        user = authenticate(request, username=usuario, password=passworld)
        if user is not None:
            login(request, user)
            return render(request, 'Applic/index.html')
        else: 
            return redirect(reverse_lazy('login'))

    else: 
        miForm = AuthenticationForm()


    return render(request, 'Applic/login.html', {'form': miForm})

def Registracion(request):
    if request.method == 'POST':
        miForm = RegisterForm(request.POST)
        if miForm.is_valid():
            newuser = miForm.cleaned_data.get('username')
            miForm.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = RegisterForm()


    return render(request, 'Applic/register.html', {'form': miForm})

def Edit(request):
    user = request.user
    if request.method == 'POST':
        miForm = EditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=user)
            user.email = miForm.cleaned_data.get('email')
            user.first_name = miForm.cleaned_data.get('first_name')
            user.last_name = miForm.cleaned_data.get('last_name')
            user.save()
            return redirect(reverse_lazy('home'))
        else:
            miForm = EditForm(instance=user)
    return render (request, 'Applic/edituser.html', {'form':miForm})


class changePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Applic/changePass.html'
    correct_url = reverse_lazy('home')