# OnlyFlans 🍮

OnlyFlans es una plataforma web de una PYME dedicada a la venta de flanes artesanales. Este sitio fue creado utilizando Django y Bootstrap para una experiencia de usuario optimizada y moderna.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

OnlyFlans permite a los usuarios explorar una variedad de sabores de flan, conocer nuestros especiales del mes, y enviar consultas a través de un formulario de contacto. En la sección de administración de Django, el equipo puede gestionar el inventario, testimonios de clientes, y visualizar los mensajes de contacto.

## Características

- **Listado de flanes**: Descripción y precios con un formato en CLP.
- **Especiales del mes**: Carousel de los flanes destacados en la página principal.
- **Formulario de contacto**: Formulario funcional que guarda mensajes en la base de datos.
- **Panel de administración**: Gestión de productos y testimonios de clientes.

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/onlyflans.git
    cd onlyflans
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

5. Crea y configura la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Carga los datos iniciales:

    ```bash
    python manage.py loaddata initial_data.json
    ```

7. Crea un superusuario para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser
    ```

8. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

Luego, abre tu navegador y ve a `http://127.0.0.1:8000` para ver el sitio en funcionamiento.

## Uso

1. Accede a la página principal para ver los **especiales del mes** en el carousel.
2. Explora los flanes en la sección de listado.
3. Envía un mensaje en la página de contacto.
4. Si eres un administrador, accede a `/admin` para gestionar el contenido del sitio.

## Ejemplos

### Página Principal
Carousel de los flanes especiales del mes y sección de introducción para explorar todos los flanes.

### Listado de Flanes
Vista en cards con nombre, descripción, precio en CLP y botón "Ver más".

### Formulario de Contacto
Formulario accesible en la página de contacto, guardando los mensajes en la base de datos.

## Contribución

¡Contribuciones son bienvenidas! Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y realiza un commit (`git commit -am 'Agrega nueva característica'`).
4. Sube tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Despedida

Gracias por explorar este proyecto. Mi objetivo es crear soluciones que inspiren, conecten y faciliten experiencias.

¡Sigue construyendo, aprendiendo y creando! 🚀

Valery Maragaño :sparkles: 
