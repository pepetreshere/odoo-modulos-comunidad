openerp.web_color_theme = function(instance, m) {
var _t = instance.web._t,
    QWeb = instance.web.qweb;
    instance.web.WebClient.include({
        set_title: function() {
            var self = this;
            if (this.session.session_is_valid()){
	            new instance.web.Model("web.theme").get_func("search_read")([]).pipe(function(result) {
	                res = result[0]
	                if (res){
		                var top_bar_gradian_x = res["top_bar_color_x"]
		                var top_bar_gradian_y = res["top_bar_color_y"]
		                var view_manager_gradient_x = res["view_manager_header_gradient_x"]
		                var view_manager_gradient_y = res["view_manager_header_gradient_y"]
		                var button_color_x = res["button_color_x"]
		                var button_color_y = res["button_color_y"]
		                var main_menu_font = res["main_menu_font"]
		                var left_bar_color = "none repeat scroll 0 0 " + res["left_bar_color"]
		                var fornt_color = res['font_color']
		                var sub_menu_font = res['sub_menu_font']
		                var topbar_menu_font = res['top_bar_menu_font']
		                var tab_string_color = res['tab_string_color']
		                var many2one_font_color = res['many2one_font_color']
		                var form_background_image_url = "url(" + res['form_background_url'] + ") repeat scroll 0 0 transparent"
		                if ('WebkitTransform' in document.body.style){
		                    var top_gradiant = "-webkit-linear-gradient(top, "+top_bar_gradian_x+", "+top_bar_gradian_y+")"
		                    var view_manager_gradient = "-webkit-linear-gradient(top, "+view_manager_gradient_x+", "+view_manager_gradient_y+")"
		                    var button_gradient = "-webkit-linear-gradient(top, "+button_color_x+", "+button_color_y+")"
		                }
		                else if('MozTransform' in document.body.style){
		                    var top_gradiant = "-moz-linear-gradient(top, "+top_bar_gradian_x+", "+top_bar_gradian_y+")"
		                    var view_manager_gradient = "-moz-linear-gradient(top, "+view_manager_gradient_x+", "+view_manager_gradient_y+")"
		                    var button_gradient = "-moz-linear-gradient(top, "+button_color_x+", "+button_color_y+")"
		                }
		                else if('OTransform' in document.body.style){
		                    var top_gradiant = "-o-linear-gradient(top, "+top_bar_gradian_x+", "+top_bar_gradian_y+")"
		                    var view_manager_gradient = "-o-linear-gradient(top, "+view_manager_gradient_x+", "+view_manager_gradient_y+")"
		                    var button_gradient = "-o-linear-gradient(top, "+button_color_x+", "+button_color_y+")"
		                }
		                else if('transform' in document.body.style){
		                    var top_gradiant = "linear-gradient(top, "+top_bar_gradian_x+", "+top_bar_gradian_y+")"
		                    var view_manager_gradient = "linear-gradient(top, "+view_manager_gradient_x+", "+view_manager_gradient_y+")"
		                    var button_gradient = "linear-gradient(top, "+button_color_x+", "+button_color_y+")"
		                }
		                $('.openerp .oe_application a').css({ 'color': many2one_font_color});
		                $('.oe_topbar').css({ 'background-image': top_gradiant});
		                $('.oe_leftbar').css({ 'background': left_bar_color});
		                $('.openerp').css({ 'color': fornt_color});
		                $('.ui-widget-content').css({ 'color': fornt_color});
		                $('.openerp .oe_dropdown_menu > li > a').css({ 'color': fornt_color});
		                $('.oe_secondary_submenu li a').css({ 'color': sub_menu_font});
		                $('.oe_menu > li > a').css({ 'color': topbar_menu_font});
		                $('.oe_notebook > li > a').css({ 'color': tab_string_color});
		                $('.openerp a.button:link, .openerp a.button:visited, .openerp button, .openerp input[type="submit"], .openerp .ui-dialog-buttonpane .ui-dialog-buttonset .ui-button').css({ 'background-image': button_gradient});
		                $('.openerp .oe_secondary_menu_section').css({ 'color': main_menu_font});
		                $('.openerp .oe_application .oe_form_sheetbg').css({ 'background': form_background_image_url});
		                $('.oe_view_manager_current > .oe_view_manager_header').css({ 'background-image': view_manager_gradient});
		                $('.ui-dialog-titlebar').css({ 'background-image': view_manager_gradient});
	                }
	            });
            }
            this._super.apply(this, arguments);
        },
    });
};