from modelo.conexion import CL_Conexion

class CL_RolesDB:

    def roles(self):
        sql = "select * FROM Roles"
        self.data = CL_Conexion().get_DB(sql)
        return self.data
