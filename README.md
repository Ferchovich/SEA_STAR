# Sistema de Peaje - Programación III

[Introduccion](#introduccion)

[Instalacion](#instalacion)

[Diagrama Entidad-Relacion](#diagrama-entidad-relacion-del-sistema)

[Diagrama Clases](#diagrama-de-clases-del-sistema)



## Introduccion
Nuestro proyecto se basa en la gestión de cruceros para la compañía naviera SEA STAR. Este sistema ha sido diseñado para satisfacer las necesidades operativas y de registro de una empresa especializada en la realización de cruceros de lujo.


## Instalacion

### Requisitos Previos

Python 3.10 requerido:

*input:*
```bash
    python --version
```

*output:*
```bash
    Python <numeroVersion>
```
<hr>

Django requerido:

*input:*
```bash
    pip install Django
```
<hr>
Pipenv requerido:


*input:*
```bash
    pip install pipenv
```

<hr>

#### Primer paso: Creacion Entorno Virtual

Va a ser muy importante trabajar con entornos virtuales ya que nos ayudará a evitar problemas relacionados con dependencias de bibliotecas y paquetes.

```bash
    pipenv install //Creacion
    pipenv shell //Ejecucion
```

#### Segundo paso: Instalacion de los modulos requeridos para su ejecucion

Una vez que estamos dentro del entorno virtual, debemos instalar todos los paquetes que se necesitaran para desarrollar/ejecutar el proyecto

```bash
    pipenv install -r requirements.txt
```

>Una vez hayas seguido estos pasos, podrás ejecutar y/o trabajar en el proyecto sin ningún problema.

## Diagrama Entidad-Relacion Del Sistema
![Imagen Diagrama Entidad-Relacion](src\seastar\static\img\erDiagram.jpg)


## Diagrama De Clases Del Sistema
![Imagen Diagrama de Clases](src\seastar\static\img\classDiagram.jpg)