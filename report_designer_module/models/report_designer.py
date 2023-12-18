```python
from odoo import models, fields, api

class ReportDesigner(models.Model):
    _name = 'report.designer'
    _description = 'Report Designer'

    name = fields.Char(string='Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    field_ids = fields.Many2many('ir.model.fields', string='Fields')
    section_ids = fields.One2many('report.designer.section', 'report_id', string='Sections')
    parameter_ids = fields.One2many('report.designer.parameter', 'report_id', string='Parameters')
    template_id = fields.Many2one('ir.attachment', string='Template')
    description = fields.Text(string='Description')

class ReportDesignerSection(models.Model):
    _name = 'report.designer.section'
    _description = 'Report Designer Section'

    name = fields.Char(string='Name', required=True)
    report_id = fields.Many2one('report.designer', string='Report')
    parent_id = fields.Many2one('report.designer.section', string='Parent Section')
    field_ids = fields.Many2many('ir.model.fields', string='Fields')
    domain = fields.Char(string='Domain')

class ReportDesignerParameter(models.Model):
    _name = 'report.designer.parameter'
    _description = 'Report Designer Parameter'

    PARAMETER_TYPES = [
        ('char', 'Char'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('many2one', 'Many2one'),
        ('many2many', 'Many2many'),
        ('date', 'Date'),
        ('datetime', 'Datetime'),
        ('boolean', 'Boolean'),
    ]

    name = fields.Char(string='Name', required=True)
    report_id = fields.Many2one('report.designer', string='Report')
    parameter_type = fields.Selection(PARAMETER_TYPES, string='Type', required=True)
    required = fields.Boolean(string='Required')
    sequence = fields.Integer(string='Sequence')
```
