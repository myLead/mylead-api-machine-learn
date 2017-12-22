from DAO.baseLeadsDAO import *

class BaseLeadsController():

    def __init__(self):
        self.__baseLeadsDAO = BaseLeadsDAO()

    #CONECTAR A CRAÇÃO DAS TABELAS PLANO E COMPRA JUNTO 
    #COM A TABELAD DE USUARO
    def create_user(self, user):

        usuarioexistente = self.__baseLeadsDAO.get_user_by_email(user.email_usuario)

        if usuarioexistente == None:
    
            user = self.__baseLeadsDAO.create_user(user)
            return user

        else:
            return usuarioexistente
