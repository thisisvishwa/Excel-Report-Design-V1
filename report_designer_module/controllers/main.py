```python
from odoo import http
from odoo.http import request

class ReportDesignerController(http.Controller):

    @http.route('/report_designer/generate_report', type='http', auth='user')
    def generate_report(self, **kwargs):
        report_designer = request.env['report.designer']
        report_id = kwargs.get('report_id')
        report = report_designer.browse(int(report_id))
        if report:
            file_data = report.generate_report()
            if file_data:
                return request.make_response(file_data,
                                             headers=[('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                                                      ('Content-Disposition', 'attachment; filename=report.xlsx;')])
        return request.redirect('/web#action=report_designer.action_report_designer')

    @http.route('/report_designer/send_report', type='json', auth='user')
    def send_report(self, report_id, email):
        report_designer = request.env['report.designer']
        report = report_designer.browse(int(report_id))
        if report:
            report.send_report(email)
        return {'status': 'success'}
```