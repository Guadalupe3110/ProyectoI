from modelo.db_fuentes_noticias import CL_FuentesNoticiasDB
from flask import request, session
import xml.etree.ElementTree as ET
import xmltodict
import requests

class CL_FuentesNoticias:

    #Lee el rss a xml
    def xml(self):
        xml= xmltodict.parse(requests.get('https://www.lanacion.com.ar/arcio/rss/').text)
        print(xml['rss']['channel']['item'][0]['category'])
        #print(xml['rss'])
        return xml
    
    #Retorna todas las fuentes de noticias
    def FN_ObtenerFuentes(self):
        return CL_FuentesNoticiasDB().FN_ObtenerFuentes()
    

    #Funcion para intertar fuente de noticia
    def FN_InsertarFuente(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            contenido = request.get_json(force = True)
            respuesta = {"Fuente": contenido}
            respuesta = CL_FuentesNoticiasDB().FN_NuevaFuente(respuesta)#Insertar fuente de noticia en base de datos 
            if(len(respuesta) != 0):
                res = "200 OK: Fuente creado con exito"
            else:
                res = "Error 400"
            return res
        else:
            return "Token invalido"
        

    #Moficiar fuente de noticia en la base de datos    
    def FN_ModificarFuente(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if request.method == 'GET':
                categoria = CL_FuentesNoticiasDB().FN_ObtenerFuenteID(id)
                return categoria
            else:
                contenido = request.get_json(force = True)
                respuesta = {"Fuente": contenido}
                respuesta = CL_FuentesNoticiasDB().FN_EditarFuente(respuesta, id)#Modificar fuente de noticia en base de datos 
                if(len(respuesta) != 0):
                    res = "200 OK: Fuente de noticia modificada con exito"
                else:
                    res = "Error 400"
                return res
        else:
            return "Token invalido"
        
    #Para verificar si se puede eliminar una fuente de noticia
    def FN_VerificarEliminar(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            categoria = CL_FuentesNoticiasDB().FN_VerificarEliminarFuente(id)
            if(categoria):
                res = "No puede"
            else:
                res = "Puede"
            return res
            
        else:
            return "Token invalido"
        
     #Eliminar fuente de noticia en la base de datos    
    def FN_EliminarFuente(self, id):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            if session['user']['idRoles'] == 1:
                categoria = CL_FuentesNoticiasDB().FN_EliminarFuente(id)#Eliminar fuente en base de datos 
                if(categoria):
                    res = "200 OK: Fuente eliminada con exito"
                else:
                    res = "Error 400"
                return res
            else:
                return "Usuario sin permisos"
        else:
            return "Token invalido"
