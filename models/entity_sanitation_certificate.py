# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models

class EntitySanitationCertificate(models.Model):
    _name = "entity.sanitation.certificate"
    _description = "Entity Sanitation Certificate"
    
    name = fields.Char(
        string="Sanitation Certificate Number", 
        required=True,
        copy=False, readonly=True,
        default='New')
    disinfection = fields.Boolean(string="Disinfection",
                                         default=False, required=True)
    rat_extermination = fields.Boolean(string="Rat Extermination",
                                         default=False, required=True)
    septic_tank_cleaning = fields.Boolean(string="Septic Tank Cleaning",
                                         default=False, required=True)
    insect_control = fields.Boolean(string="Insect Control",
                                         default=False, required=True)
    water_reservoir_cleaning_desinfection = fields.Boolean(string="Water Reservoir Cleaning and Desinfection",
                                         default=False, required=True)
    owner_id = fields.Many2one('res.partner', string="Owner", required=True)
    service_start_date = fields.Date(string="Service Start Date", required=True)
    expiration_date = fields.Date(string="Expiration Date", required=True)
    business_activity = fields.Char(string="Business Activity", required=True)
    treated_area = fields.Char(string="Treated Area", required=True)

    def action_button_print_sanitation_certificate(self):
        self.ensure_one()
        return self.env.ref('entity.action_print_sanitation_certificate_pdf').report_action(self)

    def action_previewing_report_sanitation_certificate(self):
        return True
    
    @api.model
    def create(self, vals):
        if vals.get('name','New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sanitation.certificate') or 'New'
        result = super(EntitySanitationCertificate, self).create(vals)
        return result
