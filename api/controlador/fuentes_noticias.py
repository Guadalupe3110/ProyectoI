from modelo.db_fuentes_noticias import CL_FuentesNoticiasDB
from flask import request, session
import xml.etree.ElementTree as ET
import json

class CL_FuentesNoticias:
    
    #Retorna todas las fuentes de noticias
    def FN_ObtenerFuentes(self):
        fuentes = CL_FuentesNoticiasDB().FN_ObtenerFuentes()
        if fuentes:
            json_data = json.dumps(fuentes)
            return json_data, 200
    

    #Funcion para intertar fuente de noticia
    def FN_InsertarFuente(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            contenido = request.get_json(force = True)
            respuesta = {"Fuente": contenido}
            respuesta = CL_FuentesNoticiasDB().FN_NuevaFuente(respuesta)#Insertar fuente de noticia en base de datos 
            if(len(respuesta) != 0):
                res = "201 OK: Fuente creado con exito", 201
            else:
                res = "Error 400", 400
            return res
        else:
            return "Token invalido", 401
        

    #Moficiar fuente de noticia en la base de datos    
    def FN_ModificarFuente(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if request.method == 'GET':
                fuente = CL_FuentesNoticiasDB().FN_ObtenerFuenteID(id)
                if fuente:
                    json_data = json.dumps(fuente)
                    return json_data, 200
                else:
                    return "Categoría no encontrada", 404
            else:
                contenido = request.get_json(force = True)
                respuesta = {"Fuente": contenido}
                respuesta = CL_FuentesNoticiasDB().FN_EditarFuente(respuesta, id)#Modificar fuente de noticia en base de datos 
                if(len(respuesta) != 0):
                    return "200 OK: Fuente de noticia modificada con exito", 200
                else:
                        return "Error al modificar la fuente de noticia", 400
        else:
            return "Token invalido", 401
        
    #Para verificar si se puede eliminar una fuente de noticia
    def FN_VerificarEliminar(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            fuente = CL_FuentesNoticiasDB().FN_VerificarEliminarFuente(id)
            if(fuente):
                return "No puede", 409
            else:
                return "Puede", 200
        else:
            return "Token invalido", 401
        
     #Eliminar fuente de noticia en la base de datos    
    def FN_EliminarFuente(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if CL_FuentesNoticiasDB().FN_VerificarEliminarFuente(id):
                    res = "No se puede eliminar la fuente de noticias porque está relacionada a una noticia"
                    return res, 409
            else:
                fuente = CL_FuentesNoticiasDB().FN_EliminarFuente(id)#Eliminar fuente en base de datos 
                if(fuente):
                    res = "204 OK: Fuente eliminada con exito", 204
                else:
                    res = "Error 400", 400
                return res
        else:
            return "Token invalido", 401
