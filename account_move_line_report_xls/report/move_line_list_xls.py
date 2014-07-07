# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    
#    Copyright (c) 2013 Noviat nv/sa (www.noviat.be). All rights reserved.
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

import xlwt
import time
from datetime import datetime
from report import report_sxw
from report_xls.report_xls import report_xls
from report_xls.utils import rowcol_to_cell
from account_move_line_report.report.move_line_list_print import move_line_list_print
from tools.translate import _
import logging
_logger = logging.getLogger(__name__)

class move_line_xls(report_xls):
    
    def generate_xls_report(self, _p, _xs, data, objects, wb):

        report_name = objects[0]._description or objects[0]._name
        ws = wb.add_sheet(report_name[:31])
        ws.panes_frozen = True
        ws.remove_splits = True
        ws.portrait = 0 # Landscape
        ws.fit_width_to_pages = 1
        row_pos = 0
        
        # set print header/footer
        ws.header_str = self.xls_headers['standard']
        ws.footer_str = self.xls_footers['standard']

        # Title
        cell_style = xlwt.easyxf(_xs['xls_title'])
        c_specs = [
            ('report_name', 1, 0, 'text', report_name),
        ]       
        row_data = self.xls_row_template(c_specs, ['report_name'])
        row_pos = self.xls_write_row(ws, row_pos, row_data, row_style=cell_style)
        row_pos += 1

        # Column headers
        rh_cell_format = _xs['bold'] + _xs['fill'] + _xs['borders_all']
        rh_cell_style = xlwt.easyxf(rh_cell_format)
        rh_cell_style_center = xlwt.easyxf(rh_cell_format + _xs['center'])
        rh_cell_style_right = xlwt.easyxf(rh_cell_format + _xs['right'])  
        c_specs = [
            ('move', 1, 20, 'text', _('Move')),
            ('name', 1, 42, 'text', _('Name')),
            ('date', 1, 13, 'text', _('Effective Date')),
            ('period', 1, 12, 'text', _('Period')),
            ('partner', 1, 36, 'text',  _('Partner')),
            ('account', 1, 12, 'text',  _('Account')),
            ('maturity', 1, 13, 'text',  _('Maturity Date')),
            ('debit', 1, 18, 'text',  _('Debit'), None, rh_cell_style_right),
            ('credit', 1, 18, 'text',  _('Credit'), None, rh_cell_style_right),
            ('balance', 1, 18, 'text',   _('Balance'), None, rh_cell_style_right),
            ('reconcile', 1, 12, 'text',  _('Rec.'), None, rh_cell_style_center),
            ('reconcile_partial', 1, 12, 'text',  _('Part. Rec.'), None, rh_cell_style_center),
        ]       
        row_data = self.xls_row_template(c_specs, [x[0] for x in c_specs])
        row_pos = self.xls_write_row(ws, row_pos, row_data, row_style=rh_cell_style, set_column_size=True)        
        ws.set_horz_split_pos(row_pos)   
        
        # account move lines
        aml_cell_format = _xs['borders_all']
        aml_cell_style = xlwt.easyxf(aml_cell_format)
        aml_cell_style_center = xlwt.easyxf(aml_cell_format + _xs['center'])
        aml_cell_style_date = xlwt.easyxf(aml_cell_format + _xs['left'], num_format_str = report_xls.date_format)
        aml_cell_style_decimal = xlwt.easyxf(aml_cell_format + _xs['right'], num_format_str = report_xls.decimal_format)
        for line in objects:
            debit_cell = rowcol_to_cell(row_pos, 7)
            credit_cell = rowcol_to_cell(row_pos, 8)
            bal_formula = debit_cell + '-' + credit_cell
            c_specs = [
                ('move', 1, 0, 'text', line.move_id.name or ''),
                ('name', 1, 0, 'text', line.name or ''),
                ('date', 1, 0, 'date', datetime.strptime(line.date,'%Y-%m-%d'), None, aml_cell_style_date),
                ('period', 1, 0, 'text', line.period_id.code or ''),
                ('partner', 1, 0, 'text', line.partner_id and line.partner_id.name or ''),
                ('account', 1, 0, 'text', line.account_id.code),
            ]
            if line.date_maturity.val:
                c_specs += [
                    ('maturity', 1, 0, 'date', datetime.strptime(line.date_maturity,'%Y-%m-%d'), None, aml_cell_style_date),
                ]
            else:
                c_specs += [
                    ('maturity', 1, 0, 'text', None),
                ]                                  
            c_specs += [
                ('debit', 1, 0, 'number', line.debit, None, aml_cell_style_decimal),
                ('credit', 1, 0, 'number', line.credit, None, aml_cell_style_decimal),
                ('balance', 1, 0, 'number', None, bal_formula, aml_cell_style_decimal),
                ('reconcile', 1, 0, 'text', line.reconcile_id.name or '', None, aml_cell_style_center),                
                ('reconcile_partial', 1, 0, 'text', line.reconcile_partial_id.name or '', None, aml_cell_style_center),                
            ]
            row_data = self.xls_row_template(c_specs, [x[0] for x in c_specs])
            row_pos = self.xls_write_row(ws, row_pos, row_data, row_style=aml_cell_style)

        # Totals           
        rt_cell_format = _xs['bold'] + _xs['fill'] + _xs['borders_all']
        rt_cell_style = xlwt.easyxf(rt_cell_format)
        rt_cell_style_right = xlwt.easyxf(rt_cell_format + _xs['right'])       
        rt_cell_style_decimal = xlwt.easyxf(rt_cell_format + _xs['right'], num_format_str = report_xls.decimal_format)

        aml_cnt = len(objects)
        debit_start = rowcol_to_cell(row_pos - aml_cnt, 7)
        debit_stop = rowcol_to_cell(row_pos - 1, 7)
        debit_formula = 'SUM(%s:%s)' %(debit_start, debit_stop)
        credit_start = rowcol_to_cell(row_pos - aml_cnt, 8)
        credit_stop = rowcol_to_cell(row_pos - 1, 8)
        credit_formula = 'SUM(%s:%s)' %(credit_start, credit_stop)
        debit_cell = rowcol_to_cell(row_pos, 7)
        credit_cell = rowcol_to_cell(row_pos, 8)
        bal_formula = debit_cell + '-' + credit_cell

        c_specs = [('empty%s'%i, 1, 0, 'text', None) for i in range(1,8)] 
        c_specs += [
            ('debit', 1, 0, 'number', None, debit_formula, rt_cell_style_decimal),
            ('credit', 1, 0, 'number', None, credit_formula, rt_cell_style_decimal),
            ('balance', 1, 0, 'number', None, bal_formula, rt_cell_style_decimal),
        ]       
        c_specs += [('empty%s'%i, 1, 0, 'text', None) for i in range(11,13)] 
        row_data = self.xls_row_template(c_specs, [x[0] for x in c_specs])
        row_pos = self.xls_write_row(ws, row_pos, row_data, row_style=rt_cell_style_right) 


move_line_xls('report.move.line.list.xls', 
    'account.move.line',
    parser=move_line_list_print)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: