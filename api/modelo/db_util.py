from modelo.conexion import CL_Conexion
from flask import session

class CL_UtilDB:
    
    #Funcion obtiene un objeto segun la informacion brindada, segun su tabla, columna y id
    def FN_ObtenerInsert(self, id, columna, tabla):
        sql = "SELECT * FROM " + tabla +" WHERE " + columna + "=" + id
        self.data = CL_Conexion().get_DB(sql)
        return self.data