from django.shortcuts import render, redirect
from .models import Project
from .forms import Info_contacto
from .enviarEmail import enviarme_email, enviar_correo

def home(request):
    "Renderiza los proyectos y pasa el formulario"
    projects = Project.objects.all()
    form = Info_contacto()
    return render(request, "home.html", {
        "projects": projects,
        "form" : form
        }          
                  )


def contacto(request):
    """
    Procesa los datos del formulario y envia los correos
    """
    if request.method == 'POST':
        form = Info_contacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            try:
                enviarme_email(nombre, email, mensaje)
                enviar_correo(nombre, email)
            except Exception as e:
                print(f"Error al enviar correo: {e}")
                return render(request, "error.html")

            return redirect('gracias')
        
        else:
            return render(request, "error.html")
    
    return redirect('home')

def gracias(request):
    return render(request, 'gracias.html')




