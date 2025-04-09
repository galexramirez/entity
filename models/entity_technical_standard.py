# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

ENTITY_TEMPLATE_CERTIFICATE = [
    ("co_a4_model_1", "CO A4-Model 1 - Various Companies"),
    ("co_a5_model_2", "CO A5-Model 2 - Transport - Rating"),
    ("co_a5_model_3", "CO A5-Model 3 - Various Companies"),
    ("co_a4_model_4", "CO A4-Model 4 - Location"),
    ("co_a4_model_5", "CO A4-Model 5 - Heritage Code"),
    ("ht_a4_model_1", "HT A4-Model 1 - Various Companies")
]

ENTITY_TYPE_CERTIFICATE = [
    ("operating", "OPERATING"),
    ("hydrostatic_test", "HYDROSTATIC TEST"),
]

class EntityTechnicalStandard(models.Model):
    _name = "entity.technical.standard"
    _description = "Entity Technical Standard"
    
    technical_standard = fields.Text(string="Technical Standard", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    type_certificate = fields.Selection(string='Certificate Type', selection=ENTITY_TYPE_CERTIFICATE, copy=False, required=True)
    template_certificate = fields.Selection(string='Certificate Template', selection=ENTITY_TEMPLATE_CERTIFICATE, copy=False, required=True)