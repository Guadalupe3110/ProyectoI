
from modelo.conexion import CL_Conexion
from flask import request, session

class CL_FuentesNoticiasDB:

    
    #Retorna todas las fuentes de noticias
    def FN_ObtenerFuentes(self):
        sql = "SELECT * FROM NewsSources"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
    
     #Funcion para crear nueva fuente de noticia
    def FN_NuevaFuente(self, fuente):
        fuente = fuente['Fuente']
        query = """INSERT INTO NewsSources 
				(url,name,idCategories,idUsers) 
				VALUES (%s,%s,%s,%s)"""
        val = (fuente['url'],fuente['name'],fuente['idCategories'],session['user']['idUsers'])
        cat = CL_Conexion().set_DB(query, val)
        fuente['id'] = cat
        fuente['Fuente'] = fuente
        return fuente
    
     #Obtener todas una fuente de noticia por id de la base de datos
    def FN_ObtenerFuenteID(self, id):
        sql = "SELECT * FROM NewsSources WHERE idNewsSources = %s"
        val = (id,)
        self.data = CL_Conexion().get_DB_value(sql, val)
        return self.data
    
    #Funcion para modificar fuente de noticia
    def FN_EditarFuente(self, categoria, id):
        fuente = categoria['Fuente']
        query = "UPDATE NewsSources SET url = %s, name = %s, idCategories = %s  WHERE idNewsSources = %s"
        val = ( fuente['url'],fuente['name'],fuente['idCategories'], id)
        CL_Conexion().set_DB(query, val)
        categoria['Fuente']['idNewsSources'] = id
        return categoria
    
     #Verifica si una una noticia esta relacionada a una fuente de noticia
    def FN_VerificarEliminarFuente(self, id):
        sql = "SELECT ns.* FROM NewsSources ns INNER JOIN News AS n ON ns.idNewsSources = n.idNewsSource WHERE ns.idNewsSources = %s"
        val = (id,)
        self.data = CL_Conexion().get_DB_value(sql, val)
        if len(self.data) != 0:
            return True
        return False
    
    #Funcion para eliminar fuente
    def FN_EliminarFuente(self, id):
        query = "DELETE FROM NewsSources WHERE idNewsSources = %s"
        val = (id, )
        CL_Conexion().set_DB(query, val)
        return True