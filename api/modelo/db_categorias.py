from modelo.conexion import CL_Conexion

class CL_CategoriasDB:

    #Obtener todas las categorias de la base de datos
    def FN_ObtenerCategorias(self):
        sql = "select * FROM Categories"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
