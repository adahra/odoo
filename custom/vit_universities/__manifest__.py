#
# SI Akademik manifest file
#
{
    'name': 'Sistem Informasi Akademik Perguruan Tinggi',
    'version': '12.0.1.0.0',
    'depends': ['base', 'hr', 'account', 'account_voucher'],
    'author': 'vitraining.com',
    "website": "http://www.vitraining.com",
    'category': 'Tools',
    'description': """
            Sistem Informasi Akademik Perguruan Tinggi yang sudah di sesuaikan dengan standar perguruan tinggi yang ada di Indonesia
        """,
    'installable': True,
    'application': True,
    "auto_install": False,
    'data': [
        'views/akademik.xml',
        'views/partner.xml',
        'views/wisuda.xml',
        'views/spmb.xml',
        'views/operasional.xml',
        'views/kelas.xml',
        'views/employee.xml',
        'views/jadwal.xml',
        'views/kurikulum.xml',
        'views/invoice.xml',
        'views/pembayaran.xml',
        'views/product.xml',
        'views/tab_partner.xml',
        'reports/report.xml',
        'data/data_view.xml'
    ],
}
