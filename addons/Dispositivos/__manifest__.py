{
    "name" : "Administracion de dispositivos",
    "description" : "Sistema para controlar la distribucion de los equipos",
    "author": "Marian Herrera",
    "depends": ['base'],
    "data" : [
        'data/default_users.xml',
        'data/default_tipos.xml',
        'data/default_os.xml',
        'data/default_devices.xml',

        'views/views_res.user.xml',
        'views/views_equipments.xml',
        'views/views_types_equipment.xml',
        'views/views_os.xml',
        'views/views_menu.xml',

        'reports/report.xml',
        'reports/list_template.xml',

        'security.xml'
    ],
}