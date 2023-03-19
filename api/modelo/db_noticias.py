from modelo.conexion import CL_Conexion

class CL_NoticiasDB:
    
    #Funcion para crear nueva fuente de noticia
    def FN_NuevaNoticia(self, fuente):
        fuente = fuente['Noticia']
        query = """INSERT INTO NewsSources 
				(url,name,idCategories,idUsers) 
				VALUES (%s,%s,%s,%s)"""
        val = (fuente['url'],fuente['name'],fuente['idCategories'],session['user']['idUsers'])
        cat = CL_Conexion().set_DB(query, val)
        fuente['id'] = cat
        fuente['Fuente'] = fuente
        return fuente