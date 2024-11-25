import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    """
    Esta función se encarga de procesar el markdown en el blog.
    """
    return md.markdown(
        value,
        extensions=['markdown.extensions.fenced_code',
                    'markdown.extensions.extra',
                    'markdown.extensions.admonition'
                    ], #La lista contiene las extenciones que interpretan enlaces y codigo en el markdown.
        output_format='html5'
    ).replace('<code>', '<code class="language-python">')  # Ajusta para el lenguaje deseado

# pd.. volver a entender este codigo, pedir explicación a la ia.

