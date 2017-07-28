
1.- CREAR UNA CUENTA DE GITHUB / Si ya tienes una, omitir este paso
2.- Haz un fork de este repositorio y realiza el siguiente desarrollo.


3.- De acuerdo al modelo entidad relacion incluido en la imagen llamada "Modelo_Entidad_Relacion.png" genera un modulo de odoo con los modelos necesarios, recuerda que el modelo llamado "res_users" ya existe como modelo base del sistema y deberas heredarlo.


4.- En el modelo heredado de "res_users" realiza una sobre escritura del metodo "create" para que al momento de que un usuario nuevo sea creado, le asigne un numero de empleado consecutivo a los anteriores segun el siguiente formato "000000"


5.- De acuerdo a los modelos creados y heredados, genera las vistas necesarias para generar un CRUD, teniendo en cuenta que deben existir 2 vistas basicas (Tree, Form), recuerda que la imagen del equipo debe poderse visualizar y cargar en la vista "Form"


6.- Genera los menus necesarios para acceder a las diferentes vistas creadas siguiendo la siguiente estructura:
    [Equipos de Computo] (root_menu)
        [Catálogos]
            [Sistemas Operativos]
            [Tipos de Equipo]
        [Equipos]


7.- Realizar herencia de la vista Form de usuarios ubicada en Configuracion/Usuarios y adiciona una pestaña llamada "Equipos Asignados" dentro de la cual agregarás un "Grid" con la lista de equipos asignados al usuario.


8.- Genera un permiso de acceso para que solo los usuarios a los que se les asigne este permiso puedan ver el los menus de acceso a las vistas creadas.

9.- Genera otro tipo de permiso en el que solo ciertos usuarios puedan crear nuevos equipos de computo y modificarlos.

10.- Genera un reporte PDF que liste los equipos asignados a cada usuario, el cual deberá ser accesible desde el menu "Acción" de la vista "Form" del usuario en cuestion. El menu deberá llamarse "Imprimir Lista de Equipos"


11.- En el modelo heredado "res_users" agrega un campo calculado llamado "numero_equipos_asignados" el cual devuelva el numero de equipos asignados al usuario en un valor entero. Este valos deberas mostrarlo en la vista heredada tipo "Form" de "res_users"


12.- Crea una carpeta llamada "data" y dentro de ella agrega un archivo XML mediante el cual se cargue la información por defecto de la aplicación. Esta información debe incluir:
    * 5 Usuarios
    * 10 Equipos de Computo asignados a los diferentes usuarios
    * 3 sistemas operativos asignados a los 10 equipos
    * 4 tipos de equipo (PC, LAPTOP, CELULAR, TABLET)


13.- Comprueba la funcionalidad del modulo, toma capturas de pantalla de cada una de las vistas, crea una carpeta llamada screenshots y agrega dichas capturas dentro de esta carpeta.


13.- Realiza commit del modulo y realiza un push al repositiorio de github, envia un pull request hacia este repositorio. Nosotros lo revisaremos lo mas pronto posible y calificaremos el desarrollo.



14.- Happy Coding!!!
