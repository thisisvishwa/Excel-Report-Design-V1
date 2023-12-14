{
    "name": "report_designer_module",
    "version": "1.0",
    "category": "Reporting",
    "summary": "Advanced Reporting Module for Odoo v16 CE",
    "sequence": 1,
    "author": "Your Company",
    "website": "https://www.yourcompany.com",
    "description": """
    This module provides advanced reporting capabilities, allowing users to create, customize, and print detailed financial and analytical reports in MS Excel format (XLSX, XLSM).
    """,
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/report_designer_views.xml",
        "views/report_designer_templates.xml",
        "data/report_designer_data.xml"
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
    "external_dependencies": {
        "python": [],
        "bin": []
    },
    "qweb": ["static/src/xml/report_designer.xml"],
    "css": ["static/src/css/report_designer.css"],
    "js": ["static/src/js/report_designer.js"],
}