# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2012 Camptocamp SA
# @author Vincent Renaville
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
from osv import fields, osv
from tools.translate import _
import time


    
class stock_partial_move_over(osv.osv_memory):
    _inherit = "stock.partial.move"
   
    def do_partial(self, cr, uid, ids, context=None):
        """ Makes partial moves and pickings done.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param fields: List of fields for which we want default values
        @param context: A standard dictionary
        @return: A dictionary which of fields with values.
        """
        if context is None:
            context = {}
        partial = self.browse(cr, uid, ids[0], context=context)
        context['date']=partial.date
        context['delivery_date']=partial.date
        return super(stock_partial_move_over, self).do_partial(cr, uid, ids, context=context)

stock_partial_move_over()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

