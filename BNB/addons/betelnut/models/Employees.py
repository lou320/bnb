from odoo import fields, models, api


class Employees(models.Model):
    _name = 'betelnut.employees'
    _description = 'This Module is to manage a Betelnut Business'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(required=True,Tracking=True)
    age = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    phone = fields.Char(string="Phone No.")
    address = fields.Text()

