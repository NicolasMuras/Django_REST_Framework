<h1> Django REST: Nature </h1>

![alt text](https://github.com/NicolasMuras/Django_REST_Nature/blob/main/images/elements.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementacion del proyecto</a></li>
  <li><a href="#modelos">Modelos</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduccion al proyecto</h2>

Bueno, la idea es generar un backend modulable y escalable con Django REST Framework, elegí la temática de la naturaleza por que encaja perfectamente con el concepto, mi idea es crear un escenario completamente modular, donde los elementos no dependan uno de los otros, a la vez iré probando conceptos nuevos con cada modulo añadido, la idea es también que este programa sirva como 'Cookbook', una guía donde cualquier persona pueda ver el concepto de cada metodología en una forma simple.

<h2><a id="user-content-implementación-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>Python</strong>: El lenguaje utilizado para la elaboracion del codigo.</li>
<li><strong>Django</strong>: Framework open-source utilizado para la elaboración del proyecto.</li>
<li><strong>Django REST</strong>: Es una aplicación de django que nos permitira contruir el proyecto bajo la arquitectura REST.</li>
<li><strong>django-simple-history</strong>: Guarda el estado del modelo Django en cada create/update/delete.</li>
<li><strong>Insomnia</strong>: Utilizo insomnia para ir testeando la aplicación mediante requests a medida que avanzo.</li>
<li><strong>virtualenv</strong>: Recomiendo utilizar entornos virtuales, nos hace la vida mas facil :D.</li>
</ul>

Se empieza definiendo una estructura solida para el proyecto, la idea es organizarse bien desde el comienzo al encarar un proyecto que pretende ser escalable, creamos una carpeta apps, en ella estará cada elemento de nuestro escenario, empecé por algo simple "Shroom", las partes fundamentales son: modules.py, serializers.py, api.py y urls.py.
Comienzo definiendo el modelo, luego paso a serializer.py donde empiezo construyendo un serializador simple que permitirá ejecutar el primer testeo, seguido: api.py, configuro las request y al final defino la ruta correspondiente para hacer la request en el archivo urls.py. Luego: Refactoring.

<h3>Aspectos que considero importantes:</h3>
<ul>
<li><strong>Definir serializadores para cada función CRUD. Nos permitira tener un software mas escalable.</strong></li>
<li><strong>La estructura del proyecto tiene que ser consistente desde el comienzo, ayudara a la comprension del programa.</strong></li>
<li><strong>Separar la logica de la parte de las request, es preferible que los serializers se encarguen de eso.</strong></li>
</ul>

<h3>Estructura del proyecto:</h3>

<pre>
PROYECT
│   manage.py
│
├───apps
│   │   __init__.py
│   │
│   └───shrooms
│       │   admin.py
│       │   apps.py
│       │   models.py
│       │   __init__.py
│       │
│       ├───api
│       │       api.py
│       │       serializers.py
│       │       urls.py
│       │
│       └───migrations
│               0001_initial.py
│               0002_shroom_secret.py
│               __init__.py
│
└───PROYECT
    │   asgi.py
    │   db.sqlite3
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───settings
            base.py
            local.py
            production.py
            __init__.py
</pre>

<h2><a id="user-content-modelos" class="anchor" aria-hidden="true" href="#modelos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Modelos</h2>

<table>
  <tbody><tr>
   <td><strong>Dato</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>specie</strong>
   </td>
   <td>CharField(max_length = 50)
   </td>
  </tr>
  <tr>
   <td><strong>days</strong>
   </td>
   <td>SmallIntegerField()
   </td>
  </tr>
  <tr>
   <td><strong>cap_color</strong>
   </td>
   <td>CharField(max_length=20, blank = False)
   </td>
  </tr>
  <tr>
   <td><strong>trunk_color</strong>
   </td>
   <td>CharField(max_length=20, blank = False)
   </td>
  </tr>
  <tr>
   <td><strong>secret</strong>
   </td>
   <td>CharField(max_length=10, unique = True, blank = False, null = False)
   </td>
  </tr>
</tbody></table>
