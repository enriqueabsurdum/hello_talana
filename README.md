# Talana

Desarrollo de prueba técnica para proceso de selección en Talana.

## Despliegue

Clonar o descargar proyecto:

- Para **clonar** utilizar `git clone git@github.com:enriqueabsurdum/hello_talana.git`.
- En caso de preferir **descarga**, descomprimir archivo una vez finalizada.

Para el desligue local:

1. Dentro de la carpeta del proyecto se encuentra un archivo `docker-compose.local.yml`.
2. Ejecutar aprovisionamiento local con `docker-compose -f docker-compose.local.yml build` .
3. Desplegar ambiente local con `docker-compose -f docker-compose.local.yml up`.
4. Crear una cuenta de super usuario. Desde una terminal ejecutar `docker-compose -f docker-compose.local.yml run --rm web python manage.py createsuperuser`.

Abra un navegador web y acceda a la siguiente URL `http://localhost:8000/admin en donde podrá iniciar sesión en el administrador de Django con el fin de visualizar a los usuario que se registren en la aplicación.

## API Endpoints

El proyecto cuenta con los siguientes *endpoints*:

| Método | Endpoint                         | Descripción                                               |
| ------ | -------------------------------- | --------------------------------------------------------- |
| POST   | `{url}/users/register/`          | Registrar **usuario**.                                    |
| POST   | `{url}/users/generate_password/` | Generar contraseña de **usuario** (TODO).                 |
| POST   | `{url}/users/login/`             | Iniciar sesión de **usuario**.                            |
| POST   | `{url}/users/check/`             | Verificar dirección de correo electrónico de **usuario**. |
| GET    | `{url}/users/winner/`            | Generar **usuario** ganador del sorteo.                   |

En ambiente local, el proyecto se despliega en la siguiente URL: http://localhost:8000/.

El *endpoint* `{url}/users/generate_password/` no está finalizado (ver código fuente).

### Ejemplo de registro de usuario

```json
{
    "email": "joe.doe@email.com",
    "password": "secret",
    "first_name": "Joe",
    "last_name": "Doe"
}
```

### Ejemplo de generación de contraseña de usuario

```json
{
    "token": "secret",
    "password": "secret"
}
```

### Ejemplo de verificación de inicio de sesión

```json
{
    "email": "joe.doe@email.com",
    "password": "secret",
}
```

### Ejemplo de verificación de correo electrónico de usuario

```json
{
    "token": "secret"
}
```

