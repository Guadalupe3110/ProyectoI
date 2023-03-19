from modelo.db_noticias import CL_NoticiasDB
from flask import request, session

class CL_Noticias:
    
    #Funcion para intertar fuente de noticia
    def FN_InsertarNoticia(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            contenido = request.get_json(force = True)
            respuesta = {"Noticia": contenido}
            respuesta = CL_NoticiasDB().FN_NuevaNoticia(respuesta)#Insertar noticia en base de datos 
            if(len(respuesta) != 0):
                res = "201 OK: Noticia creada con exito", 201
            else:
                res = "Error 400", 400
            return res
        else:
            return "Token invalido", 401