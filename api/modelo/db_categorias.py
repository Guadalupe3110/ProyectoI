from modelo.conexion import CL_Conexion

class CL_CategoriasDB:

    #Obtener todas las categorias de la base de datos
    def FN_ObtenerCategorias(self):
        sql = "SELECT * FROM Categories"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
    
    #Obtener todas una categoria por id de la base de datos
    def FN_ObtenerCategoriasID(self, id):
        sql = "SELECT * FROM Categories WHERE idCategories = %s"
        val = (id,)
        self.data = CL_Conexion().get_DB_value(sql, val)
        return self.data
    
    #Funcion para crear nueva categoria
    def FN_NuevaCategoria(self, categoria):
        categoria = categoria['Categoria']
        query = """INSERT INTO Categories 
				(name) 
				VALUES (%s)"""
        val = (categoria['name'],)
        cat = CL_Conexion().set_DB(query, val)
        categoria['id'] = cat
        categoria['Categoria'] = categoria
        return categoria
    
    #Funcion para modificar categoria
    def FN_EditarCategoria(self, categoria, id):
        cat = categoria['Categoria']
        query = "UPDATE Categories SET name = %s WHERE idCategories = %s"
        val = ( cat['name'], id)
        CL_Conexion().set_DB(query, val)
        categoria['Categoria']['idCategories'] = id
        return categoria
    
    #Verifica si una una noticia o fuente de noticia esta relacionada a una categoria
    def FN_VerificarEliminarCategoria(self, id):
        sql = "SELECT c.* FROM Categories c INNER JOIN News AS n ON c.idCategories = n.idCategories INNER JOIN NewsSources AS ns ON c.idCategories = ns.idCategories WHERE c.idCategories = %s"
        val = (id,)
        self.data = CL_Conexion().get_DB_value(sql, val)
        if len(self.data) != 0:
            return True
        return False

     #Funcion para eliminar categoria
    def FN_EliminarCategoria(self, id):
        query = "DELETE FROM Categories WHERE idCategories = %s"
        val = (id, )
        CL_Conexion().set_DB(query, val)
        return True
