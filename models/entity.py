from odoo import _, api, models, fields
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class Entity(models.Model):
    _name = 'entity'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Entity'

    name = fields.Char(string='Name', tracking=True)
    image_entity= fields.Binary(string="Image", tracking=True )
    tag_ids = fields.Many2many("entity.tag", string="Tags", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    entity_type_id = fields.Many2one("entity.type", string="Type", options="{'no_create': True, 'no_create_edit':True}", tracking=True)
    entity_type_agent_id = fields.Many2one("entity.type.agent", string="Type Agent", options="{'no_create': True, 'no_create_edit':True}", required=True, tracking=True)
    entity_manufacturer_id = fields.Many2one("entity.manufacturer", string="Manufacturer", options="{'no_create': True, 'no_create_edit':True}", tracking=True)
    entity_model_id = fields.Many2one("entity.model", string="Model", options="{'no_create': True, 'no_create_edit':True}", tracking=True)
    category_id = fields.Many2one("entity.category", string="Category", options="{'no_create': True, 'no_create_edit':True}", required=True)
    entity_origin_id = fields.Many2one("entity.origin", string="Origin", options="{'no_create': True, 'no_create_edit':True}", tracking=True)
    date_manufacture = fields.Date(string="Date Manufacture", required=True, tracking=True)
    reference_document = fields.Char(String="Reference Document", tracking=True)
    note = fields.Html(string="Note", tracking=True)
    entity_cylinder_capacity_id = fields.Many2one("entity.cylinder.capacity", string="Cylinder Capacity", options="{'no_create': True, 'no_create_edit':True}", required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    unique_code = fields.Char(string='Unique Code', tracking=True)
    manufacturer_code = fields.Char(string='Manufacturer Code', tracking=True)
    application_code = fields.Char(string='Application Code', tracking=True)
    stamping_code = fields.Char(string='Stamping Code', tracking=True)
    heritage_code = fields.Char(string='Heritage Code', tracking=True)
    entity_percentage_load_id = fields.Many2one("entity.percentage.load", string="Percentage Load", options="{'no_create': True, 'no_create_edit':True}", tracking=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True, tracking=True)
    operating_lines_ids = fields.One2many("entity.operating.line", "entity_id", string="Operating Lines", tracking=True)
    hydrostatic_test_lines_ids = fields.One2many("entity.hydrostatic.test.line", "entity_id", string="Hydrostatic Test Lines", tracking=True)
    last_name_operating = fields.Char(compute="_compute_last_name_operating", string="Last Name Operating")
    last_reload_id = fields.Integer(compute="_compute_last_reload_id", string="Last Reload Id")
    last_reload_date = fields.Date(compute="_compute_last_reload_date", string="Last Reload Date")
    next_reload_date = fields.Date(compute="_compute_next_reload_date", string="Next Reload Date")
    last_owner_id = fields.Char(compute="_compute_last_owner_id", string="Last Owner")
    last_reload_location = fields.Char(compute="_compute_last_reload_location", string="Last Location")
    last_reload_cylinder_number = fields.Char(compute="_compute_last_reload_cylinder_number", string="Last Cylinder Number")
    last_technician_id = fields.Char(compute="_compute_last_technician_id", string="Last Technician")
    last_extinction_rating = fields.Char(compute="_compute_last_extinction_rating", string='Last Extinction Rating')
    last_name_hydrostatic_test = fields.Char(compute="_compute_last_name_hydrostatic_test", string="Last Name Hydrostatic Test")
    last_id_hydrostatic_test = fields.Integer(compute="_compute_last_id_hydrostatic_test", string="Last Id Hydrostatic Test")
    last_date_hydrostatic_test = fields.Date(compute="_compute_last_date_hydrostatic_test", string="Last Date Hydrostatic Test")
    last_date_next_hydrostatic_test = fields.Date(compute="_compute_last_date_next_hydrostatic_test", string="Last Date Next Hydrostatic Test")
    last_hydrostatic_test_result = fields.Char(compute="_compute_last_hydrostatic_test_result", string="Last Hydrostatic Test Result")
    last_test_pressure = fields.Char(compute="_compute_last_test_pressure", string="Last Test Pressure")
    last_hydrostatic_test_pressure = fields.Char(compute="_compute_last_hydrostatic_test_pressure", string="Last Hydrostatic Test Pressure")
    last_hydrostatic_test_cylinder_number = fields.Char(compute="_compute_last_hydrostatic_test_cylinder_number", string="Last Hydrostatic Test Cylinder Number")
    last_remarks = fields.Char(compute="_compute_last_remarks", string="Last Remarks")
    
    @api.model
    def create(self, vals):
        name_fields = ['entity_type_agent_id', 'category_id', 'entity_cylinder_capacity_id', 'serial_number']
        name_parts = []
        for field in name_fields:
            if field in vals:
                if field in ['entity_type_agent_id', 'category_id', 'entity_cylinder_capacity_id']:
                    related_model = self.env[self._fields[field].comodel_name]
                    related_record = related_model.browse(vals[field])
                    name_parts.append(related_record.name)
                else:
                    name_parts.append(str(vals[field]))
        vals['name'] = '/'.join(name_parts) if name_parts else "New"
        return super(Entity, self).create(vals)

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_name_operating(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_name_operating = last_record.name if last_record else ""
    
    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_reload_id(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_reload_id = last_record.id_loading if last_record else 0

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_reload_date(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_reload_date = last_record.date_loading if last_record else False

    @api.depends('operating_lines_ids.date_loading')
    def _compute_next_reload_date(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.next_reload_date = last_record.date_reloading if last_record else False

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_owner_id(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_owner_id = last_record.owner_id.name if last_record else ""

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_reload_location(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_reload_location = last_record.location if last_record else ""
            
    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_reload_cylinder_number(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_reload_cylinder_number = last_record.cylinder_number if last_record else 0

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_technician_id(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_technician_id = last_record.technician_id.name if last_record else 0

    @api.depends('operating_lines_ids.date_loading')
    def _compute_last_extinction_rating(self):
        for record in self:
            last_record = max(record.operating_lines_ids, key=lambda r: r.date_loading, default=False)
            record.last_extinction_rating = last_record.extinction_rating if last_record else ""

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_name_hydrostatic_test(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_name_hydrostatic_test = last_record.name if last_record else ""

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_id_hydrostatic_test(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_id_hydrostatic_test = last_record.id_hydrostatic_test if last_record else 0

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_date_hydrostatic_test(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_date_hydrostatic_test = last_record.date_hydrostatic_test if last_record else False

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_date_next_hydrostatic_test(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_date_next_hydrostatic_test = last_record.date_next_hydrostatic_test if last_record else False

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_hydrostatic_test_result(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_hydrostatic_test_result = last_record.hydrostatic_test_result if last_record else ""

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_test_pressure(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_test_pressure = last_record.test_pressure if last_record else ""

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_hydrostatic_test_pressure(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_hydrostatic_test_pressure = last_record.hydrostatic_test_pressure if last_record else ""

    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_remarks(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_remarks = last_record.remarks if last_record else ""
            
    @api.depends('hydrostatic_test_lines_ids.date_hydrostatic_test')
    def _compute_last_hydrostatic_test_cylinder_number(self):
        for record in self:
            last_record = max(record.hydrostatic_test_lines_ids, key=lambda r: r.date_hydrostatic_test, default=False)
            record.last_hydrostatic_test_cylinder_number = last_record.cylinder_number if last_record else 0
