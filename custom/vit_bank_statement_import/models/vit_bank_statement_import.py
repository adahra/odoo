import base64
import logging

from odoo import fields, api, models, _
from odoo.exceptions import Warning, UserError

_logger = logging.getLogger(__name__)


class VitBankStatementImport(models.Model):
    _name = "vit.bank.statement.import"
    _description = "Bank Statement Import"

    bank_name = fields.Selection([], string='Bank Name', required=True)
    name = fields.Char(string='Number', default='New', required=True)
    date_import = fields.Date(string='Import Date', default=fields.Datetime.now)
    journal_id = fields.Many2one('account.journal', string='Bank Journal', required=True)
    file_data = fields.Binary(string='Import File')
    filename = fields.Char(string='File Name')
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], string='State', default='draft', copy=False)
    company_id = fields.Many2one("res.company", string="Company",
                                 default=lambda self: self.env['res.company']._company_default_get(), required=True)
    bank_statement_id = fields.Many2one(comodel_name="account.bank.statement", string="Bank Statment", copy=False)
    is_only_date = fields.Boolean(string="Import only this date",
                                  help="Import only bank statement lines on this import date?", default=True)
    is_search_mid = fields.Boolean(string="Search partner by MID", help="Automatically search partner by MID?",
                                   default=True)

    def get_sequence(self, vals):
        pref = vals['bank_name'].split(' ')
        pref = str(pref[0])
        company_id = self.env['res.company'].browse(vals['company_id'])
        # supaya lebih generic
        # wh_code = company_id.warehouse_id.code
        wh_code = company_id.name[0:4]
        sequence_id = self.env['ir.sequence'].search([
            ('code', '=', self._name),
            ('prefix', '=', '%s/%s/' % (wh_code, pref)),
            ('company_id', '=', vals['company_id']),
        ], limit=1)
        if not sequence_id:
            sequence_id = self.env['ir.sequence'].sudo().create({
                'name': 'BS Import %s %s' % (wh_code, pref),
                'code': self._name,
                'company_id': vals['company_id'],
                'implementation': 'no_gap',
                'prefix': '%s/%s/' % (wh_code, pref),
                'padding': 5,
            })
        return sequence_id.next_by_id()

    @api.model
    def create(self, vals):
        vals['name'] = self.get_sequence(vals)
        return super(VitBankStatementImport, self).create(vals)

    @api.multi
    def validity_check(self):
        self.ensure_one()
        if not self.journal_id.default_debit_account_id or not self.journal_id.default_credit_account_id:
            raise UserError(
                _('You have to set a Default Debit Account and a Default Credit Account for the journal: %s') % (
                    self.journal_id.name))
        lines = base64.b64decode(self.file_data)
        if not lines:
            raise UserError(_('Empty file content: %s') % (self.filename))

    @api.multi
    def action_process(self):
        for me_id in self:
            if me_id.state != 'draft':
                continue
            me_id.validity_check()
            me_id.write({'state': 'done'})

    @api.multi
    def action_cancel(self):
        for me_id in self:
            me_id.state = 'draft'
            me_id.bank_statement_id.unlink()

    @api.multi
    def unlink(self):
        for me_id in self:
            if me_id.state != 'draft':
                raise Warning('Tidak bisa menghapus data yang bukan draft !')
        return super(VitBankStatementImport, self).unlink()
