# coding=utf-8
import uuid
import webapp2

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
        nr_comerciante = uuid.uuid4().hex
        params = {
            'nome': nome,
            'cnpj': cnpj,
            'nr_comerciante': nr_comerciante
        }
        return render_template('cadastro.html',params)
