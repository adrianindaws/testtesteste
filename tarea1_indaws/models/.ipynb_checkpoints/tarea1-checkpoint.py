#-*- coding: utf-8 -*-

from odoo import models, fields, api
class productoPrueba(models.Model):
    _inherit = "res.partner"
    _descripcion = "Modulo campos many2one"
    
    
    user_senior_id = fields.Many2one('res.user', string = 'senior')
    user_junior_id = fields.Many2one('res.user', string = 'junior')
    user_tikcets_id = fields.Many2one('res.user', string = 'responsable tickets')
    
    