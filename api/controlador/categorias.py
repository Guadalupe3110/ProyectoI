from modelo.db_categorias import CL_CategoriasDB
from flask import request, session

class CL_Categorias:

    #Obtiene todas las categoria registradas por el administrador
    def FN_ObtenerCategorias(self):
        return CL_CategoriasDB().FN_ObtenerCategorias()
    
    #Funcion para intertar categoria
    def FN_InsertarCategoria(self):
        token = request.headers.get('token')
        print(token)
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            print(session['user']['idRoles'])
            if session['user']['idRoles'] == 1:
                contenido = request.get_json(force = True)
                respuesta = {"Categoria": contenido}
                respuesta = CL_CategoriasDB().FN_NuevaCategoria(respuesta)#Insertar categoria en base de datos 
                if(len(respuesta) != 0):
                    res = "200 OK: Categoria creado con exito"
                else:
                    res = "Error 400"
                return res
            else:
                return "Usuario sin permisos"
        else:
            return "Token invalido"