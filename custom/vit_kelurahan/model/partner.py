import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # after zip
    kelurahan_id = fields.Many2one(comodel_name="vit.kelurahan", string="Kelurahan", required=False, )
    kecamatan_id = fields.Many2one(comodel_name="vit.kecamatan", string="Kecamatan", required=False, )
    kota_id = fields.Many2one(comodel_name="vit.kota", string="Kota/Kab", required=False, )


class Kelurahan(models.Model):
    _name = 'vit.kelurahan'
    _description = 'Kelurahan model'

    name = fields.Char('Kelurahan')
    zip = fields.Integer(string="Kode POS", required=False, )
    kecamatan_id = fields.Many2one(comodel_name="vit.kecamatan", string="Kecamatan", required=False, )


class Kecamatan(models.Model):
    _name = 'vit.kecamatan'
    _description = 'Kecamatan model'

    name = fields.Char('Kecamatan', index=1)
    kota_id = fields.Many2one(comodel_name="vit.kota", string="Kota", required=False, )


class Kota(models.Model):
    _name = 'vit.kota'
    _description = 'Kota model'

    name = fields.Char('Kota/Kab', index=1)
    jenis = fields.Selection(string="Jenis", selection=[('kota', 'Kota'), ('kab', 'Kab.'), ], required=False, index=1)
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", required=False, )
