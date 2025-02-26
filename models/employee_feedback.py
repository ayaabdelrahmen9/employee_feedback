from odoo import api, fields, models
from odoo.exceptions import ValidationErrgior


class EmployeeFeedback(models.Model):
    _name = 'employee.feedback'
    _description = 'Employee Feedback'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    feedback = fields.Text(string='Feedback', required=True)
    date_submitted = fields.Date(string='Date Submitted', default=fields.Date.today)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('action_taken', 'Action Taken')
    ], string='Status', default='pending', tracking=True)

    category = fields.Selection([
        ('work_environment', 'Work Environment'),
        ('management', 'Management'),
        ('team_dynamics', 'Team Dynamics')
    ], string='Category')

    attachments = fields.Many2many('ir.attachment', string='Attachments')
    rating = fields.Integer(string='Rating', help='Rate from 1 to 5')

    @api.constrains('feedback')
    def _check_feedback_not_empty(self):
        for record in self:
            if not record.feedback.strip():
                raise ValidationError("Feedback cannot be empty.")

    @api.constrains('rating')
    def _check_rating(self):
        for record in self:
            if record.rating and (record.rating < 1 or record.rating > 5):
                raise ValidationError("Rating must be between 1 and 5.")


class Employee(models.Model):
    _inherit = 'hr.employee'

    feedback_ids = fields.One2many('employee.feedback', 'employee_id', string='Feedback')
