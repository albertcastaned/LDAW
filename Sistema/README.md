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
$ source .env/bin/activate
```

Debera salir su prompt como:
```
(.env) $ 
```

La primera vez que activa su ambiente virtual necesitara instalar todas las dependencias con el comando:
```
(.env) $ pip3 install -r requirements.txt
```


## Iniciar Servidor local
Para iniciar el servidor en el ambiente virtual, debera correr

```
export FLASK_APP=project.py
```

y luego
```
flask run
```

Debera salir algo parecido a:
```
$ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 572-008-498
```
