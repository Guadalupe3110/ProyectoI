from modelo.db_categorias import CL_CategoriasDB
class CL_Categorias:

    #Obtiene todas las categoria registradas por el administrador
    def FN_ObtenerCategorias(self):
        return CL_CategoriasDB().FN_ObtenerCategorias()