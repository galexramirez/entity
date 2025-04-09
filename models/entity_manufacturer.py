# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class EntityManufacturer(models.Model):
    _name = "entity.manufacturer"
    _description = "Entity Manufacturer"
    _order = "sequence, name"
    
    name = fields.Char(string="Name")
    image_entity_manufacturer= fields.Binary(string="Image")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    entity_model_ids = fields.One2many("entity.model", "entity_manufacturer_id", string="Model")
    entity_model_count = fields.Integer(compute="_compute_entity_model_count", string="Model")
    
    @api.depends('entity_model_ids.entity_manufacturer_id')
    def _compute_entity_model_count(self):
        for record in self:
            record.entity_model_count = record.entity_model_ids.search_count([('entity_manufacturer_id','=',record.id)]) 
            
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A entity type name must be unique!')
    ]