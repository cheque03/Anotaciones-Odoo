#-*- coding: utf-8 -*

# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models, api

class PlantillaTest(models.Model):
    _name = 'plantilla.test'

    name = fields.Char(string='Demo', required=True,
    )
