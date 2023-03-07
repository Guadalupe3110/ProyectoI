from modelo.conexion import CL_Conexion

class CL_CategoriasDB:

    #Obtener todas las categorias de la base de datos
    def FN_ObtenerCategorias(self):
        sql = "select * FROM Categories"
        self.data = CL_Conexion().get_DB(sql)
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
