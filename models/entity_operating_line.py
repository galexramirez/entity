# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class EntityOperatingLine(models.Model):
    _name = "entity.operating.line"
    _description = "Entity Operating Line"
    _order = 'date_loading desc'

    name = fields.Char(string='Name', readonly=True, default='New')
    id_loading = fields.Integer(string="ID.")
    entity_id = fields.Many2one('entity', string='Entity', required=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True)
    location = fields.Char(string='Location')
    date_loading = fields.Date(string='Date Loading', required=True, default=fields.Date.today)
    date_reloading = fields.Date(string='Date Reloading', required=True, default=datetime.today() + relativedelta(years=1))
    cylinder_number = fields.Char(string='Cylinder Number')
    technician_id = fields.Many2one("res.partner", string="Technician", required=True)
    extinction_rating = fields.Char(string='Extinction Rating')

    _sql_constraints = [
        ('operating_unique', 'unique(owner_id,date_loading)', 'A owner and date loading must be unique!')
    ]
    
    @api.onchange("date_loading")
    def _onchange_date_loading(self):
        for record in self:
            if record.date_loading:
                record.date_reloading = record.date_loading + relativedelta(years=1)
            else:
                record.date_reloading = False