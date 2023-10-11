from odoo import fields,models

class ItEquipmentRepair(models.Model):
    _name = "itm.equipment.repair"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "this class allow you to register the history of repair in IT"
    _order = "date desc"



    name = fields.Char("IT Description")
    partner_id = fields.Many2one(
        "res.partner",
        "Partner",
        required=True,
        domain="[('manage_it','=',1)]",
        tracking=True,
        help="A partner or user which are using this device",
    )
    equipment_id = fields.Many2one("itm.equipment", "Asset", ondelete="cascade")
    user_id = fields.Many2one(
        "res.users", "User", required=True, default=lambda self: self.env.user.id
    )
    component_type_id = fields.Many2one("itm.equipment.component.type", required=True)
    date = fields.Date(default=fields.Datetime.now())
    charge_type = fields.Selection(
        [
            ("user", "User Charge"),
            ("company", "Company Charge"),
        ],
        "Payment Charge Type",
        required=True,
        default="user",
    )
    erp_expense = fields.Char("ERP Expense #")
    item_cost = fields.Float("Cost")
    note = fields.Char("Spare Parts Notes")


