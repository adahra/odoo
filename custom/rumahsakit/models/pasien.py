from odoo import models, fields


class RumahSakitPasien(models.Model):
    _name = 'rumahsakit.pasien'
    _description = 'Master Pasien'
    _rec_name = 'nama'

    nama = fields.Char(string='Nama', required=True)
    umur = fields.Integer(string='Umur')
    keterangan = fields.Text(string='Catatan')
    foto = fields.Binary(string='Foto', attachment=True)
    gender = fields.Selection([
        ('laki', 'Laki-laki'),
        ('perempuan', 'Perempuan')
    ], string='Jenis Kelamin', default='laki')
