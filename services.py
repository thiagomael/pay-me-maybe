# coding=utf-8
from google.appengine.ext import ndb
from pysimplesoap.server import SoapDispatcher
from random import random
import webapp2

from models import Comerciante, Pagamento


def autorizar(nr_comerciante, cartao, quantia):
    if not Comerciante.exists(nr_comerciante):
        raise Exception("Comerciante inexistente: %s" % nr_comerciante)
    if random() < 0.7:
        Pagamento.efetuar(nr_comerciante, cartao, quantia)
        return "OK"
    else:
        return "NOT OK"


soap_dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://pay-me-maybe.appspot.com/pagamentocartao-1.0.0",
    action = 'http://pay-me-maybe.appspot.com/pagamentocartao-1.0.0', # SOAPAction
    namespace = 'http://pay-me-maybe.appspot.com/pagamentocartao-1.0.0',
    prefix="ns0",
    trace = True,
    ns = True)

soap_dispatcher.register_function(
    "requestAutorizar",
    autorizar,
    returns={"responseAutorizar": str},
    args={
        "nr_comerciante": str,
        "quantia": str,
        "cartao": {
            "numero": str,
            "nome": str,
            "data_validade": str,
            "cod_seguranca": str
        }
    }
)


class PagamentoCartaoService(webapp2.RequestHandler):
    def post(self):
        soap_request = self.request.body
        soap_response = soap_dispatcher.dispatch(soap_request)
        self.response.write(soap_response)


class Wsdl(webapp2.RequestHandler):
    def get(self):
        with open("pagamentocartao-1.0.0.wsdl", 'r') as f:
            self.response.headers['Content-Type'] = 'application/soap+xml'
            self.response.write(f.read())
