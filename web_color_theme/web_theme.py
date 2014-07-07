# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 ZestyBeanz Technologies Pvt. Ltd.
#    (http://wwww.zbeanztech.com)
#    contact@zbeanztech.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields

class web_themes_wizard(osv.osv_memory):
    _name = 'web.theme.wizard'
    _inherit = 'res.config.settings'
    _columns = {
                'module_top_bar_color_x': fields.char('Top Bar Gradient', size=7),
                'module_top_bar_color_y': fields.char('Top Bar Color', size=7),
                'module_view_manager_header_gradient_x': fields.char('View Manager Header Gradient', size=7),
                'module_view_manager_header_gradient_y': fields.char('View Manager Header Gradient', size=7),
                'module_left_bar_color': fields.char('Left Bar Color', size=7),
                'module_font_color': fields.char('Font Color', size=7),
                'module_main_menu_font': fields.char('Main Menu Font Color', size=7),
                'module_sub_menu_font': fields.char('Sub Menu Font Color', size=7),
                'module_top_bar_menu_font': fields.char('Top Bar Menu Font Color', size=16),
                'module_tab_string_color': fields.char('Tab String Font Color', size=7),
                'module_button_color_x': fields.char('Button Background Color', size=7),
                'module_button_color_y': fields.char('Button Background Color', size=7),
                'module_many2one_font_color': fields.char('Link Color', size=7),
                'module_form_background_url': fields.char('Form Background image URL', size=128)
                }
    
    def default_get(self, cr, uid, fields, context=None):
        web_theme_pool = self.pool.get('web.theme')
        res = super(web_themes_wizard, self).default_get(cr, uid, fields, context=context)
        web_theme_ids = web_theme_pool.search(cr, uid, [], context=context)
        if web_theme_ids:
            web_theme_obj = web_theme_pool.browse(cr, uid, web_theme_ids[0], context=context)
            vals = {
                    'module_top_bar_color_x': web_theme_obj.top_bar_color_x,
                    'module_top_bar_color_y': web_theme_obj.top_bar_color_y,
                    'module_view_manager_header_gradient_x': web_theme_obj.view_manager_header_gradient_x,
                    'module_view_manager_header_gradient_y': web_theme_obj.view_manager_header_gradient_y,
                    'module_left_bar_color': web_theme_obj.left_bar_color,
                    'module_font_color': web_theme_obj.font_color,
                    'module_main_menu_font': web_theme_obj.main_menu_font,
                    'module_sub_menu_font': web_theme_obj.sub_menu_font,
                    'module_top_bar_menu_font': web_theme_obj.top_bar_menu_font,
                    'module_tab_string_color': web_theme_obj.tab_string_color,
                    'module_button_color_x': web_theme_obj.button_color_x,
                    'module_button_color_y': web_theme_obj.button_color_y,
                    'module_many2one_font_color': web_theme_obj.many2one_font_color,
                    'module_form_background_url': web_theme_obj.form_background_url
                    }
            res.update(vals)
        return res
    
    def save_record(self, cr, uid, ids, context=None):
        web_theme_pool = self.pool.get('web.theme')
        data = self.read(cr, uid, ids, context=context)[0]
        vals = {
                'top_bar_color_x': data.get('module_top_bar_color_x'),
                'top_bar_color_y': data.get('module_top_bar_color_y'),
                'view_manager_header_gradient_x': data.get('module_view_manager_header_gradient_x'),
                'view_manager_header_gradient_y': data.get('module_view_manager_header_gradient_y'),
                'left_bar_color': data.get('module_left_bar_color'),
                'font_color': data.get('module_font_color'),
                'main_menu_font': data.get('module_main_menu_font'),
                'sub_menu_font': data.get('module_sub_menu_font'),
                'top_bar_menu_font': data.get('module_top_bar_menu_font'),
                'tab_string_color': data.get('module_tab_string_color'),
                'button_color_x': data.get('module_button_color_x'),
                'button_color_y': data.get('module_button_color_y'),
                'many2one_font_color': data.get('module_many2one_font_color'),
                'form_background_url': data.get('module_form_background_url'),
                }
        web_theme_ids = web_theme_pool.search(cr, uid, [], context=context)
        if web_theme_ids:
            web_theme_pool.write(cr, uid, web_theme_ids, vals, context=context)
        else:
            web_theme_ids = web_theme_pool.create(cr, uid, vals, context=context)
        return web_theme_ids

web_themes_wizard()

class web_themes(osv.osv):
    _name = 'web.theme'
    _columns = {
                'top_bar_color_x': fields.char('Top Bar Gradient', size=7),
                'top_bar_color_y': fields.char('Top Bar Color', size=7),
                'view_manager_header_gradient_x': fields.char('View Manager Header Gradient', size=7),
                'view_manager_header_gradient_y': fields.char('View Manager Header Gradient', size=7),
                'left_bar_color': fields.char('Left Bar Color', size=7),
                'font_color': fields.char('Font Color', size=7),
                'main_menu_font': fields.char('Main Menu Font Color', size=7),
                'sub_menu_font': fields.char('Sub Menu Font Color', size=7),
                'top_bar_menu_font': fields.char('Top Bar Menu Font Color', size=16),
                'tab_string_color': fields.char('Tab String Font Color', size=7),
                'button_color_x': fields.char('Button Background Color', size=7),
                'button_color_y': fields.char('Button Background Color', size=7),
                'many2one_font_color': fields.char('Link Color', size=7),
                'form_background_url': fields.char('Form Background image URL', size=128)
                }

web_themes_wizard()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: