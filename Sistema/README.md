# Proyecto de Laboratorio Desarrollo Web

## Integrantes
* Alberto Castañeda Arana A01250647
* Adriana Paola Salinas García A01703675
* Max Burkle Goya A01702321

## Requisitos
  * Python Version > 3.6.9

## Configuracion Ambiente Virtual
Para poder ejecutar la aplicacion, debera crear primero un ambiente virtual con el siguiente comando:

```
$ python3 -m venv .env
```

Ya que tienes el ambiente virtual creado , deberas activarlo siempre para empezar a trabajar con el comando: 

```
$source .env/bin/activate
```

Debera salir su prompt como:
```
(.env) $ 
```

La primera vez que activa su ambiente virtual necesitara instalar todas las dependencias con el comando:
```
pip3 install -r requirements.txt
```


## Ejecutar Flask

Ya que tienes tu ambiente virtual activado con las dependencias instaladas, solo necesitar ejecutar lo siguiente para iniciar la aplicacion Flask:
```
$ (venv) flask run
(venv) $ _
```

Debera salir algo parecido a lo siguiente:
```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### (Opcional) Como Correr Pruebas Automaticamente En Cada Commit 
En el directorio debera poner el comando:
```
$ scripts/install-hooks.sh
```
para instalar el Hook. Solo debera hacer esto una primera vez.

Para saltar las pruebas en un commit utilicen:
```
git commit --no-verify -m "test"
```