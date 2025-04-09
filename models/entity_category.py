# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityCategory(models.Model):
    _name = "entity.category"
    _description = "Entity Category"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]