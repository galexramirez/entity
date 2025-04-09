# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityOrigin(models.Model):
    _name = "entity.origin"
    _description = "Entity Origin"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    entity_origin_ids = fields.One2many("entity", "entity_origin_id", string="Entity Origin")
    entity_origin_count = fields.Integer(compute="_compute_entity_origin_count", string="Entity Origin Count")
    
    @api.depends('entity_origin_ids.entity_origin_id')
    def _compute_entity_origin_count(self):
        for record in self:
            record.entity_origin_count = record.entity_origin_ids.search_count([('entity_origin_id','=',record.id)])
            
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]