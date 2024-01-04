# 在 estate/models/estate_property.py 中
from odoo import models, fields, api
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    selling_state = fields.Char(string='Status',readonly=True)

    #新增Many2one 字段
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    salesman_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    #新增Many2Many 字段
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
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
    def action_sold(self):
        # 在這裡實現將房產設為已售的邏輯
        self.selling_state = "selled"
        print("SOLD has be press changes")
        if(self.selling_state !="selled"):
            return True
        else:
            print("警告 警告")
            return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': '警告',
                'message': '這是警告訊息。',
                'type': 'warning',  # 設置彈窗類型為警告
                'sticky': False,  # 彈窗是否持續顯示
            },
        }
            

    def action_cancel(self):
        # 在這裡實現取消房產的邏輯
        print("CANCEL has be press")
        return True
    # 在複製時不複製的字段
    def copy(self, default=None):
        default = dict(default or {})
        default.update({
            'price': 0.0,  # 複製時將售價設為 0.0
            'availability_date': False,  # 複製時不複製可用日期
        })
        return super(EstateProperty, self).copy(default)
class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(string='Type Name')
class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'

    name = fields.Char(string="Name")
  