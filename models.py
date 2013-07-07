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

    @classmethod
    def get_by_comerciante(cls, nr_comerciante, ordem, start_cursor=None):
        query = Pagamento.query(ancestor=ndb.Key(Comerciante, nr_comerciante))
        criterio = -Pagamento.hora
        query = query.order(criterio if ordem > 0 else criterio.reversed())
        cursor = ndb.Cursor(urlsafe=start_cursor)
        pagamentos, proximo, tem_mais = query.fetch_page(10, start_cursor=cursor)
        anterior = cursor.reversed()
        return (pagamentos if ordem > 0 else reversed(pagamentos),
                anterior.urlsafe() if anterior else '',
                proximo.urlsafe() if proximo else '',
                tem_mais)
