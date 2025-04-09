# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityCylinderCapacity(models.Model):
    _name = "entity.cylinder.capacity"
    _description = "Entity Cylinder Capacity"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    entity_cylinder_capacity_ids = fields.One2many("entity", "entity_cylinder_capacity_id", string="Cylinder Capacity")
    entity_cylinder_capacity_count = fields.Integer(compute="_compute_entity_cylinder_capacity_count", string="Cylinder Capacity Count")
    
    @api.depends('entity_cylinder_capacity_ids.entity_cylinder_capacity_id')
    def _compute_entity_cylinder_capacity_count(self):
        for record in self:
            record.entity_cylinder_capacity_count = record.entity_cylinder_capacity_ids.search_count([('entity_cylinder_capacity_id','=',record.id)])
            
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]