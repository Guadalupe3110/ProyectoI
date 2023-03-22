from modelo.conexion import CL_Conexion
from flask import session

class CL_NoticiasDB:
    
    #Funcion para crear nueva new de noticia
    def FN_NuevaNoticia(self, noticia):
        new = noticia['Noticia']
        query = """INSERT INTO News 
				(title,short_description,permanlink,date,idNewsSource,idUsers,idCategories) 
				VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        print(new['idNewsSource'])
        print(type(new['idNewsSource']))
        val = (new['title'],new['short_description'],new['permanlink'],new['date'],new['idNewsSource'],new['idUsers'],new['idCategories'])
        idnew = CL_Conexion().set_DB(query, val)
        noticia['Noticia']['id'] = idnew
        return True
    
    #Obtener las noticias de usuario logueado
    def FN_ObtenerNoticiaUsuario(self):
        sql = "SELECT * FROM News WHERE idUsers = %s"
        val = (session['user']['idUsers'],)
        self.data = CL_Conexion().get_DB_value(sql, val)
        return self.data
    
    #Obtener las noticias de usuario logueado y por categoria
    def FN_ObtenerNoticiaUsuarioCategoria(self, idCategoria):
        sql = "SELECT * FROM News WHERE idUsers = %s AND idCategories = %s"
        val = (session['user']['idUsers'],idCategoria)
        self.data = CL_Conexion().get_DB_value(sql, val)
        return self.data