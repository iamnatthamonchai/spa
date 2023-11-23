# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
import base64

dict_theme_style = {

    'style_1':  {
        'primary_color': '#017e84',
        'primary_hover': '#015a5e',
        'primary_active': '#015a5e',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#714B67',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#68465f',
        'header_active_color': '#68465f',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#858585',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#77717e',
        'sidebar_color_2': '#c9a8a9',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_7',
        'chatter_position': 'sided',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#ad86a3',
        'loading_style': 'style_10',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_1',
    },

    'style_2':  {
        'primary_color': '#ffc107',
        'primary_hover': '#c79100',
        'primary_active': '#c79100',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#ffc107',
        'header_font_color': '#212121',
        'header_hover_color': '#c79100',
        'header_active_color': '#c79100',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#c79100',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#d1aa0e',
        'sidebar_color_2': '#f0cb35',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_1',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#ad8713',
        'loading_style': 'style_1',
        'checkbox_style':'style_3',
        'radio_style':'style_3',
        'scrollbar_style' : 'style_2',
        'discuss_chatter_style' : 'style_2',
        'app_icon_style' : 'style_2',
    },

    'style_3':  {
        'primary_color': '#5c77ff',
        'primary_hover': '#004ccb',
        'primary_active': '#004ccb',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#5c77ff',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#004ccb',
        'header_active_color': '#004ccb',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#004ccb',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#0072ff',
        'sidebar_color_2': '#00c6ff',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_2',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#394cad',
        'loading_style': 'style_2',
        'checkbox_style':'style_2',
        'radio_style':'style_2',
        'scrollbar_style' : 'style_3',
        'discuss_chatter_style' : 'style_3',
        'app_icon_style' : 'style_3',
    },
    'style_4':  {
        'primary_color': '#00bcd4',
        'primary_hover': '#008ba3',
        'primary_active': '#008ba3',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#00bcd4',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#008ba3',
        'header_active_color': '#008ba3',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#008ba3',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#00bcd4',
        'sidebar_color_2': '#02daf2',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_3',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#008BA3',
        'loading_style': 'style_3',
        'checkbox_style':'style_3',
        'radio_style':'style_3',
        'scrollbar_style' : 'style_4',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_4',
    },
    'style_5':  {
        'primary_color': '#ff5722',
        'primary_hover': '#c41c00',
        'primary_active': '#c41c00',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#ff5722',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#c41c00',
        'header_active_color': '#c41c00',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#c41c00',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#e43a15',
        'sidebar_color_2': '#e43a15',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_4',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#C41C00',
        'loading_style': 'style_4',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_5',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_1',
    },
    'style_6':  {
        'primary_color': '#673ab7',
        'primary_hover': '#320b86',
        'primary_active': '#320b86',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#673ab7',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#320b86',
        'header_active_color': '#320b86',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#320b86',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#6a3093',
        'sidebar_color_2': '#a044ff',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_5',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#3f1b7d',
        'loading_style': 'style_5',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_2',
    },
    'style_7':  {
        'primary_color': '#9e9e9e',
        'primary_hover': '#707070',
        'primary_active': '#707070',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#9e9e9e',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#707070',
        'header_active_color': '#707070',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#707070',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#757f9a',
        'sidebar_color_2': '#d7dde8',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_6',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#666666',
        'loading_style': 'style_6',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_2',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_3',
    },
    'style_8':  {
        'primary_color': '#4caf50',
        'primary_hover': '#087f23',
        'primary_active': '#087f23',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#4caf50',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#087f23',
        'header_active_color': '#087f23',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#087f23',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#1d976c',
        'sidebar_color_2': '#93f9b9',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_7',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#1b801f',
        'loading_style': 'style_7',
        'scrollbar_style' : 'style_3',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_4',
    },
    'style_9':  {
        'primary_color': '#ff9800',
        'primary_hover': '#c66900',
        'primary_active': '#c66900',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#ff9800',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#c66900',
        'header_active_color': '#c66900',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#c66900',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#ff512f',
        'sidebar_color_2': '#f09819',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_1',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#b5781f',
        'loading_style': 'style_8',
        'scrollbar_style' : 'style_4',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_1',
    },

    'style_10':  {
        'primary_color': '#e91e63',
        'primary_hover': '#b0003a',
        'primary_active': '#b0003a',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#e91e63',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#b0003a',
        'header_active_color': '#b0003a',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#b0003a',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#dd2476',
        'sidebar_color_2': '#ff512f',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_2',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#ab1a4b',
        'loading_style': 'style_9',
        'scrollbar_style' : 'style_5',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_2',
    },
    'style_11':  {
        'primary_color': '#9c27b0',
        'primary_hover': '#6a0080',
        'primary_active': '#6a0080',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#9c27b0',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#6a0080',
        'header_active_color': '#6a0080',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#6a0080',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#88219a',
        'sidebar_color_2': '#9733ee',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_3',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#741485',
        'loading_style': 'style_1',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_3',
    },
    'style_12':  {
        'primary_color': '#f44336',
        'primary_hover': '#ba000d',
        'primary_active': '#ba000d',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#f44336',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#ba000d',
        'header_active_color': '#ba000d',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#ba000d',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#d31027',
        'sidebar_color_2': '#ea384d',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_4',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#a8332a',
        'loading_style': 'style_11',
        'scrollbar_style' : 'style_2',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_4',
    },

    'style_13':  {
        'primary_color': '#009688',
        'primary_hover': '#00675b',
        'primary_active': '#00675b',
        'secondary_color': '#E6E6E6',
        'secondary_hover': '#CDCDCD',
        'secondary_active': '#CDCDCD',
        'header_background_color': '#009688',
        'header_font_color': '#FFFFFF',
        'header_hover_color': '#00675b',
        'header_active_color': '#00675b',
        'h1_color': '#4E4E4E',
        'h2_color': '#4E4E4E',
        'h3_color': '#4E4E4E',
        'h4_color': '#4E4E4E',
        'h5_color': '#4E4E4E',
        'h6_color': '#4E4E4E',
        'p_color': '#4E4E4E',
        'h1_size': 28,
        'h2_size': 17,
        'h3_size': 18,
        'h4_size': 20,
        'h5_size': 13,
        'h6_size': 12,
        'p_size': 13,
        'body_font_color': '#4E4E4E',
        'body_background_color': '#F9F9F9',
        'body_font_family': 'Roboto',
        'button_style': 'style_4',
        'separator_style': 'style_6',
        'separator_color': '#00675b',

        'body_background_type': 'bg_color',
        'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': False,
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'checkbox_style': 'default',
        'radio_style': 'default',
        'sidebar_color_1': '#007a6e',
        'sidebar_color_2': '#00b2a0',
        'sidebar_img': 'style_1',
        'breadcrumb_style': 'style_5',
        'chatter_position': 'normal',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#00675B',
        'loading_style': 'style_12',
        'scrollbar_style' : 'style_3',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_1',
    },
}


