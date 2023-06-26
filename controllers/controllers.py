# -*- coding: utf-8 -*-
# from odoo import http


# class Discipline(http.Controller):
#     @http.route('/discipline/discipline', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/discipline/discipline/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('discipline.listing', {
#             'root': '/discipline/discipline',
#             'objects': http.request.env['discipline.discipline'].search([]),
#         })

#     @http.route('/discipline/discipline/objects/<model("discipline.discipline"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('discipline.object', {
#             'object': obj
#         })
