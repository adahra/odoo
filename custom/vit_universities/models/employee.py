from odoo import fields, models


class HREmployee(models.Model):
    _inherit = 'hr.employee'
    _name = 'hr.employee'

    def _get_master_jadwal(self, cr, uid, ids, ):
        result = {}
        emp_id = self.browse(cr, uid, ids[0]).id
        # import pdb;pdb.set_trace()
        jad_obj = self.pool.get('master.jadwal')
        jad_ids = jad_obj.search(cr, uid, [
            ('employee_id', '=', emp_id),
            ('is_active', '=', True)], )
        if jad_ids == []:
            return result
        result[emp_id] = jad_ids
        return result

    is_dosen = fields.Boolean('Dosen')
    master_jadwal_ids = fields.Many2many(_get_master_jadwal, relation="master.jadwal", string="Jadwal Mengajar")
