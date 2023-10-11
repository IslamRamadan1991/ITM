from odoo  import models,fields

class ItServicesPassword(models.Model):
    _name ="itm.services.password"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description ="this can save all it services password with link"

    name = fields.Char("Service Username" , required=True)
    password = fields.Char("Service Password")
    link = fields.Char("link / Destinations")
    service_passwprd_type = fields.Selection(
        [
            ("domain", "active directory"),
            ("ksc", "kaspersky Security Center"),
            ("idrac", "IDRAC / Dell"),
            ("local", "Local Admin"),
            ("hostgator", "CPanel / Mail Server Cloud"),
            ("fortinet", "FortiGate Cloud"),
            ("dropbox", "DropBox Cloud"),
            ("orange", "Orange Domain Service Renewal"),
            ("qnap", "TND QNAP"),
            ("office", "Microsoft Office 365 Account"),
            ("pcon", "PCon"),
            ("itservice", "IT Service Password"),
            ("other", "Other Service Password"),
        ],
        "Service Password Type",
        required=True,
        default="other",
    )

    service_active = fields.Boolean("Services UP ?")
    service_note = fields.Char("Service Description / Comments")



