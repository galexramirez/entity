# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields

class EntityModel(models.Model):
    _name = 'entity.model'
    _description = 'Entity Model'
    _order = 'entity_manufacturer_id, name'

    name = fields.Char(string='Name', required=True)
    entity_manufacturer_id = fields.Many2one("entity.manufacturer", string="Manufacturer", options="{'no_create': True, 'no_create_edit':True}")
    note = fields.Html(string="Note")
    