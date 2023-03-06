from modelo.conexion import CL_Conexion

class CL_UsuarioDB:

    def FN_NuevoUsuario(self,usuario):
        usuario = usuario['Usuario']
        query = """INSERT INTO Users 
				(email, first_name, last_name, idRoles) 
				VALUES (%s, %s, %s, %s)"""
        val = (usuario['email'],usuario['first_name'],usuario['last_name'],usuario['idRoles'])
        usu = CL_Conexion().set_DB(query, val)
        usuario['id'] = usu
        usuario['Usuario'] = usuario
        return usuario