# coding=utf-8
import os

import webapp2
import jinja2

import pages


ROUTES = [
    ('/', pages.Inicio),
    ('/cadastro', pages.Cadastro),
    ('/form_cadastro', pages.FormCadastro),
]

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__),
                             'templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
    extensions=['jinja2.ext.autoescape']
)

application = webapp2.WSGIApplication(ROUTES, debug=True)
