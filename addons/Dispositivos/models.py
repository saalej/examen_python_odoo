from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = "res.users"

    # Campos adicionales
    num_employee = fields.Char(string = "Num. de Empleado", readonly=True, size = 50)
    date_admission = fields.Date(string = "Fecha de Ingreso")
    num_imss = fields.Char(string = "Num. de IMSS", size = 50)

    @api.model
    def create(self, values):
        values['num_employee'] = self.env['ir.sequence'].next_by_code('EmpNum') or "/"
        return super(ResUsersInherit, self).create(values)


class Equipos_Computo(models.Model):
    _name = "equipos_computo"

    name = fields.Char(string = "nombre_equipo", size = 50)
    type_id = fields.Many2one("tipo_equipos", string = "tipo_equipo_id") # Enlazar con tipo_equipo
    os_id = fields.Many2one("sistemas_operativos", string = "tipo_equipo_id") # Enlazar con OS
    ram = fields.Char(string = "memoria_ram", size = 50)
    storage = fields.Char(string = "capacidad_disco_duro", size = 50)
    serial_number = fields.Char(string = "numero_de_serie", size = 50)
    user = fields.Many2one("res.users", string = "usuario_asignado_id")# Enlazar con res_users
    image = fields.Binary(string = "imagen", attachment = True)
    
class OS(models.Model):
    _name = "sistemas_operativos"

    name = fields.Char(string = "nombre_sistema", size = 50)
    version = fields.Char(string = "version", size = 50)

class Tipo_Equipos(models.Model):
    _name = "tipo_equipos"

    name = fields.Char(string = "tipo_equipo", size = 50)
    