# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityTag(models.Model):
    _name = "entity.tag"
    _description = "Entity Tag"
    _order = "name"
    
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A property tag name must be unique!')
    ]