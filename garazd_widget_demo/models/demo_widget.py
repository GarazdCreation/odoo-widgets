# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import fields, models


class DemoWidget(models.Model):
    _name = "demo.widget"
    _description = 'Odoo Widgets Demo'

    name = fields.Char(
        string='Name',
    )
    calculator_int = fields.Integer(
        string='Calculator',
        help='The widget "calculator" allows to calculate digit values using '
             'a string representing as a simple formula.'
             'Supported arithmetic operations: + - * / ^ ( )',
    )
    calculator_float = fields.Float(
        string='Calculator',
        help='The widget "calculator" allows to calculate digit values using '
             'a string representing as a simple formula.'
             'Supported arithmetic operations: + - * / ^ ( )',
    )
