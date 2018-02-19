from django.core.exceptions import ValidationError

num = ('1','2','3','4','5','6','7','8','9','0')


def Validate_studio(value):
    for n in num:
        if n in value:
            raise ValidationError("No ingresar numeros")
        else:
            return value
