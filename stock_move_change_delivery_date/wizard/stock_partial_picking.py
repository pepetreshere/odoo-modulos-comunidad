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
from lxml import etree

    
class stock_partial_picking_over(osv.osv_memory):
    _inherit = "stock.partial.picking"
   
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
    
        objects= self.pool.get('stock.partial.picking.line').search(cr, uid, [('wizard_id','=',partial.id)]) 
        for objeto in objects:
            obj=self.pool.get('stock.partial.picking.line').browse(cr, uid,objeto)
            
            if obj.product_id.standard_price == 0:
                  raise osv.except_osv(_("Warning"), _("Error valoracion!, No puede realizar este proceso algun producto tiene precio de costo cero"))
        context['date']=partial.date
        context['delivery_date']=partial.date
        return super(stock_partial_picking_over, self).do_partial(cr, uid, ids, context=context)


#        obj_sale = self.pool.get('sale.order')
#        obj_mclaim = self.pool.get('medical.claim')
#        obj_claim = self.browse(cr, uid, ids)
#    
#        for r in obj_claim:
#            #list_total_ids = obj_mclaim.search(cr,uid,[('sale_order_ids','=',r.sale_order_ids[0].id)], order='id')
#            list_sale_total_ids = obj_sale.search(cr,uid,[('medical_id','=',r.id)], order='id')
#            list_ids = obj_sale.search(cr,uid,[('medical_id','=',r.id),('state_claim','=',False)], order='id')
#            
#            leng_total = len(list_sale_total_ids)
#            leng = len(list_ids)
#            
#            if leng_total == leng:
#                for r_id in list_ids:
#                    obj_sale.write(cr, uid, r_id, {'state_claim':True})      
#            else:
#                newlist=[];
#                so ="";
#                for r1_id in list_sale_total_ids:
#                    if list_ids != newlist:
#                        for r_id in list_ids:
#                            cl = obj_sale.browse(cr, uid, r1_id).name
#                            if r1_id != r_id:
#                                so = so+cl;
#                    else:
#                        so = "Todas las reclamaciones"                                              
#                    # si es igual quiere decir que hay mas de dos reclamaciones con el campo 
#                    # r_id sales order
#                    # se debemandar un msn al usuario y quitar de la tabla sale_order_claim
#                raise osv.except_osv(_('Invalid Action!'), _('No se puede confirmar la reclamacion ya que las siguientes pedidos de venta ya estan reclamadas: %s.') %(so))
#                        
#        self.write(cr, uid, ids, {'state': 'confirm', 'date_confirm':time.strftime('%Y-%m-%d %H:%M:%S'),'date_upload':time.strftime('%Y-%m-%d')}, context=context)
#        return True
 


stock_partial_picking_over()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

