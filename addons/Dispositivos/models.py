from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = "res.users"

    # Campos adicionales
    num_employee = fields.Char(string = "Num. de Empleado", readonly=True)
    date_admission = fields.Date(string = "Fecha de Ingreso")
    num_imss = fields.Char(string = "Num. de IMSS")

    @api.model
    def create(self, values):
        values['num_employee'] = self.env['ir.sequence'].next_by_code('EmpNum') or "/"
        return super(ResUsersInherit, self).create(values)