# coding=utf-8
import os

import webapp2
import jinja2

import pages
import services


ROUTES = [
    ('/', pages.Inicio),
    ('/cadastro', pages.Cadastro),
    ('/form_cadastro', pages.FormCadastro),
    ('/pagamentos', pages.Pagamentos),
    ('/pagamentocartao-1.0.0/wsdl', services.Wsdl),
    ('/pagamentocartao-1.0.0/PagamentoCartaoService', services.PagamentoCartaoService),
]

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__),
                             'templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
    extensions=['jinja2.ext.autoescape']
)

application = webapp2.WSGIApplication(ROUTES, debug=True)
