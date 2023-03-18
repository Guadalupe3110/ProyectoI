from modelo.db_categorias import CL_CategoriasDB
from flask import request, session
import json

class CL_Categorias:

    #Obtiene todas las categoria registradas por el administrador
    def FN_ObtenerCategorias(self):
        categorias = CL_CategoriasDB().FN_ObtenerCategorias()
        if categorias:
            json_data = json.dumps(categorias)
            return json_data, 200
        else:
            return "No se encontraron categorías", 204
    
    #Funcion para intertar categoria
    def FN_InsertarCategoria(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if session['user']['idRoles'] == 1:
                contenido = request.get_json(force = True)
                respuesta = {"Categoria": contenido}
                respuesta = CL_CategoriasDB().FN_NuevaCategoria(respuesta)#Insertar categoria en base de datos 
                if(len(respuesta) != 0):
                    return "201 OK: Categoría creada con éxito", 201
                else:
                    return "Error interno del servidor", 500
            else:
                return "Usuario sin permisos", 403
        else:
            return "Token invalido", 401
        
    #Moficiar ategoria en la base de datos    
    def FN_ModificarCategoria(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if session['user']['idRoles'] == 1:
                if request.method == 'GET':
                    categoria = CL_CategoriasDB().FN_ObtenerCategoriasID(id)
                    if categoria:
                        json_data = json.dumps(categoria)
                        return json_data, 200
                    else:
                        return "Categoría no encontrada", 404
                else:
                    contenido = request.get_json(force = True)
                    respuesta = {"Categoria": contenido}
                    respuesta = CL_CategoriasDB().FN_EditarCategoria(respuesta, id)#Modificar categoria en base de datos 
                    if(len(respuesta) != 0):
                        return "200 OK: Categoría modificada con éxito", 200
                    else:
                        return "Error al modificar la categoría", 400
            else:
                return "Usuario sin permisos", 403
        else:
            return "Token inválido", 401
        

    def FN_VerificarEliminar(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if session['user']['idRoles'] == 1:
                categoria = CL_CategoriasDB().FN_VerificarEliminarCategoria(id)#Eliminar categoria en base de datos 
                if categoria:
                    return "No puede", 409
                else:
                    return "Puede", 200
            else:
                return "Usuario sin permisos", 401
        else:
            return "Token invalido", 401
    
    #Eliminar ategoria en la base de datos    
    def FN_EliminarCategoria(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if session['user']['idRoles'] == 1:
                if CL_CategoriasDB().FN_VerificarEliminarCategoria(id):
                    res = "No se puede eliminar la categoría porque está relacionada a una fuente de noticia o noticia"
                    return res, 409
                else:
                    if CL_CategoriasDB().FN_EliminarCategoria(id):
                        res = "204 OK: Categoria eliminada con exito"
                        return res, 204
                    else:
                        res = "Error 400"
                        return res, 400
            else:
                return "Usuario sin permisos", 401
        else:
            return "Token invalido", 401
