# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

ENTITY_PH_RESULT = [
    ("aprobado", "APROBADO"),
    ("no_aprobado", "NO APROBADO")
]

ENTITY_TEST_PRESSURE = [
    ("alta_presion", "ALTA PRESION"),
    ("baja_presion", "BAJA PRESION")
]

ENTITY_PH_PRESSURE = [
    ("35_kg_cm2", "38 Kg/cm2"),
    ("55_kg_cm2", "55 Kg/cm2")
]

ENTITY_OWNER_TYPE = [
    ("principal", "PRINCIPAL"),
    ("tercero", "TERCERO")
]

class EntityHydrostaticTestLine(models.Model):
    _name = "entity.hydrostatic.test.line"
    _description = "Entity Hydrostatic Test Line"
    _order = 'date_hydrostatic_test desc'

    name = fields.Char(
        string="Certificate Hydrostatic Test Number",
        required=True, copy=False, readonly=True,
        default='New')
    id_hydrostatic_test = fields.Integer(string="ID.")
    entity_id = fields.Many2one('entity', string='Entity', required=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True)
    owner_type = fields.Selection(string='Owner Type', selection=ENTITY_OWNER_TYPE, copy=False, required=True)
    date_hydrostatic_test = fields.Date(string='Date Hydrostatic Test', required=True, default=fields.Date.today)
    date_next_hydrostatic_test = fields.Date(string='Date Next Hydrostatic Test', default=datetime.today() + relativedelta(years=5))
    hydrostatic_test_result = fields.Selection(string='Hydrostatic Test Result', selection=ENTITY_PH_RESULT, copy=False, default='aprobado')
    test_pressure = fields.Selection(string='Test Pressure', selection=ENTITY_TEST_PRESSURE, copy=False, default='alta_presion')
    hydrostatic_test_pressure = fields.Selection(string='Hydrostatic Test Pressure', selection=ENTITY_PH_PRESSURE, copy=False)
    remarks = fields.Char(string='Remarks', required=True, default="El resultado de la prueba es válida por (05) años")
    cylinder_number = fields.Char(string='Cylinder Number')

    _sql_constraints = [
        ('hydrostatic_test_unique', 'unique(owner_id,date_hydrostatic_test)', 'A owner and date hydrostatic test must be unique!')
    ]
    
    def action_print_report_hydrostatic_test(self):
        return True
        """ return self.env.ref('entity_hydrostatic_test_line.action_print_report_hydrostatic_test').report_action(self)  """
    
    @api.model
    def create(self, vals):
        if vals.get('name','New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hydrostatic.test.certificate') or 'New'
        result = super(EntityHydrostaticTestLine, self).create(vals)
        return result
    
    @api.onchange("hydrostatic_test_result")
    def _onchange_hydrostatic_test_result(self):
        for record in self:
            if record.hydrostatic_test_result=='aprobado':
                record.remarks = "El resultado de la prueba es válida por (05) años"
                record.date_next_hydrostatic_test = record.date_hydrostatic_test + relativedelta(years=5)
            else:
                record.remarks = "Equipo es dado de baja"
                record.date_next_hydrostatic_test = False
    
    @api.onchange("date_hydrostatic_test")
    def _onchange_date_hydrostatic_test(self):
        for record in self:
            if record.date_hydrostatic_test:
                record.date_next_hydrostatic_test = record.date_hydrostatic_test + relativedelta(years=5)
            else:
                record.date_next_hydrostatic_test = False