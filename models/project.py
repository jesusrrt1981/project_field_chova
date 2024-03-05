
from odoo import models, fields, api, _



class Project(models.Model):
    _inherit = "project.task"

    progress=fields.Integer(string="Progress")
    progress_child=fields.Integer(string="Progress")

