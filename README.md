# Proyecto de Laboratorio Desarrollo Web

## Integrantes
* Alberto Castañeda Arana A01250647
* Adriana Paola Salinas García A01703675
* Max Burkle Goya A01702321

## Como Correr Pruebas Automaticamente En Cada Commit
En el directorio debera poner el comando:
```
$ venv-win\Scripts\activate
(venv-win) $ bash scripts/install-hooks.bash
```
para instalar el Hook. Solo debera hacer esto una primera vez.

Para saltar las pruebas en un commit utilicen:
```
git commit --no-verify -m "test"
```

## Como Ejecutar
Para poder ejecutar la aplicacion, debera utilizar el ambiente virtual dependiendo de su sistema operativo ejecutando el comando correspondiente.

### Windows
```
$ venv-win\Scripts\activate
(venv-win) $ _
```

Ya que tienes el ambiente virtual activado , para iniciar la aplicacion ejecuta: 
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
