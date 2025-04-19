from django import template

register = template.Library()

@register.filter
def formatear_moneda(value):
    try:
        value = float(value)
        return "{:,.0f} $ COP".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value

@register.filter
def total_producto(value):
    try:
        precio = float(value["precio"])    
        cantidad = int(value["cantidad"])
        total = precio * cantidad
        return f"{total:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".") + " $ COP"

    except (ValueError, KeyError, TypeError):
        return "0,00 COP"
    
