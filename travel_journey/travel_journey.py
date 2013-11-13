# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
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

from openerp.osv import fields, orm


class travel_journey(orm.Model):
    _description = 'Journey of travel'
    _name = 'travel.journey'
    _columns = {
        'from': fields.many2one('res.country.state.city', 'From', required='True',
                                help='Source city of travel.'),
        'to': fields.many2one('res.country.state.city', 'To', required='True',
                              help='Destination city of travel.'),
        'passenger_id': fields.many2one('travel.passenger', 'Passenger', required='True',
                                        help='Passenger on this journey.'),

    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
