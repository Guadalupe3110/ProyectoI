from modelo.db_roles import CL_RolesDB
class CL_Roles:

    #Retorna todos los roles de la base de datos
    def FN_ObtenerRoles(self):
        return CL_RolesDB().FN_ObtenerRoles()