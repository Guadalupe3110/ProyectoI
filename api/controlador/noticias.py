from modelo.db_noticias import CL_NoticiasDB
from modelo.db_fuentes_noticias import CL_FuentesNoticiasDB
from flask import request, session
import xmltodict
import requests
import json

class CL_Noticias:
    
    #Lee el rss a xml
    def xml(self, url):
        xml= xmltodict.parse(requests.get(url).text)
        return xml
    
    #Funcion para intertar fuente de noticia
    def FN_InsertarNoticia(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            contenido = request.get_json(force = True)
            new = self.FN_ObtenerInfo(contenido)
            respuesta = CL_NoticiasDB().FN_NuevaNoticia(new)#Insertar noticia en base de datos 
            if(respuesta):
                res = "201 OK: Noticia creada con exito", 201
            else:
                res = "Error 400", 400
            return res
        else:
            return "Token invalido", 401
        
    #Obtiene la informacion necesaria para insertar noticia
    def FN_ObtenerInfo(self, contenido):
        fuente = CL_FuentesNoticiasDB().FN_ObtenerFuenteID(contenido['idNewsSource'])[0]
        noticiaXML = self.xml(fuente['url'])
        new = { 'title': noticiaXML['rss']['channel']['item'][0]['title'],
               'short_description': noticiaXML['rss']['channel']['item'][0]['description'],
               'permanlink': noticiaXML['rss']['channel']['item'][0]['link'],
               'date': noticiaXML['rss']['channel']['item'][0]['pubDate'],
               'idNewsSource': contenido['idNewsSource'],
               'idUsers': session['user']['idUsers'],
               'idCategories': fuente['idCategories']

        }
        respuesta = {"Noticia": new}
        return respuesta
    
    #Retorna las noticias de usuario logueado
    def FN_ObtenerNoticiasUsuario(self):
        noticias = CL_NoticiasDB().FN_ObtenerNoticiaUsuario()
        if len(noticias) != 0:
            json_data = json.dumps(noticias)
            return json_data, 200
        else:
            return "sin datos", 204
        
    #Retorna las noticias de usuario logueado por categoria
    def FN_ObtenerNoticiasUsuarioCategoria(self, idCategoria):
        noticias = CL_NoticiasDB().FN_ObtenerNoticiaUsuarioCategoria(idCategoria)
        if len(noticias) != 0:
            json_data = json.dumps(noticias)
            return json_data, 200
        else:
            return "sin datos", 204
