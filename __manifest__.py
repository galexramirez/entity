# -*- coding: utf-8 -*-
###################################################################################
#
#    Conectiva Perú S.A.
#
#    Copyright (C) 2024-TODAY Conectiva Perú(<https://www.conectiva.com.pe>)
#    Author: Conectiva Solutions(<https://www.conectiva.com.pe>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'Entity',
    'version': '17.0.1.1.1',
    'summary': 'Entity Management',
    'description': 'Entity Management Module For Odoo 17 Community',
    'category': 'Sales',
    'author': 'ALexander Ramirez Sandoval',
    'company': 'Conectiva Perú S.A.',
    'maintainer': 'Conectiva Perú S.A.',
    'website': "https://www.conectiva.com",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/ir_sequence_data.xml',
        'views/entity_customer_views.xml',
        'views/entity_technician_views.xml',
        'views/entity_views.xml',
        'views/entity_type_views.xml',
        'views/entity_model_views.xml',
        'views/entity_manufacturer_views.xml',
        'views/entity_category_views.xml',
        'views/entity_tag_views.xml',
        'views/entity_type_agent_views.xml',
        'views/entity_origin_views.xml',
        'views/entity_cylinder_capacity_views.xml',
        'views/entity_percentage_load_views.xml',
        'views/entity_technical_standard_views.xml',
        'views/entity_operating_certificate_views.xml',
        'views/entity_sanitation_certificate_views.xml',
        'views/entity_menus.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
