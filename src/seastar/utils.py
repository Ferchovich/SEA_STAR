
from django.http import HttpRequest
def getLoggedUser(request: HttpRequest):
    return request.session.get("user", "Iniciar Sesion")