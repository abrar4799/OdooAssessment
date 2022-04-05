from unicodedata import name
from odoo import models, fields 

class ConpartnersModel(models.Model):
    _name = "copartners.model"
    #_inherit = 'mail.thread'
    _rec_name = 'name'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True,tracking=True )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True )
    country= fields.Char( tracking=True )
    joining_date=fields.Date( tracking=True )
    tag_ids = fields.Many2many('custom.model.tags', tracking=True )
    customer_id = fields.Many2many('res.partner',tracking=True )
    company_id = fields.Many2one('res.company', required=True ,tracking=True )
    notes=fields.Char( tracking=True )
    comments=fields.Char(tracking=True )

class TagsModel(models.Model):
     _name = 'tags.model'
     _rec_name = 'tag_name'

     tag_name = fields.Char( tracking=True)


    