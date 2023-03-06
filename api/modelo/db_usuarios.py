from modelo.conexion import CL_Conexion
import hashlib
import secrets
class CL_UsuarioDB:

    def FN_NuevoUsuario(self,usuario):
        usuario = usuario['Usuario']
        usuario['token'] = secrets.token_hex(16)
        usuario['token'] = hashlib.md5(usuario['token'].encode())
        query = """INSERT INTO Users 
				(email, first_name, last_name, idRoles, token) 
				VALUES (%s, %s, %s, %s, %s)"""
        val = (usuario['email'],usuario['first_name'],usuario['last_name'],usuario['idRoles'], usuario['token'].hexdigest())
        usu = CL_Conexion().set_DB(query, val)
        usuario['id'] = usu
        usuario['Usuario'] = usuario
        return usuario
    
    def FN_Login(self, email, contrasena):
        query = "SELECT u.*, r.* FROM Users as u  INNER JOIN Roles AS r ON u.idRoles  = r.idRoles WHERE u.email = %s AND u.password = %s"
        val = (email, contrasena)
        self.data = CL_Conexion().get_DB_value(query, val)
        resultado = []
        for result in self.data:
            resultado.append(self.data[result])
        return resultado