class sh_ent_theme_config_settings(models.Model):
    _name = 'sh.ent.theme.config.settings'
    _description = 'Back Theme Config Settings'

    name = fields.Char(string="Theme Settings")

    theme_style = fields.Selection([
        ('style_1', 'Default'),
        ('style_2', 'AMBER'),
        ('style_3', 'BLUE'),
        ('style_4', 'CYAN'),
        ('style_5', 'DEEP-ORANGE'),
        ('style_6', 'DEEP-PURPLE'),
        ('style_7', 'GRAY'),
        ('style_8', 'GREEN'),
        ('style_9', 'ORANGE'),
        ('style_10', 'PINK'),
        ('style_11', 'PURPLE'),
        ('style_12', 'RED'),
        ('style_13', 'TEAL'),
    ], string="Theme Color", default='style_1')

    primary_color = fields.Char(string='Primary Color', default='#00A09D')
    primary_hover = fields.Char(string='Primary Hover', default='#007a77')
    primary_active = fields.Char(string='Primary Active', default='#007a77')

    secondary_color = fields.Char(string='Secondary Color', default='#E6E6E6')
    secondary_hover = fields.Char(string='Secondary Hover', default='#CDCDCD')
    secondary_active = fields.Char(
        string='Secondary Active', default='#CDCDCD')

    header_background_color = fields.Char(
        string='Header Background Color', default='#875A7B')
    header_font_color = fields.Char(
        string='Header Font Color', default='#FFFFFF')
    header_hover_color = fields.Char(
        string='Header Hover Color', default='#68465f')
    header_active_color = fields.Char(
        string='Header Active Color', default='#68465f')

    h1_color = fields.Char(string='H1 Color', default='#4E4E4E')
    h2_color = fields.Char(string='H2 Color', default='#4E4E4E')
    h3_color = fields.Char(string='H3 Color', default='#4E4E4E')
    h4_color = fields.Char(string='H4 Color', default='#4E4E4E')
    h5_color = fields.Char(string='H5 Color', default='#4E4E4E')
    h6_color = fields.Char(string='H6 Color', default='#4E4E4E')
    p_color = fields.Char(string='P Color', default='#4E4E4E')

    h1_size = fields.Integer(string='H1 Size', default=28)
    h2_size = fields.Integer(string='H2 Size', default=17)
    h3_size = fields.Integer(string='H3 Size', default=18)
    h4_size = fields.Integer(string='H4 Size', default=20)
    h5_size = fields.Integer(string='H5 Size', default=13)
    h6_size = fields.Integer(string='H6 Size', default=12)
    p_size = fields.Integer(string='P Size', default=13)

    body_font_color = fields.Char(string='Body Font Color', default='#4E4E4E')
    body_background_type = fields.Selection([
        ('bg_color', 'Color'),
        ('bg_img', 'Image')
    ], string="Body Background Type", default="bg_color")

    body_background_color = fields.Char(
        string='Body Background Color', default="#F9F9F9")
    body_background_image = fields.Binary(string='Body Background Image ')
    body_font_family = fields.Selection([
        ('Roboto', 'Roboto'),
        ('Raleway', 'Raleway'),
        ('Poppins', 'Poppins'),
        ('Oxygen', 'Oxygen'),
        ('OpenSans', 'OpenSans'),
        ('KoHo', 'KoHo'),
        ('Ubuntu', 'Ubuntu'),
        ('custom_google_font', 'Custom Google Font'),
    ], string='Body Font Family', default='Roboto')

    body_google_font_family = fields.Char(string="Google Font Family")
    is_used_google_font = fields.Boolean(string="Is use google font?")

    button_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
    ], string='Button Style', default="style_4")
    is_button_with_icon_text = fields.Boolean(
        string="Button with text and icon?", default=False)

    separator_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Default'),
    ], string='Separator Style', default="style_6")

    separator_color = fields.Char(string="Separator Color", default="#5D1049")

    sidebar_color_1 = fields.Char(
        string="Background Color 1", default="#77717e")
    sidebar_color_2 = fields.Char(
        string="Background Color 2", default="#c9a8a9")
    sidebar_img = fields.Selection([('style_1', 'Style 1'), ('style_2', 'Style 2'), ('style_3', 'Style 3'), (
        'style_4', 'Style 4'), ('style_5', 'Style 5')], string=" Background Image", default='style_1')


