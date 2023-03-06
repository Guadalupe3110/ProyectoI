from modelo.db_roles import CL_RolesDB
class CL_Roles:

    def FN_ObtenerRoles(self):
        return CL_RolesDB().FN_ObtenerRoles()