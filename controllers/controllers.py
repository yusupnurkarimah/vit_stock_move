# -*- coding: utf-8 -*-
from odoo import http

# class VitStockMove(http.Controller):
#     @http.route('/vit_stock_move/vit_stock_move/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_stock_move/vit_stock_move/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_stock_move.listing', {
#             'root': '/vit_stock_move/vit_stock_move',
#             'objects': http.request.env['vit_stock_move.vit_stock_move'].search([]),
#         })

#     @http.route('/vit_stock_move/vit_stock_move/objects/<model("vit_stock_move.vit_stock_move"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_stock_move.object', {
#             'object': obj
#         })