#     sidebar_background_type = fields.Selection([
#         ('bg_color','Color'),
#         ('bg_img','Image')
#         ],string = "Sidebar Background Type", default = "bg_color")
#
#     sidebar_background_color = fields.Char(string = 'Sidebar Background Color')
#     sidebar_background_image = fields.Binary(string = 'Sidebar Background Image')
#
#     sidebar_font_color =  fields.Char(string = 'Sidebar Font Color')
#     sidebar_font_hover_color = fields.Char(string = 'Sidebar Font Hover Color')
#     sidebar_font_hover_background_color = fields.Char(string = 'Sidebar Font Hover Background Color')
#     sidebar_style = fields.Selection([
#         ('style_1','Style 1'),
#         ('style_2','Style 2'),
#         ('style_3','Style 3'),
#         ('style_4','Style 4'),
#         ('style_5','Style 5'),
#         ('style_6','Style 6'),
#         ('style_7','Style 7'),
#         ('style_8','Style 8'),
#         ], string = 'Sidebar Style')
    loading_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ('style_9', 'Style 9'),
        ('style_10', 'Style 10'),
        ('style_11', 'Style 11'),
        ('style_12', 'Style 12'),
    ], string='Loading Style', default="style_1")

    progress_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('none', 'None'),
    ], string='Progress Bar Style', default="style_1")

    progress_height = fields.Char("Height")
    progress_color = fields.Char("Color")

    loading_gif = fields.Binary(string="Loading GIF")
    loading_gif_file_name = fields.Char(string="Loading GIF File Name")

    list_view_border = fields.Selection([
        ('bordered', 'Bordered'),
        ('without_border', 'Without Border')
    ], default='without_border', string="List View Border")

    list_view_is_hover_row = fields.Boolean(string="Rows Hover?", default=True)
    list_view_hover_bg_color = fields.Char(
        string="Hover Background Color", default="#f5f5f5")
    list_view_even_row_color = fields.Char(
        string="Even Row Color", default="#FFFFFF")
    list_view_odd_row_color = fields.Char(
        string="Odd Row Color", default="#FFFFFF")

    login_page_style = fields.Selection([
        ('style_0', 'Odoo Standard'),
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
    ], string="Style", default='style_3')

    login_page_background_type = fields.Selection([
        ('bg_color', 'Color'),
        ('bg_img', 'Image')
    ], string="Background Type", default="bg_color")

    login_page_background_color = fields.Char(
        string='Background Color', default="#B3FFB8")
    login_page_background_image = fields.Binary(string='Background Image ')
    login_page_box_color = fields.Char(string='Box Color')
    login_page_banner_image = fields.Char(string='Banner Image')

    # Sticky
    is_sticky_form = fields.Boolean(string="Form Status Bar")
    is_sticky_chatter = fields.Boolean(string="Chatter")
    is_sticky_list = fields.Boolean(string="List View")
    is_sticky_list_inside_form = fields.Boolean(string="List View Inside Form")

    # Modal Popup
    modal_popup_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ('style_9', 'Style 9'),
        ('style_10', 'Style 10'),
        ('style_11', 'Default'),
    ], string='Popup Style', default='style_11')

    # mobile icon style
    mobile_icon_style = fields.Selection(
        [('default', 'Default'), ('floating', 'Floating')], string='Mobile Icon', default='default')

    # New checkbox icon style
    checkbox_style = fields.Selection([
        ('custom','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),
        ('default','Default'),                 
        ],string = 'Checkbox Style',default='custom')

    # New Radio icon style
    radio_style = fields.Selection([
        ('custom','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),
        ('default','Default'),                  
        ],string = 'Radio Button Style',default='custom')

    scrollbar_style = fields.Selection([
        ('style_1','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),
        ('style_4','Style 4'),
        ('style_5','Style 5'),                 
        ],string = 'Scrollbar Style',default='style_1')

    discuss_chatter_style = fields.Selection([
        ('style_1','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),                
        ],string = 'Discuss Chatter Style',default='style_1')

    app_icon_style = fields.Selection([
       ('style_1', 'Standard'),
        ('style_2', 'Line Icon'),
        ('style_3', '3D Icon'),
        ('style_4', 'Dual Tone'),
        ], string='App Icon Style', default='style_1')

    tab_style = fields.Selection([('horizontal', 'Horizontal'), (
        'vertical', 'Vertical')], string="Tab Style (Desktop)", default='horizontal')
    tab_style_mobile = fields.Selection([('horizontal', 'Horizontal'), (
        'vertical', 'Vertical')], string="Tab Style (Mobile)", default='vertical')

    horizontal_tab_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
    ], string='Horizontal Tab Style', default='style_7')

    vertical_tab_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
    ], string='Vertical Tab Style', default='style_7')

    form_element_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
    ], string='Form Element Style', default='style_7')

    chatter_position = fields.Selection(
        [('normal', 'Normal'), ('sided', 'Sided')], string="Chatter Position", default='normal')

    breadcrumb_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
    ], string='Breadcrumb Style', default='style_1')

    # def search_primary_var_template(self):
    #     if self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo():
    #         return self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo().active

    # def deactivate_primary_variable_scss(self):
    #     if self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo():
    #         self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo().write(
    #             {'active': False})
    #     if self.env.ref('sh_entmate_theme.sh_assets_background_color_scss').sudo():
    #         self.env.ref('sh_entmate_theme.sh_assets_background_color_scss').sudo().write(
    #             {'active': True})
    #     return True

    # def activate_primary_variable_scss(self):
    #     if self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo():
    #         self.env.ref('sh_entmate_theme.sh_assets_primary_variables').sudo().write(
    #             {'active': True})
    #     if self.env.ref('sh_entmate_theme.sh_assets_background_color_scss').sudo():
    #         self.env.ref('sh_entmate_theme.sh_assets_background_color_scss').sudo().write(
    #             {'active': False})
    #     return True

    @api.onchange('body_font_family')
    def onchage_body_font_family(self):
        if self.body_font_family == 'custom_google_font':
            self.is_used_google_font = True
        else:
            self.is_used_google_font = False
            self.body_google_font_family = False

    def action_preview_theme_style(self):
        if self:

            context = dict(self.env.context or {})
            img_src = ""
            if context and context.get('which_style', '') == 'theme':
                img_src = "/sh_ent_theme_config/static/src/img/preview/theme/style_theme.png"

            if context and context.get('which_style', '') == 'button':
                img_src = "/sh_ent_theme_config/static/src/img/preview/button/style_button.png"

            if context and context.get('which_style', '') == 'separator':
                img_src = "/sh_ent_theme_config/static/src/img/preview/separator/style_separator.png"

            if context and context.get('which_style', '') == 'sidebar':
                img_src = "/sh_ent_theme_config/static/src/img/preview/sidebar/style sidebar.png"

            if context and context.get('which_style', '') == 'login_page':
                img_src = "/sh_ent_theme_config/static/src/img/preview/login_page/style_login.png"

            if context and context.get('which_style', '') == 'mobile':
                img_src = "/sh_ent_theme_config/static/src/img/preview/mobile_preview.png"

            if context and context.get('which_style', '') == 'checkbox':
                img_src = "/sh_ent_theme_config/static/src/img/preview/checkbox_style_preview.png"

            if context and context.get('which_style', '') == 'scrollbar_style':
                img_src = "/sh_ent_theme_config/static/src/img/preview/scrollbar_style_gif.gif"

            if context and context.get('which_style', '') == 'discuss_chatter_style':
                img_src = "/sh_ent_theme_config/static/src/img/preview/discuss_chatter/discuss_chatter.png"

            if context and context.get('which_style', '') == 'app_icon_style':
                img_src = "/sh_ent_theme_config/static/src/img/preview/app_icon_style.png" 

            if context and context.get('which_style', '') == 'radio':
                img_src = "/sh_ent_theme_config/static/src/img/preview/radio_btn_style_preview.png"

            if context and context.get('which_style', '') == 'enterprise_svg':
                img_src = "/sh_ent_theme_config/static/src/img/preview/enterprise_svg_preview.png"

            if context and context.get('which_style', '') == 'loading':
                img_src = "/sh_ent_theme_config/static/src/img/preview/loading-gif.gif"

            context['default_img_src'] = img_src

            return {
                'name': _('Preview Style'),
                'view_mode': 'form',
                'res_model': 'sh.theme.preview.wizard',
                'view_id': self.env.ref('sh_ent_theme_config.sh_ent_theme_config_theme_preview_wizard_form').id,
                'type': 'ir.actions.act_window',
                'context': context,
                'target': 'new',
                'flags': {'form': {'action_buttons': False}}
            }

    def action_change_theme_style(self):
        print("\n\n\n\n action_change_theme_style")
        if self and self.theme_style:
            selected_theme_style_dict = dict_theme_style.get(
                self.theme_style, False)
            if selected_theme_style_dict:
                self.update(selected_theme_style_dict)

    @api.onchange('theme_style')
    def onchage_theme_style(self):

        if self and self.theme_style:
            selected_theme_style_dict = dict_theme_style.get(
                self.theme_style, False)
            if selected_theme_style_dict:
                self.update(selected_theme_style_dict)

    def write(self, vals):
        """
           Write theme settings data in a less file
        """

        print("\n\n\n THEME Style   ", vals)
        res = super(sh_ent_theme_config_settings, self).write(vals)
        if self:
            for rec in self:

                content = """   
$o-enterprise-color: %s;
$primaryColor:%s;
$primary_hover:%s;
$primary_active:%s;
$secondaryColor:%s;
$secondary_hover:%s;
$secondary_active:%s;
$list_td_th:0.75rem !important;

$header_bg_color:%s;
$header_font_color:%s;
$header_hover_color:%s;
$header_active_color:%s;

$h1_color:%s;
$h2_color:%s;
$h3_color:%s;
$h4_color:%s;
$h5_color:%s;
$h6_color:%s;
$p_color:%s;

$h1_size:%spx;
$h2_size:%spx;
$h3_size:%spx;
$h4_size:%spx;
$h5_size:%spx;
$h6_size:%spx;
$p_size:%spx;

$body_font_color:%s;
$body_background_type:%s;
$body_background_color:%s;
$body_font_family:%s;

$button_style:%s;
$o-mail-attachment-image-size: 100px !default;

$separator_style:%s;
$separator_color:%s;

$o-community-color:%s;
$o-tooltip-background-color:%s;
$o-brand-secondary:%s;
$o-brand-odoo: $o-community-color;
$o-brand-primary: $o-community-color;

$is_button_with_icon_text:%s;

$body_google_font_family:%s;
$is_used_google_font:%s;

$list_view_border:%s;
$list_view_is_hover_row:%s;
$list_view_hover_bg_color:%s;
$list_view_even_row_color:%s;
$list_view_odd_row_color:%s;

$login_page_style: %s;
$login_page_background_type: %s;
$login_page_background_color:%s;
$login_page_box_color:%s;
$theme_style: %s;

$is_sticky_form:%s;
$is_sticky_chatter:%s;
$is_sticky_list:%s;
$is_sticky_list_inside_form:%s;
 
$modal_popup_style:%s;
$mobile_icon_style:%s;
$checkbox_style:%s;
$radio_style:%s;
$scrollbar_style:%s;
$discuss_chatter_style:%s;
$app_icon_style:%s;

$sidebar_color_1:%s;
$sidebar_color_2:%s;
$sidebar_img:%s;
$tab_style:%s;
$tab_style_mobile:%s;
$horizontal_tab_style:%s;
$vertical_tab_style:%s;
$form_element_style:%s;
$chatter_position:%s;
$breadcrumb_style:%s;
$loading_style:%s;
$progress_style:%s;
$progress_height:%s;
$progress_color:%s;
                """ % (

                    rec.primary_color,
                    rec.primary_color,
                    rec.primary_hover,
                    rec.primary_active,

                    rec.secondary_color,
                    rec.secondary_hover,
                    rec.secondary_active,

                    rec.header_background_color,
                    rec.header_font_color,
                    rec.header_hover_color,
                    rec.header_active_color,


                    rec.h1_color,
                    rec.h2_color,
                    rec.h3_color,
                    rec.h4_color,
                    rec.h5_color,
                    rec.h6_color,
                    rec.p_color,


                    rec.h1_size,
                    rec.h2_size,
                    rec.h3_size,
                    rec.h4_size,
                    rec.h5_size,
                    rec.h6_size,
                    rec.p_size,

                    rec.body_font_color,
                    rec.body_background_type,
                    rec.body_background_color,
                    rec.body_font_family,

                    rec.button_style,




                    rec.separator_style,
                    rec.separator_color,

                    rec.primary_color,
                    rec.primary_color,
                    rec.secondary_color,
                    rec.is_button_with_icon_text,

                    rec.body_google_font_family,
                    rec.is_used_google_font,

                    rec.list_view_border,
                    rec.list_view_is_hover_row,
                    rec.list_view_hover_bg_color,
                    rec.list_view_even_row_color,
                    rec.list_view_odd_row_color,

                    rec.login_page_style,
                    rec.login_page_background_type,
                    rec.login_page_background_color,
                    rec.login_page_box_color,
                    rec.theme_style,

                    rec.is_sticky_form,
                    rec.is_sticky_chatter,
                    rec.is_sticky_list,
                    rec.is_sticky_list_inside_form,

                    rec.modal_popup_style,
                    rec.mobile_icon_style,
                    rec.checkbox_style,
                    rec.radio_style,
                    rec.scrollbar_style,
                    rec.discuss_chatter_style,
                    rec.app_icon_style,

                    rec.sidebar_color_1,
                    rec.sidebar_color_2,
                    rec.sidebar_img,
                    rec.tab_style,
                    rec.tab_style_mobile,
                    rec.horizontal_tab_style,
                    rec.vertical_tab_style,
                    rec.form_element_style,
                    rec.chatter_position,
                    rec.breadcrumb_style,
                    rec.loading_style,
                    rec.progress_style,
                    rec.progress_height,
                    rec.progress_color,
                )

                IrAttachment = self.env["ir.attachment"]
                # search default attachment by url that will created when app installed...
                url = "/sh_ent_theme_config/static/src/scss/back_theme_config_main_scss.scss"

                search_attachment = IrAttachment.sudo().search([
                    ('url', '=', url),
                ], limit=1)

                # Check if the file to save had already been modified
                datas = base64.b64encode((content or "\n").encode("utf-8"))
                if search_attachment:
                    # If it was already modified, simply override the corresponding attachment content
                    search_attachment.sudo().write({"datas": datas})

                else:
                    # If not, create a new attachment
                    new_attach = {
                        "name": "Back Theme Settings scss File",
                        "type": "binary",
                        "mimetype": "text/scss",
                        "datas": datas,
                        "url": url,
                        "public": True,
                        "res_model": "ir.ui.view",
                    }

                    IrAttachment.sudo().create(new_attach)

                # clear the catch to applied our new theme effects.
                self.env["ir.qweb"].clear_caches()

        return res