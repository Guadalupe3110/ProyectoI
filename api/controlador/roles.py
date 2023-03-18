from modelo.db_roles import CL_RolesDB
import json

class CL_Roles:

    #Retorna todos los roles de la base de datos
    def FN_ObtenerRoles(self):
        roles = CL_RolesDB().FN_ObtenerRoles()
        if roles:
            json_data = json.dumps(roles)
            return json_data, 200
        else:
            return "No se encontraron roles", 204