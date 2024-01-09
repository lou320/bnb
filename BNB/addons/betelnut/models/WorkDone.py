from odoo import fields, models, api


class WorkDone(models.Model):
    _name = 'betelnut.workdone'
    _description = 'Description'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'worker'
    worker = fields.Many2one('betelnut.employees')
    a_thone_thay_vass = fields.Integer(default=0)
    a_thone_gyi_vass = fields.Integer(default=0)
    a_shay_sate_vass = fields.Integer(default=0)
    a_ni_pwa_vass = fields.Integer(default=0)
    workcomplete = fields.Integer()
    wage = fields.Integer(default=0)
    is_created = fields.Boolean(string='Is Created', default=False)

    @api.model
    def create(self, values):
        values['wage'] = (values['a_thone_thay_vass']*350) + (values['a_thone_gyi_vass']*400) + (values['a_shay_sate_vass']*300) + (values['a_ni_pwa_vass']*450)
        values['workcomplete'] = values['a_thone_thay_vass']+ values['a_thone_gyi_vass']+values['a_shay_sate_vass']+values['a_ni_pwa_vass']
        values['is_created'] = True
        return super(WorkDone, self).create(values)