# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityTypeAgent(models.Model):
    _name = "entity.type.agent"
    _description = "Entity Type Agent"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    entity_type_agent_ids = fields.One2many("entity", "entity_type_agent_id", string="Entity Type Agent")
    entity_type_agent_count = fields.Integer(compute="_compute_entity_type_agent_count", string="Entity Type Agent")
    hydrostatic_test_description = fields.Char(string="Hydrostatic Test Description", required=True)
    
    @api.depends('entity_type_agent_ids.entity_type_id')
    def _compute_entity_type_agent_count(self):
        for record in self:
            record.entity_type_agent_count = record.entity_type_agent_ids.search_count([('entity_type_agent_id','=',record.id)])
            
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]