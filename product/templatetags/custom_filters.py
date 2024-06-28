# wird nicht mehr genutzt, kann aber genutzt werden, um Klassen zu Formularelementen hinzuzufügen
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})