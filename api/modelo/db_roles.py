from modelo.conexion import CL_Conexion

class CL_RolesDB:

    #Obtiene todos los roles de la base de datos
    def FN_ObtenerRoles(self):
        sql = "select * FROM Roles"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
    
   
    

