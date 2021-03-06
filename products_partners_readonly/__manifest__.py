# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Products & Partners read-only MFH',
    'version': '12.0.1.0.0',
    'author': 'Falcon Solutions SpA',
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': 'Evita que se creen productos o partners en otras vistas.',
    'depends': ['sale', 'product', 'stock', 'account', 'purchase'],
    'data': [
        'views/purchase_order.xml',
        'views/sale_order.xml',
        'views/account_invoice.xml',
        'views/stock_picking.xml'
    ],
    'installable': True,
    'application': False,
    'demo': [],
    'test': []
}
