# -*- coding: utf-8 -*-
#############################################################################
#
#    Conectiva Perú S.A.
#
#    Copyright (C) 2024-TODAY Conectiva Perú(<https://www.conectiva.com.pe>)
#    Author: Conectiva Solutions(<https://www.conectiva.com.pe>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import api, fields, models

class Partner(models.Model):
    """Inherited res partner model"""
    _inherit = 'res.partner'

    active_entity = fields.Boolean(string="Active Entity",
                                         default=False)
    is_technical = fields.Boolean(string="Is Technical",
                                         default=False)
    owner_entity_ids = fields.One2many(
        'entity', 'owner_id',
        ondelete='restrict', string='Owner Entities')

    technician_entity_ids = fields.One2many(
        'entity.operating.line', 'technician_id',
        ondelete='restrict', string='Technician Entities')

    def _valid_field_parameter(self, field, name):
        if name == 'ondelete':
            return True
        return super(Partner,
                     self)._valid_field_parameter(field, name)

    def _compute_display_name(self):
        for contact in self:
            contact.display_name = f'{contact.name}/{contact.street}'
