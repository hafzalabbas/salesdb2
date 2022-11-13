# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class partner_indexseq(models.Model):
    _inherit = 'res.partner'

    partner_index = fields.Char(string="Reg Number", readonly=True, copy=False)


    @api.model
    def create(self,vals):
        vals['partner_index'] = self.env['ir.sequence'].next_by_code('partner.indexseqid')
        if not self.ref:
            vals['ref'] = vals.get('partner_index')
        res = super(partner_indexseq, self).create(vals)
        return res

    @api.model
    def write(self, vals):
        if not self.partner_index:
            vals['partner_index'] = self.env['ir.sequence'].next_by_code('partner.indexseqid')
            if not vals.get('ref'):
                vals['ref'] = vals.get('partner_index')
        reswrite = super(partner_indexseq, self).write(vals)
        return reswrite
