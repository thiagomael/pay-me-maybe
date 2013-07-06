# coding=utf-8
import json
import uuid

from google.appengine.ext import ndb


class Comerciante(ndb.Model):
    numero = ndb.StringProperty()
    nome = ndb.StringProperty()
    cnpj = ndb.StringProperty()

    @classmethod
    def cadastrar(cls, nome, cnpj):
        numero = uuid.uuid4().hex
        comerciante = Comerciante(id=numero)
        comerciante.nome = nome
        comerciante.cnpj = cnpj
        comerciante.numero = numero
        comerciante.put()
        return comerciante

    @classmethod
    def exists(cls, nr_comerciante):
        return cls.get_by_id(nr_comerciante) is not None


class Pagamento(ndb.Model):
    comerciante = ndb.KeyProperty(kind=Comerciante)
    quantia = ndb.StringProperty(indexed=False)
    cartao = ndb.JsonProperty()
    hora = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def efetuar(cls, nr_comerciante, cartao, quantia):
        comerciante = Comerciante.get_by_id(nr_comerciante)
        assert comerciante
        pagamento = Pagamento(parent=comerciante.key)
        pagamento.comerciante = comerciante.key
        pagamento.quantia = quantia
        pagamento.cartao = cartao
        pagamento.put()
