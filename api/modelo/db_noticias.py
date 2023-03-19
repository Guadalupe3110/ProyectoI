from modelo.conexion import CL_Conexion

class CL_NoticiasDB:
    
    #Funcion para crear nueva new de noticia
    def FN_NuevaNoticia(self, noticia):
        new = noticia['Noticia']
        query = """INSERT INTO News 
				(title,short_description,permanlink,date,idNewsSource,idUsers,idCategories) 
				VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        val = (new['title'],new['short_description'],new['permanlink'],new['date'],new['idNewsSource'],new['idUsers'],new['idCategories'])
        idnew = CL_Conexion().set_DB(query, val)
        noticia['Noticia']['id'] = idnew
        return True