from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string


def enviarme_email(nombre, email, mensaje):
    """
    Recibe nombre, email y mensaje, para pasarme los datos de quien desea contactarme.
    """

    
    try:
        # Validar email del usuario
        validate_email(email)
    except ValidationError:
        return "El correo proporcionado no es válido."

    # Configurar asunto y cuerpo del mensaje
    subject = "Nuevo mensaje desde el formulario de contacto"
    cuerpo_mensaje = f"""
    Has recibido un nuevo mensaje:
    
    Nombre: {nombre}
    Email: {email}
    Mensaje:
    {mensaje}
    """

    # Configurar destinatario (tu correo)
    destinatario = settings.EMAIL_HOST_USER  

    # Crear y enviar el mensaje
    enviar_mensaje = EmailMultiAlternatives(
        subject=subject,
        body=cuerpo_mensaje,
        from_email=destinatario,  # Remitente
        to=[destinatario],        # destinatario
    )

    enviar_mensaje.send()
    return "Se envió el correo exitosamente."


def enviar_correo(nombre, email):
    """Recibe nombre y email.
        El nombre que recibe es para pasar contexto a el mensaje 
        El correo que recibe es para el destino.
    """
    try:
        # Validar email del usuario
        validate_email(email)
    except ValidationError:
        return "El correo proporcionado no es válido."

    # Configurar asunto y cuerpo del mensaje
    subject = "Gracias por contactarme :D"

    #Cuerpo del mensaje en html.
    contenido = render_to_string("correo.html",{
            'nombre': nombre     
    })


    # Configurar destinatario (tu correo)
    destinatario = email  
    
    remitente = settings.EMAIL_HOST_USER

    # Crear y enviar el mensaje
    enviar_mensaje = EmailMultiAlternatives(
        subject=subject,
        body="Gracias por contactar conmigo :D",
        from_email=remitente,  
        to=[destinatario],        
    )

    enviar_mensaje.attach_alternative(contenido, "text/html")

    enviar_mensaje.send()
    return "Se envió el correo exitosamente."
