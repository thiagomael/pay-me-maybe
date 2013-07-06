# coding=utf-8
from google.appengine.ext import ndb
import webapp2

from models import Comerciante
from template_utils import render_template


class Inicio(webapp2.RequestHandler):
    def get(self):
        return render_template('index.html')


class FormCadastro(webapp2.RequestHandler):
    def get(self):
        return render_template('form_cadastro.html')


class Cadastro(webapp2.RequestHandler):
    def post(self):
        nome = self.request.get('nome')
        cnpj = self.request.get('cnpj')
        comerciante = Comerciante.cadastrar(nome, cnpj)
        params = {
            'nome': nome,
            'cnpj': cnpj,
            'nr_comerciante': comerciante.numero
        }
        return render_template('cadastro.html',params)
