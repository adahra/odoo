from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    npm = fields.Char('partner_id', string='NPM', readonly=True)