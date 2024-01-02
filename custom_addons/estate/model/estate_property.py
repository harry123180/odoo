# 在 estate/models/estate_property.py 中
from odoo import models, fields, api
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='刀具名稱')
    description = fields.Text(string='描述')
    postcode = fields.Char(string='型號')
    date_availability = fields.Date(string='入庫日期')
    expected_price = fields.Float(string='購買 價格')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='庫存量', default=2)  # 新增，預設為 2
    living_area = fields.Integer(string='加工次數')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='不可使用')
    garden = fields.Boolean(string='唯一')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Char(string='Garden Orientation')
    price = fields.Float(string='Price', readonly=True)  # 新增，售價設為唯讀
    availability_date = fields.Date(string='Availability Date', default=lambda self: fields.Date.today() + timedelta(days=90))  # 新增，預設為 3 個月內

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Property name must be unique.'),
    ]

    # 在複製時不複製的字段
    def copy(self, default=None):
        default = dict(default or {})
        default.update({
            'price': 0.0,  # 複製時將售價設為 0.0
            'availability_date': False,  # 複製時不複製可用日期
        })
        return super(EstateProperty, self).copy(default)
