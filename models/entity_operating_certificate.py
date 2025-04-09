# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

ENTITY_TEMPLATE_CERTIFICATE = [
    ("co_a4_model_1", "CO A4-Model 1 - Various Companies"),
    ("co_a5_model_2", "CO A5-Model 2 - Transport - Rating"),
    ("co_a5_model_3", "CO A5-Model 3 - Various Companies"),
    ("co_a4_model_4", "CO A4-Model 4 - Location"),
    ("co_a4_model_5", "CO A4-Model 5 - Heritage Code")
]

class EntityOperatingCertificate(models.Model):
    _name = "entity.operating.certificate"
    _description = "Entity Operating Certificate"
    
    name = fields.Char(
        string="Operating Certificate Number", 
        required=True,
        copy=False, readonly=True,
        default='New')
    owner_id = fields.Many2one('res.partner', string="Owner", required=True)
    date_certificate = fields.Date(string="Date Certificate", required=True)
    template_certificate = fields.Selection(string='Template Certificate', selection=ENTITY_TEMPLATE_CERTIFICATE, copy=False, required=True)
    
    def action_print_report_operating_certificate(self):
        return True
        """ return self.env.ref('entity_hydrostatic_test_line.action_print_report_hydrostatic_test').report_action(self)  """

    def action_previewing_report_operating_certificate(self):
        return True
    
    @api.model
    def create(self, vals):
        if vals.get('name','New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('operating.certificate') or 'New'
        result = super(EntityOperatingCertificate, self).create(vals)
        return result
