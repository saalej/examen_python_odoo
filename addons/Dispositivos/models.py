from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = "res.users"

    # Campos adicionales
    num_employee = fields.Char(string = "Num. de Empleado", readonly=True, size = 50)
    date_admission = fields.Date(string = "Fecha de Ingreso")
    num_imss = fields.Char(string = "Num. de IMSS", size = 50)
    #numero_equipos_asignados = fields.Integer(string="Num. de equipos asignados", compute="_compute_numero_equipos_asignados", store=True)
    
    # Campos heredados
    equipment_ids = fields.Many2many('equipos_computo', 'user_equipos_computo_rel', 'user_id', 'equipos_computo_id', string ="Equipos asignados")

    # Sequence
    @api.model
    def create_sequence(self, values):
        if not values.get('num_employee'):
            sequence = self.env['ir.sequence'].create({
                'name': 'Employee_Number_Sequence',
                'code': 'emp_number',
                'prefix': '',
                'padding': 6,
                'number_next_actual': 6,  
                'implementation': 'standard'
            })

            num_employee = sequence.next_by_code('emp_number') or '/'
            values['num_employee'] = num_employee

        return super(ResUsersInherit, self).create(values)
    
    @api.model
    def create(self, values):
        return self.create_sequence(values)

    # Grid
    def write(self, values):
        result = super(ResUsersInherit, self).write(values)
        self.update_user_assigned_equipment(self)
        return result

    def unlink_equipment(self):
        self.equipment_ids.write({'user': None})
        return super(ResUsersInherit, self).unlink()

    def update_user_assigned_equipment(self, user):
        if user.equipment_ids:
            user.equipment_ids.write({'user': user.id})
    
    # Report
    @api.model
    def get_assigned_equipment(self, user_id):
        user = self.env['res.users'].browse(user_id)
        equipment_records = user.equipment_ids
        return equipment_records
    
class Equipos_Computo(models.Model):
    _name = "equipos_computo"

    name = fields.Char(string = "nombre_equipo", size = 50)
    type_id = fields.Many2one("tipo_equipos", string = "tipo_equipo_id") # Enlazar con tipo_equipo
    os_id = fields.Many2one("sistemas_operativos", string = "tipo_equipo_id") # Enlazar con OS
    ram = fields.Char(string = "memoria_ram", size = 50)
    storage = fields.Char(string = "capacidad_disco_duro", size = 50)
    serial_number = fields.Char(string = "numero_de_serie", size = 50)
    user = fields.Many2one('res.users', string='Usuario asignado', ondelete='restrict')# Enlazar con res_users
    image = fields.Binary(string = "imagen", attachment = True)

class OS(models.Model):
    _name = "sistemas_operativos"

    name = fields.Char(string = "nombre_sistema", size = 50)
    version = fields.Char(string = "version", size = 50)

class Tipo_Equipos(models.Model):
    _name = "tipo_equipos"

    name = fields.Char(string = "tipo_equipo", size = 50)
    
    