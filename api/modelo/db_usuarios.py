from modelo.conexion import CL_Conexion
class CL_UsuarioDB:

    #Insertar en la base de datos un nuevo usuario
    def FN_NuevoUsuario(self,usuario):
        usuario = usuario['Usuario']
        query = """INSERT INTO Users 
				(email, first_name, last_name, idRoles, password) 
				VALUES (%s, %s, %s, %s, %s)"""
        val = (usuario['email'],usuario['first_name'],usuario['last_name'],usuario['idRoles'],usuario['password'])
        usu = CL_Conexion().set_DB(query, val)
        usuario['id'] = usu
        usuario['Usuario'] = usuario
        return usuario
    
    #Select para el login de un usuario con inner join para saber el rol de usuario logueado
    def FN_Login(self, email, contrasena):
        query = "SELECT u.*, r.* FROM Users as u  INNER JOIN Roles AS r ON u.idRoles  = r.idRoles WHERE u.email = %s AND u.password = %s"
        val = (email, contrasena)
        self.data = CL_Conexion().get_DB_value(query, val)
        if len(self.data) != 0:
            return self.data[0]
        return False
    
    def FN_ModificarUsuario(self, usuario):
        query = "UPDATE Users SET token = %s WHERE idUsers = %s"
        val = (usuario['token'], usuario['idUsers'])
        print(val)
        CL_Conexion().set_DB(query, val)
        return True