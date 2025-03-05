from odoo import models, fields, api

class NoteManagement(models.Model):
    _name = 'note.management'
    _description = 'Note Management'
    _inherit = ['mail.thread', 'mail.activity.mixin'] 

    title = fields.Char(string="Title", required=True, tracking=True)
    description = fields.Text(string="Description", tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ], string="Status", default='draft', tracking=True)

  