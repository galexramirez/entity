# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityPercentageLoad(models.Model):
    _name = "entity.percentage.load"
    _description = "Entity Percentage Load"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    entity_percentage_load_ids = fields.One2many("entity", "entity_percentage_load_id", string="Percentage Load")
    entity_percentage_load_count = fields.Integer(compute="_compute_entity_percentage_load_count", string="Percentage Load Count")
    
    @api.depends('entity_percentage_load_ids.entity_percentage_load_id')
    def _compute_entity_percentage_load_count(self):
        for record in self:
            record.entity_percentage_load_count = record.entity_percentage_load_ids.search_count([('entity_percentage_load_id','=',record.id)])
            
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]