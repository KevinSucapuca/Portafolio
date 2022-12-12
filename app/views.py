from django.shortcuts import render,redirect,get_object_or_404
from .models import Portafolio
from .forms import ContactoForm, PortafolioForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.


def home(request):
    portafolio = Portafolio.objects.all()
    data = {
        'portafolio' : portafolio
        
    }
    return render(request,'app/home.html',data)


def contacto(request):
    
    data = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"
        else:
            data["mensaje"] = formulario
    return render(request,'app/contacto.html',data)

@login_required
def galeria(request):
    return render(request,'app/galeria.html')

@login_required
def agregar_portafolio(request):
    data = {
        'form': PortafolioForm()
    }
    if request.method == 'POST':
        formulario =PortafolioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado correctamente")
            return redirect(to="listar_portafolio")
        else:
            data['form'] = formulario
    return render(request, 'app/agregar.html',data)


def listar_portafolio(request):
    portafolio = Portafolio.objects.all()
    data = {
        'portafolio':portafolio
    }
    return render(request, 'app/listar.html',data)

@login_required
def modificar_portafolio(request, id):
    
    portafolio = get_object_or_404(Portafolio, id=id)
    
    data = {
        'form': PortafolioForm(instance=portafolio)
    }
    
    if request.method == 'POST':
        formulario = PortafolioForm(data = request.POST, instance = portafolio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_portafolio")
        data["form"] =formulario
    
    return render(request, 'app/modificar.html',data)

@login_required
def eliminar_portafolio (request,id):
    portafolio = get_object_or_404(Portafolio, id=id)
    portafolio.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_portafolio")



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='home')
        data["form"] = formulario
    
    return render(request, 'registration/registro.html',data)