from flask_sqlalchemy import SQLAlchemy
from datetime         import datetime
from sqlalchemy       import ForeignKey, Integer
from sqlalchemy.orm   import relationship
from mylead           import db

class Lead(db.Model):
    __tablename__       = 'Lead'
    id_lead             = db.Column(db.Integer,                                          primary_key = True)
    id_pessoa_lead      = db.Column(db.Integer, ForeignKey('Pessoa.id_pessoa'),          nullable = False)
    id_empresa_lead     = db.Column(db.Integer, ForeignKey('Empresa.id_empresa'),        nullable = False)
    id_rede_social_lead = db.Column(db.Integer, ForeignKey('RedeSocial.id_rede_social'), nullable = False)
    id_dono_lead        = db.Column(db.Integer, ForeignKey('RedeSocial.id_dono'),        nullable = False)

    id_Pessoa = relationship(Pessoa,         foreing_keys = [id_pessoa_lead])
    id_Empresa = relationship(Empresa,       foreing_keys = [id_empresa_lead])
    id_RedeSocial = relationship(RedeSocial, foreing_keys = [id_rede_social_lead])
    id_Dono = relationship(Dono,             foreing_keys = [id_dono_lead])

class Pessoa(db.Model):
    __tablename__    = 'Pessoa'
    id_pessoa        = db.Column(db.Integer,     primary_key=True)
    nome_pessoa      = db.Column(db.String(100), nullable = False)
    email_pessoa     = db.Column(db.String(100), nullable = False)
    telefone_usuario = db.Column(db.String(20),  nullable = True)
    celular_pessoa   = db.Column(db.String(20),  nullable = True)

class Empresa(db.Model):
    __tablename__ = 'Empresa'
    id_empresa    = db.Column(db.Integer,     primary_key=True)
    nome_empresa  = db.Column(db.String(100), nullable = False)
    qtdps_empresa = db.Column(db.Integer,     nullable = False)
    ramo_empresa  = db.Column(db.String(20),  nullable = False)

class Eventos(db.Model):
    __tablename__     = 'Eventos'
    id_evento         = db.Column(db.Integer,     primary_key=True)
    descricao_evento  = db.Column(db.String(100), nullable = False)
  
class Atividades(db.Model):
     __tablename__       = 'Atividades'
    id_atividade         = db.Column(db.Integer,     primary_key=True)
    descricao_atividade  = db.Column(db.String(100), nullable = False)

class Atuacao(db.Model):
    id_lead_atuacao      = db.Column(db.Integer, nullable = True)
    id_atividade_atuacao = db.Column(db.Integer, nullable = True)

    id_Lead      = relationship(Lead,      foreing_keys = [id_lead_atuacao])
    id_Atividade = relationship(Atividade, foreing_keys = [id_atividade_atuacao])

class Participacao(db.Model):
    id_lead_participacao       = db.Column(db.Integer, nullable = True)
    id_evento_participacao     = db.Column(db.Integer, nullable = True)

    id_Lead      = relationship(Lead, foreing_keys = [id_lead_participacao])
    id_Evento = relationship(Evento,  foreing_keys = [id_evento_participacao])


class RedeSocial(db.Model):
    __tablename__  = 'RedeSocial'
    id_rede_social = db.Column(db.Integer,   primary_key = True)
    link_fck       = db.Column(db.String(200), nullable = False)
    link_lkdn      = db.Column(db.String(200), nullable = False)
    link_twt       = db.Column(db.String(200), nullable = False)
    link_blog      = db.Column(db.String(200), nullable = False)

class DonoLead(db.Model):
    __tablename__ = 'DonoLead'
    id_dono       = db.Column(db.Integer,     primary_key=True)
    email_dono    = db.Column(db.String(100), nullable = False)
    nome_dono     = db.Column(db.String(100,  primary_key=True)
