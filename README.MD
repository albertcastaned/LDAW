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

## Iniciar API REST
Para iniciar la aplicacion API, utiliza el script:

```
(.env) $ ./start_api.sh
```

## Iniciar aplicacion web cliente
Para iniciar la aplicacion cliente en el ambiente virtual, utiliza el script:

```
(.env) $ ./start_client.sh
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

La aplicacion cliente consumira la API, asi que esta debe estar corriendo al mismo tiempo para que el cliente funcione.

## Base de Datos

Para generar nuevas migraciones si es que se agregan tablas o se cambia alguna tabla:
```
$ ./migrate.sh
```

Para iniciar o actualizar la base de datos con las migraciones:
```
$ ./makemigrations.sh
```

