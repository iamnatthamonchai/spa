# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "EnterpriseMate Backend Theme [For Community Edition]",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "license": "OPL-1",
    "category": "Themes/Backend",
    "version": "15.0.13",
    "summary": "Enterprise Backend Theme, Enterprise Theme, Backend Enterprise Theme, Flexible Enterprise Theme, Enter prise Theme Odoo",
    "description": """Do you want odoo enterpise look in your community version? Are You looking for modern, creative, clean, clear, materialise odoo enterpise look theme for your backend? So you are at the right place, We have made sure that this theme is highly clean, modern, fully customizable enterprise look theme. Cheers!""",
    "depends":
    [
        "web",
        "sh_ent_theme_config",
        "mail"
    ],

    "data":
    [
        "data/pwa_configuraion_data.xml",
        "security/base_security.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/pwa_configuration_view.xml",
        "views/assets.xml",
        "views/login_layout.xml",
        "views/notifications_view.xml",
        "views/send_notifications.xml",
        "views/web_push_notification.xml",
    ],

     'assets': {
       
        'web.assets_backend': [
            'sh_entmate_theme/static/src/scss/switch_button.scss',
            'sh_entmate_theme/static/src/scss/theme.scss',
            'sh_entmate_theme/static/src/scss/font.scss',
            'sh_entmate_theme/static/src/scss/buttons.scss',
            'sh_entmate_theme/static/src/scss/background-img.scss',
            'sh_entmate_theme/static/src/scss/saidbar.scss',
            'sh_entmate_theme/static/src/scss/separtor.scss',
            'sh_entmate_theme/static/src/scss/navbar.scss',
            'sh_entmate_theme/static/src/scss/form_view.scss',
            'sh_entmate_theme/static/src/scss/button_icon.scss',
            'sh_entmate_theme/static/src/scss/sidebar_bg.scss',
            'sh_entmate_theme/static/src/scss/theme_style_4.scss',
            'sh_entmate_theme/static/src/scss/popup_style.scss',
            'sh_entmate_theme/static/src/scss/menu_mobile.scss',
            'sh_entmate_theme/static/src/scss/sticky_chatter.scss',
            'sh_entmate_theme/static/src/scss/sticky_form.scss',
            'sh_entmate_theme/static/src/scss/sticky_list_inside_form.scss',
            'sh_entmate_theme/static/src/scss/sticky_list.scss',
            'sh_entmate_theme/static/src/js/menu.js',
            'sh_entmate_theme/static/src/js/global_search.js',
            'sh_entmate_theme/static/src/scss/global_search.scss',
            'sh_entmate_theme/static/src/js/apps_menu.js',
            'sh_entmate_theme/static/src/js/status_bar.js',
            # 'sh_entmate_theme/static/src/js/customize_user.js',
            'sh_entmate_theme/static/src/js/night_mode.js',
            'sh_entmate_theme/static/src/js/control_panel.js',
            'sh_entmate_theme/static/src/scss/quick_menu.scss',
            'sh_entmate_theme/static/src/js/quick_menu.js',
            'sh_entmate_theme/static/src/js/vertical_pen.js',
            'sh_entmate_theme/static/src/js/calculator.js',
            'sh_entmate_theme/static/src/js/language_selector.js',
            'sh_entmate_theme/static/src/scss/tab.scss',
            'sh_entmate_theme/static/src/scss/todo/todo.scss',
            'sh_entmate_theme/static/src/scss/form_element_style.scss',
            'sh_entmate_theme/static/src/scss/chatter_position.scss',
            'sh_entmate_theme/static/src/scss/calculator.scss',
            'sh_entmate_theme/static/src/scss/notification.scss',
            'sh_entmate_theme/static/src/scss/breadcrumb.scss',
            'sh_entmate_theme/static/src/scss/form_full_width.scss',
            'sh_entmate_theme/static/src/scss/loader.scss',
            'sh_entmate_theme/static/src/scss/checkbox_style/checkbox_style.scss',
            'sh_entmate_theme/static/src/scss/radio_btn_style/radio_btn_style.scss',

            # 'sh_entmate_theme/static/src/js/sh_bus_notification.js',
            # 'sh_entmate_theme/static/src/js/web_notification.js',
            'sh_entmate_theme/static/src/scss/nprogress.scss',
            'sh_entmate_theme/static/src/js/nprogress.js',
            'sh_entmate_theme/static/src/js/progressbar.js',
            'sh_entmate_theme/static/src/scss/background-color.scss',
            'sh_entmate_theme/static/index.js',
            'https://www.gstatic.com/firebasejs/8.4.3/firebase-app.js',
            'https://www.gstatic.com/firebasejs/8.4.3/firebase-messaging.js',
            'sh_entmate_theme/static/src/js/firebase.js',
            'sh_entmate_theme/static/src/js/todo.js',
            'sh_entmate_theme/static/src/js/todo_widget.js',

            'sh_entmate_theme/static/src/js/action_service.js',
            'sh_entmate_theme/static/src/js/route_service.js',
            'sh_entmate_theme/static/src/js/action_container.js',
          
            'sh_entmate_theme/static/src/js/dropdown.js',
            # 'sh_entmate_theme/static/src/js/profilesection.js',
            # 'sh_entmate_theme/static/src/js/control_panel_lagecy.js',
            
             'sh_entmate_theme/static/src/js/navbar.js',
            # ('replace', 'web/static/src/webclient/actions/action_container.js', 
            # 'sh_entmate_theme/static/src/js/action_container.js'),        
            'sh_entmate_theme/static/src/js/bus_notification.js',
            'sh_entmate_theme/static/src/scss/night_mode_user.scss',
            'sh_entmate_theme/static/src/js/menu_service.js',

        ],
        'web.assets_qweb': [
                "sh_entmate_theme/static/src/xml/sh_thread.xml",
                "sh_entmate_theme/static/src/xml/menu.xml",
                "sh_entmate_theme/static/src/xml/navbar.xml",
                "sh_entmate_theme/static/src/xml/form_view.xml",
                "sh_entmate_theme/static/src/xml/widget.xml",
                "sh_entmate_theme/static/src/xml/global_search.xml",
                "sh_entmate_theme/static/src/xml/base.xml",
                "sh_entmate_theme/static/src/xml/web_quick_menu.xml",
                "sh_entmate_theme/static/src/xml/todo.xml",
        ],
         'web.assets_frontend': [
            'sh_entmate_theme/static/src/scss/login_style_1.scss'
           
        ],
        
      
       
    },
    'images': [
        'static/description/banner.gif',
        'static/description/splash-screen_screenshot.gif'
    ],
    "live_test_url": "https://softhealer.com/contact_us",
    "installable": True,
    "application": True,
    "price": 73,
    "currency": "EUR",
    "bootstrap": True
}