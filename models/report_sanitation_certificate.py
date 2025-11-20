# -*- coding: utf-8 -*-
from odoo import api, models

class ReportSanitationCertificate(models.AbstractModel):
    _name = 'report.entity.report_sanitation_certificate_pdf'
    _description = 'Sanitation Certificate Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['entity.sanitation.certificate'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'entity.sanitation.certificate',
            'docs': self.env['entity.sanitation.certificate'].browse(docids),
        }