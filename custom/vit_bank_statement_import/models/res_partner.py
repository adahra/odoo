import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    mid = fields.Char(string="MID", required=False)
    va = fields.Char(string="Virtual Account", required=False)
