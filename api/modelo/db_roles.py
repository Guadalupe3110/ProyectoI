from modelo.conexion import CL_Conexion

class CL_RolesDB:

    def roles(self):
        sql = "select * FROM Roles"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
    
    def prueba(self):
        try:
            storedProc = "CALL proyecto_web_noticias.PA_SeleccionarNoticias()"
            self.data = CL_Conexion().get_DB(storedProc)
            return self.data 
        except Exception as e:
            print("Error: %s" % e)
