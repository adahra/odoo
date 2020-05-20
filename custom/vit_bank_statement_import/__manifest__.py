{
    "name": "Import Bank Statement",
    "version": "1.0",
    "author": "vitraining.com",
    "category": "Extra Tools",
    "website": "www.vitraining.com",
    "license": "AGPL-3",
    "summary": "",
    "description": """
        Base module for Import Bank Statement.
        Override the action_process() method to parse your custom bank statement import files.
    """,
    "depends": [
        "account",
    ],
    "data":[
        "views/vit_bank_statement_import_view.xml",
        "views/res_partner.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "qweb": [],
    "test": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}