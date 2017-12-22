from   flask import Flask, request, jsonify, render_template
from   dbhelper import *
from   flask_sqlalchemy import SQLAlchemy
from   mylead import app, db
from   controller.baseLeadsController import *

baseLeadsController = BaseLeadsController()

@app.route('/base', methods =['POST']) 
def distributionOfTables():
    
    data = request.get_json()

    
    new_user = Usuario(nome=data['nome'], email_usuario = data['email_usuario'],senha_usuario=hash, cnpj=data['cnpj'])
    oper_result = baseLeadsController.create_user(new_user)

    if oper_result == None:

        today = date.getDateToday()
        vencimento = date.getDateFuture()
        lastUser = baseLeadsController.getLast()
        new_order = Compra(data_compra = today, data_vencimento = vencimento, id_usuario=lastUser, id_plano= data['id_plano'])
        order = compraController.createComopra(new_order)

        return jsonify({'status': 'success', 'message': 'Usuario cadastrado', 'data': {}})

    else:
        return jsonify({'status': 'error', 'message': 'Email ja cadastrado', 'data': {} })
